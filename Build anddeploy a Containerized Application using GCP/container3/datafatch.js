const express = require('express');
//https://firebase.google.com/docs/firestore/quickstart#node.js
const { Firestore } = require('@google-cloud/firestore');

const app = express();
const db = new Firestore();

app.use(express.json())

app.get('/online-users', async (req, res) => {
  try {
    // Query Firestore for online users
    /*code based on
    https://firebase.google.com/docs/firestore/quickstart#node.js*/
    const stateRef = db.collection('state');
    /*code based on
    https://firebase.google.com/docs/firestore/quickstart#node.js*/
    const snapshot = await stateRef.where('status', '==', 'online').get();
    const onlineUsers = snapshot.docs.map((doc) => doc.data());

    res.status(200).json(onlineUsers);
  } catch (error) {
    console.error('Error retrieving online users:', error);
    res.status(500).json({ error: 'Failed to retrieve online users' });
  }
});


app.post('/logout', async (req, res) => {
  try {
    const userName = req.body.name; 

    // Update the user's status to "offline" in the database
    /*code based on
    https://firebase.google.com/docs/firestore/quickstart#node.js*/
    const stateRef = db.collection('state');
    /*code based on
    https://firebase.google.com/docs/firestore/quickstart#node.js*/
    const userSnapshot = await stateRef.where('name', '==', userName).get();

    if (userSnapshot.empty) {
      res.status(404).json({ error: 'User not found' });
    } else {
      const userId = userSnapshot.docs[0].id;
      await stateRef.doc(userId).update({ status: 'offline' });
      res.status(200).json({ message: 'Logout successful' });
    }
  } catch (error) {
    console.error('Error logging out:', error);
    res.status(500).json({ error: 'Failed to logout' });
  }
});



const port = process.env.PORT || 5002;
app.listen(port, () => {
  console.log(`State extraction microservice listening on port ${port}`);
});