import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:3001/api/articles")
      .then((response) => {
        setArticles(response.data);
      })
      .catch((error) => {
        console.error("Error fetching articles:", error);
      });
  }, []);

  return (
    <>
      <div className="App">
        <h1>The Latest</h1>
        <ul>
          {articles.map((article) => (
            <li key={article._id}>
              <h2>{article.title}</h2>
              <p>{article.author}</p>
              <a href={article.url} target="_blank">
                Read more
              </a>
              <p>
                Published on:{" "}
                {new Date(article.publishedDate).toLocaleDateString()}
              </p>
              <div className="divider"></div>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

export default App;
