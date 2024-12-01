const express = require('express');
const cors = require('cors'); // Allow cross-origin requests

const app = express();
const PORT = process.env.PORT || 5002;

app.use(cors()); // Enable CORS for all routes
app.use(express.json()); // Parse JSON bodies

// Sample endpoint to get users
app.get('/api/user', (req, res) => {
    res.json([{ id: 1, name: 'John Doe' }, { id: 2, name: 'Jane Doe' }]);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

