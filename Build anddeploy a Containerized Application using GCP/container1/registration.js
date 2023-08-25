const express = require('express');
const { Firestore } = require('@google-cloud/firestore');

const app = express();
const db = new Firestore();

app.use(express.json());

app.post('/register', async (req, res) => {
  const { name, password, email, location } = req.body;

  // Store registration data in Firestore
  /*code based on
    https://firebase.google.com/docs/firestore/quickstart#node.js*/
  const regData = {
    name,
    password,
    email,
    location
  };

  await db.collection('Reg').add(regData);

  res.send('Registration successful!!');
});

app.listen(5000, () => {
  console.log('Registration Service running on port 5000');
});