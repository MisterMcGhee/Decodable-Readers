import React, { useState } from 'react';
import clogo from './clogo.svg';
import './Login.css';
import App from './App';

function Login () {
    const [isVerified, setIsVerified] = useState(false);
  
    const checkPw = () => {
      // gets the current input value
      const answer = document.getElementById("password").value;
    
      if (answer === "yourSecretPassword") { 
        setIsVerified(true);
      } else {
        alert("Sorry, that's not it");
      }
    };
  
   return (
    <>
    {isVerified ? <App />
      :
     (
    <div className="Login">
        <header className="Login-header">
                <img src={clogo} className="Login-clogo" alt="clogo" />
                <form onSubmit={checkPw} className="Login-form">
                    <input className="Login-input" placeholder="password" id="password" name="password"/>
                    <button className="Login-button">Login</button>
                </form>
        </header>
    </div>
    )}
    </>
   );
}

export default Login;