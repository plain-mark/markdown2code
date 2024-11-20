// manifest.json
{
  "manifest_version": 2,
  "name": "Code Block Extractor",
  "version": "1.0",
  "description": "Extracts code blocks from chat interfaces",
  "permissions": [
    "activeTab",
    "http://localhost:5000/"
  ],
  "content_scripts": [{
    "matches": [
      "*://*.discord.com/*",
      "*://*.claude.ai/*",
      "*://*.chat.openai.com/*"
    ],
    "js": ["content.js"]
  }]
}

// content.js
function extractCodeBlocks() {
  // Match common chat interfaces' code block elements
  const selectors = [
    // Discord
    'code', 
    '.markup-2BOw-j code',
    // Claude
    '.prose code',
    // ChatGPT  
    '.markdown-renderer code'
  ];

  const codeBlocks = [];
  
  selectors.forEach(selector => {
    document.querySelectorAll(selector).forEach(element => {
      // Skip inline code
      if (!element.closest('pre')) return;
      
      const code = element.textContent;
      const language = element.className.match(/language-(\w+)/)?.[1] || 'text';
      
      codeBlocks.push({
        code,
        language,
        timestamp: new Date().toISOString()
      });
    });
  });

  return codeBlocks;
}

function sendToLocalhost(codeBlocks) {
  fetch('http://localhost:5000/code-blocks', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(codeBlocks)
  })
  .then(response => console.log('Code blocks sent successfully'))
  .catch(error => console.error('Error sending code blocks:', error));
}

// Extract and send code blocks every 5 seconds
setInterval(() => {
  const blocks = extractCodeBlocks();
  if (blocks.length > 0) {
    sendToLocalhost(blocks);
  }
}, 5000);

// Add keyboard shortcut (Ctrl+Shift+E)
document.addEventListener('keydown', (e) => {
  if (e.ctrlKey && e.shiftKey && e.key === 'E') {
    const blocks = extractCodeBlocks();
    if (blocks.length > 0) {
      sendToLocalhost(blocks);
      alert(`Sent ${blocks.length} code block(s) to localhost:5000`);
    } else {
      alert('No code blocks found on this page');
    }
  }
});
