const express = require("express");
const router = express.Router();

//Get all articles
router.get("/", (req, res) => {
  res.json({ mssg: "GET all articles" });
});

//Get single article
router.get("/:id", (req, res) => {
  res.json({ mssg: "GET sinlge articles" });
});

module.exports = router;
