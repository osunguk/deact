import React, { Component } from 'react';
import './App.css';

class App extends Component{
  state = {
    todoList: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const todoList = await res.json();
      this.setState({
        todoList
      });
    } catch (e) {
      console.log(e)
    }
  }

  render() {
    return (
      <div>
        {
          this.state.todoList.map(todo => (
            <div key={todo.id}>
              <h1>{todo.name}</h1>
            </div>
          ))
        }
      </div>
    )
  }
}

export default App;
