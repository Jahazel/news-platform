import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [articleList, setArticleList] = useState([]);

  useEffect(() => {
    axios
      .get("/api/articles")
      .then((response) => {
        console.log("response", response);
        setArticleList(response.data);
      })
      .catch((error) => {
        if (error.response) {
          console.error("Error response:", error.response);
        } else if (error.request) {
          console.error("Error request:", error.request);
        } else {
          console.error("Error message:", error.message);
        }
      });
  }, []);

  return (
    <>
      <div>
        <h1>Articles</h1>
        <ul>
          {articleList.map((item) => (
            <li key={item._id}>
              <h3>{item.title}</h3>
              <p>{item.url}</p>
              <p>{item.author}</p>
              <p>{item.publishedDate}</p>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

export default App;
