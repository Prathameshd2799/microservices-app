const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// In-memory storage (NO DATABASE)
let users = [];

// POST API
app.post("/users", (req, res) => {
  const { name, email, contact } = req.body;

  const newUser = {
    id: users.length + 1,
    name,
    email,
    contact
  };

  users.push(newUser);

  res.json({
    message: "User saved successfully",
    data: newUser
  });
});

// GET API
app.get("/users", (req, res) => {
  res.json(users);
});

app.listen(3000, () => {
  console.log("Backend running at http://localhost:3000");
});