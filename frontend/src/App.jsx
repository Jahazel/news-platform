import Header from "./components/Header";
import ArticleList from "./components/ArticleList";
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
      <ArticleList articles={articles} />
    </>
  );
}

export default App;
