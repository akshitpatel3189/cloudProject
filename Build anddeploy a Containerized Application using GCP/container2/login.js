const express = require('express');
/*code based on
    https://firebase.google.com/docs/firestore/quickstart#node.js*/
const { Firestore } = require('@google-cloud/firestore');

const app = express();
const db = new Firestore();

app.use(express.json());

app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  try {
    // Check if login credentials are valid by querying the Firestore database
    /*code based on
    https://firebase.google.com/docs/firestore/quickstart#node.js*/
    const snapshot = await db.collection('Reg')
      .where('email', '==', email)
      .where('password', '==', password)
      .limit(1)
      .get();

    if (snapshot.empty) {
      res.status(401).json({ error: 'Invalid login credentials' });
      return;
    } 
    // Login successful
    const user = snapshot.docs[0].data();
    const userId = snapshot.docs[0].id;

    // Update user status to "online" in Firestore
    const stateRef = db.collection('state').doc(userId);
    await stateRef.set({ status: 'online', name: user.name });

    res.status(200).json({ name: user.name, message: 'Login successful' });
  } catch (error) {
    console.error('Error during login:', error);
    res.status(500).json({ error: 'Login failed' });
  }
});

const port = process.env.PORT || 5001;
app.listen(port, () => {
  console.log(`Login microservice listening on port ${port}`);
});