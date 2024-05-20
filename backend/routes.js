const express = require("express");
const router = express.Router();
const Article = require("./models/article");

router.get("/", (req, res) => {
  Article.find()
    .sort({ publishedDate: -1 })
    .then((articles) => res.json(articles))
    .catch((err) =>
      res.status(500).json({ sucess: false, error: err.message })
    );
});

module.exports = router;
