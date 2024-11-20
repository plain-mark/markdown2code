# project_sharing.py
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional
import requests
from dotenv import load_dotenv
import subprocess
import json
from dataclasses import dataclass
import time
from git import Repo
import gitlab
from github import Github
from bitbucket_api import Bitbucket

@dataclass
class RepoConfig:
    name: str
    description: str
    private: bool
    has_issues: bool = True
    has_wiki: bool = True
    has_projects: bool = True
    auto_init: bool = True
    gitignore_template: str = "Python"
    license_template: str = "mit"

class ProjectSharing:
    def __init__(self):
        load_dotenv()
        self.project_path = Path.cwd()
        self.project_name = self.project_path.name
        
        # Tokeny z .env
        self.tokens = {
            'github': os.getenv('GITHUB_TOKEN'),
            'gitlab': os.getenv('GITLAB_TOKEN'),
            'bitbucket': os.getenv('BITBUCKET_TOKEN'),
            'bitbucket_username': os.getenv('BITBUCKET_USERNAME')
        }
        
        # Sprawdzenie wymaganych tokenów
        missing_tokens = [k for k, v in self.tokens.items() if not v]
        if missing_tokens:
            print(f"Brakujące tokeny w .env: {', '.join(missing_tokens)}")
            print("Utwórz plik .env z odpowiednimi tokenami:")
            print("""
GITHUB_TOKEN=your_github_token
GITLAB_TOKEN=your_gitlab_token
BITBUCKET_TOKEN=your_bitbucket_token
BITBUCKET_USERNAME=your_bitbucket_username
            """)
            sys.exit(1)
        
        self.repo_config = self._create_repo_config()
    
    def _create_repo_config(self) -> RepoConfig:
        """Tworzy konfigurację repozytorium na podstawie plików projektu"""
        # Odczytaj opis z package.json lub setup.py jeśli istnieją
        description = self._get_project_description()
        
        return RepoConfig(
            name=self.project_name,
            description=description or f"Code blocks manager - {self.project_name}",
            private=False
        )
    
    def _get_project_description(self) -> Optional[str]:
        """Próbuje odczytać opis projektu z plików konfiguracyjnych"""
        if (self.project_path / 'package.json').exists():
            with open(self.project_path / 'package.json') as f:
                try:
                    return json.load(f).get('description')
                except json.JSONDecodeError:
                    pass
        
        if (self.project_path / 'setup.py').exists():
            # Próba odczytania opisu z setup.py
            try:
                with open(self.project_path / 'setup.py') as f:
                    content = f.read()
                    if 'description=' in content:
                        description = content.split('description=')[1].split(',')[0]
                        return description.strip('"\' ')
            except Exception:
                pass
        
        return None
    
    def _init_git(self) -> Repo:
        """Inicjalizuje lokalne repozytorium git"""
        if not (self.project_path / '.git').exists():
            repo = Repo.init(self.project_path)
            
            # Dodaj .gitignore jeśli nie istnieje
            gitignore_path = self.project_path / '.gitignore'
            if not gitignore_path.exists():
                with open(gitignore_path, 'w') as f:
                    f.write("""
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.env
code_blocks/
*.db
                    """)
            
            # Dodaj README.md jeśli nie istnieje
            readme_path = self.project_path / 'README.md'
            if not readme_path.exists():
                with open(readme_path, 'w') as f:
                    f.write(f"""# {self.project_name}

{self.repo_config.description}

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Set up environment variables in `.env`:
```
GITHUB_TOKEN=your_github_token
GITLAB_TOKEN=your_gitlab_token
BITBUCKET_TOKEN=your_bitbucket_token
BITBUCKET_USERNAME=your_bitbucket_username
```

2. Run the API:
```bash
python app.py
```

3. Run tests:
```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
                    """)
            
            # Dodaj plik LICENSE jeśli nie istnieje
            license_path = self.project_path / 'LICENSE'
            if not license_path.exists():
                with open(license_path, 'w') as f:
                    f.write(f"""MIT License

Copyright (c) {time.strftime("%Y")} {self.project_name}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
                    """)
            
            # Wykonaj początkowy commit
            repo.index.add(['.gitignore', 'README.md', 'LICENSE'])
            repo.index.commit("Initial commit")
        else:
            repo = Repo(self.project_path)
        
        return repo

    def create_github_repo(self) -> str:
        """Tworzy repozytorium na GitHub"""
        g = Github(self.tokens['github'])
        user = g.get_user()
        
        try:
            repo = user.create_repo(
                self.repo_config.name,
                description=self.repo_config.description,
                private=self.repo_config.private,
                has_issues=self.repo_config.has_issues,
                has_wiki=self.repo_config.has_wiki,
                has_projects=self.repo_config.has_projects,
                auto_init=False
            )
            return repo.clone_url
        except Exception as e:
            print(f"Błąd podczas tworzenia repozytorium na GitHub: {e}")
            return None

    def create_gitlab_repo(self) -> str:
        """Tworzy repozytorium na GitLab"""
        gl = gitlab.Gitlab('https://gitlab.com', private_token=self.tokens['gitlab'])
        
        try:
            project = gl.projects.create({
                'name': self.repo_config.name,
                'description': self.repo_config.description,
                'visibility': 'public' if not self.repo_config.private else 'private',
                'initialize_with_readme': False
            })
            return project.http_url_to_repo
        except Exception as e:
            print(f"Błąd podczas tworzenia repozytorium na GitLab: {e}")
            return None

    def create_bitbucket_repo(self) -> str:
        """Tworzy repozytorium na Bitbucket"""
        bitbucket = Bitbucket(
            username=self.tokens['bitbucket_username'],
            password=self.tokens['bitbucket_token']
        )
        
        try:
            response = bitbucket.repositories.create({
                'name': self.repo_config.name,
                'description': self.repo_config.description,
                'is_private': self.repo_config.private,
                'scm': 'git'
            })
            return f"https://bitbucket.org/{self.tokens['bitbucket_username']}/{self.repo_config.name}.git"
        except Exception as e:
            print(f"Błąd podczas tworzenia repozytorium na Bitbucket: {e}")
            return None

    def push_to_remote(self, repo: Repo, remote_url: str, platform: str):
        """Pushuje kod do zdalnego repozytorium"""
        try:
            remote_name = platform.lower()
            if remote_name in [r.name for r in repo.remotes]:
                remote = repo.remote(remote_name)
                remote.set_url(remote_url)
            else:
                remote = repo.create_remote(remote_name, remote_url)
            
            remote.push(refspec='master:master')
            print(f"Kod został pomyślnie wysłany do {platform}")
        except Exception as e:
            print(f"Błąd podczas wysyłania kodu do {platform}: {e}")

    def share_project(self):
        """Główna funkcja do udostępniania projektu"""
        print(f"Udostępnianie projektu: {self.project_name}")
        
        # Inicjalizacja git
        repo = self._init_git()
        
        # Tworzenie repozytoriów na różnych platformach
        platforms = {
            'GitHub': self.create_github_repo,
            'GitLab': self.create_gitlab_repo,
            'Bitbucket': self.create_bitbucket_repo
        }
        
        for platform, create_func in platforms.items():
            print(f"\nTworzenie repozytorium na {platform}...")
            remote_url = create_func()
            if remote_url:
                print(f"Repozytorium utworzone: {remote_url}")
                self.push_to_remote(repo, remote_url, platform)
            else:
                print(f"Nie udało się utworzyć repozytorium na {platform}")
        
        print("\nProjekt został pomyślnie udostępniony!")

if __name__ == '__main__':
    sharing = ProjectSharing()
    sharing.share_project()
