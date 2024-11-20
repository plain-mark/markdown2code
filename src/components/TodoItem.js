import React from 'react';

function TodoItem({ todo, todos, setTodos }) {
    const toggleTodo = () => {
        setTodos(todos.map(t =>
            t.id === todo.id ? { ...t, completed: !t.completed } : t
        ));
    };

    const deleteTodo = () => {
        setTodos(todos.filter(t => t.id !== todo.id));
    };

    return (
        <div className="todo-item">
            <input
                type="checkbox"
                checked={todo.completed}
                onChange={toggleTodo}
            />
            <span style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>
                {todo.text}
            </span>
            <button onClick={deleteTodo}>Delete</button>
        </div>
    );
}

export default TodoItem;
```

Finally, the entry point:
```javascript
