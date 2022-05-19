import React, { useState } from "react";
import axios from "axios";

const Form = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const handleSubmit = (e) => {
    e.preventDefault();
    setUsername("");
    setPassword("");
    axios
      .post("http://localhost:3001/login", {
        user: username,
        pass: password,
      })
      .then((result) => {
        if (result.data === "Success") {
          window.location.pathname = "/dashboard";
        } else {
          alert("Wrong username / password");
        }
      })
      .catch((error) => {
        throw error;
      });
  };
  return (
    <form className="form" method="POST" onSubmit={(e) => handleSubmit(e)}>
      <input
        type={"text"}
        placeholder={"username"}
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type={"password"}
        placeholder={"password"}
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Login</button>
    </form>
  );
};

export default Form;
