const mongoose = require("mongoose");

// Define the schema for an article
const articleSchema = new mongoose.Schema({
  title: { type: String, required: true },
  url: { type: String, required: true },
  author: { type: String, required: true },
  publishedDate: { type: Date, required: true },
});
// Create a model from the schema
// A model allows for creating and reading documents from the underlying MongoDB database
const Article = mongoose.model("Article", articleSchema);

// Export the Article model for use in other parts of the application
module.exports = Article;
