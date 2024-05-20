const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(bodyParser.json());

mongoose
  .connect("mongodb://localhost:27017/articleDB", {})
  .then(() => console.log("MongoDB connected..."))
  .catch((err) => console.log(err));

const articles = require("./routes");
app.use("/api/articles", articles);

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));