require("dotenv").config();
const express = require("express");
const articleRoutes = require("./routes/articles");
const mongoose = require("mongoose");

//Express app
const app = express();

//Middleware
app.use(express.json());

app.use((req, res, next) => {
  console.log(req.path, req.method);
  next();
});

//Routes
app.use("/api/articles", articleRoutes);

//Connect to DB
mongoose
  .connect(process.env.MONG_URI)
  .then(() => {
    //Listen for requests
    app.listen(process.env.PORT, () =>
      console.log(`Connected to DB and listening on port`, process.env.PORT)
    );
  })
  .catch((error) => {
    console.log(error);
  });
