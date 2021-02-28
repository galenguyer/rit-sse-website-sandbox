import './App.css';
import React, { Component } from 'react';
import Cookies from 'js-cookie';

class App extends Component {
  state = {
    email:
      Cookies.get('email') != null ? Cookies.get('email') : 'Not Logged In',
    loggedIn: Cookies.get('email') != null
  };

  render() {
    return (
      <div className="App">
        <p>
          {this.state.loggedIn ? (
            this.state.email
          ) : (
            <a
              href={
                process.env.REACT_APP_API_HOST +
                '/api/v0/login?redirect=' +
                window.location.href
              }
            >
              Log in!
            </a>
          )}
        </p>
      </div>
    );
  }
}

export default App;
