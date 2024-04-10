import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [articleList, setArticleList] = useState([]);

  useEffect(() => {
    axios
      .get("/api/articles")
      .then((response) => {
        console.log("response" + response);
        setArticleList(response.data);
      })
      .catch((error) => console.error(error));
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
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

export default App;
