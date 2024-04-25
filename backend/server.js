const express = require("express");
const cors = require("cors");
const app = express();
const PORT = process.env.PORT || 3001;
const mongoose = require("mongoose");
const Article = require("./models/article");

app.use(cors());

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

mongoose
  .connect("mongodb://localhost:27017/articleDB", {})
  .then(() => console.log("connected to MongoDB..."))
  .catch((err) => console.error("Could not connect to MongoDB..."));

app.get("/api/articles", async (req, res) => {
  try {
    const articles = await Article.find();
    console.log(`Found ${articles.length} articles`);
    res.json(articles);
  } catch (error) {
    console.error("Error fetching articles:", error);
    res.status(500).send("Server Error");
  }
});
