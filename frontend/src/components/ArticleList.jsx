import React from "react";
import "../App.css";

const ArticleList = ({ articles }) => {
  return (
    <div className="article-list">
      {articles.map((article, index) => (
        <div key={index} className="article">
          <h2 className="article-title">{article.title}</h2>
          <p className="article-author">{article.author}</p>
          <a href={article.url} target="_blank" className="article-link">
            Read more
          </a>
        </div>
      ))}
    </div>
  );
};

export default ArticleList;
