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
      <form onSubmit={checkPw}>
        <img src={clogo} className="App-clogo" alt="clogo" />
       <input id="password" name="password" />
       <button>open sesame</button>
      </form>
    )}
    </>
   );
}

export default Login;