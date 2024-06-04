import Header from "./components/Header";
import React, { useState } from "react";

function App() {
  const [articles, setArticles] = useState([]);

  const fetchArticles = async (query) => {
    try {
      const response = await fetch(`http://localhost:3001/search?q=${query}`);
      const data = await response.json();
      setArticles(data);
    } catch (error) {
      console.error("Error fetching articles:", error);
    }
  };

  return (
    <>
      <Header onSearch={fetchArticles} />
      <div className="article-list">
        {articles.map((article, index) => (
          <div key={index} className="article">
            <h2>{article.title}</h2>
            <p>{article.author}</p>
            <a href={article.url}>Read more</a>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
