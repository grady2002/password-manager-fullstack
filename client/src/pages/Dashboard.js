import React, { useState, useEffect } from "react";
import axios from "axios";
import "../App.scss";

const Dashboard = () => {
  const [data, setData] = useState([]);
  const [name, setName] = useState("");
  const [pass, setPass] = useState("");
  const [site, setSite] = useState("");
  const [show, setShow] = useState(false);
  useEffect(() => {
    axios
      .get("http://localhost:3001/getdata")
      .then((result) => {
        setData(result.data);
      })
      .catch((error) => {
        throw error;
      });
  }, []);
  const deleteUser = (username) => {
    username === "admin"
      ? alert("Cannot delete admin")
      : axios
          .post("http://localhost:3001/delete", {
            name: username,
          })
          .then(() => {
            alert(`User "${username}" successfully deleted.`);
            window.location.reload();
          })
          .catch((error) => {
            throw error;
          });
  };
  const changePassword = (username) => {
    let newPass = prompt("Enter new password ");
    axios
      .post("http://localhost:3001/changepassword", {
        user: username,
        pass: newPass,
      })
      .then(() => {
        alert(`Password of ${username} changed to ${newPass}`);
        window.location.reload();
      })
      .catch((error) => {
        throw error;
      });
  };
  const addUser = (e, name, pass, wsite) => {
    e.preventDefault();
    axios
      .post("http://localhost:3001/adduser", {
        user: name,
        pass: pass,
        site: wsite,
      })
      .then(() => {
        alert(`User "${name}" added`);
        window.location.reload();
      })
      .catch((error) => {
        throw error;
      });
  };

  return (
    <React.Fragment>
      <div className="top">
        <h3 className="dashboard-header">Welcome, admin !</h3>
        <button className="show-passwords" onClick={() => setShow(!show)}>
          Show All Passwords
        </button>
      </div>
      <table className="table">
        <thead>
          <tr>
            <th>Username</th>
            <th>Password</th>
            <th>Website</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => {
            return (
              <tr key={index}>
                <td>{item.username}</td>
                <td>
                  {show
                    ? item.password
                    : item.password
                        .slice(item.password.length)
                        .padStart(item.password.length, "*")}
                </td>
                <td>{item.site}</td>
                <td className="flex-td">
                  <button
                    className="delete-user"
                    onClick={() => {
                      deleteUser(item.username);
                    }}
                  >
                    Delete User
                  </button>
                  <button
                    className="change-password"
                    onClick={() => {
                      changePassword(item.username);
                    }}
                  >
                    Change Password
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <form
        className="add-user"
        method="POST"
        onSubmit={(e) => addUser(e, name, pass, site)}
      >
        <input
          type={"text"}
          value={name}
          placeholder={"Username"}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type={"text"}
          value={pass}
          placeholder={"Password"}
          onChange={(e) => setPass(e.target.value)}
        />
        <input
          type={"text"}
          value={site}
          placeholder={"Site"}
          onChange={(e) => setSite(e.target.value)}
        />
        <button className="add-user-submit">Add User</button>
      </form>
    </React.Fragment>
  );
};

export default Dashboard;
