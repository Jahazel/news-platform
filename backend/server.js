const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const cors = require("cors");
const Article = require("./models/Article"); // Import the Article model

const app = express();

app.use(cors());
app.use(bodyParser.json());

mongoose
  .connect("mongodb://localhost:27017/articleDB", {})
  .then(() => console.log("MongoDB connected..."))
  .catch((err) => console.log(err));

app.get("/search", async (req, res) => {
  try {
    const query = req.query.q;
    const articles = await Article.find({
      title: { $regex: query, $options: "i" },
    });
    res.json(articles);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
