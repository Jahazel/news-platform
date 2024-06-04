import React from "react";
import SearchBar from "./SearchBar";
import "../App.css";

const Header = ({ onSearch }) => {
  return (
    <>
      <div className="header-container">
        <h1>Readme.</h1>
        <SearchBar onSearch={onSearch} />
      </div>
    </>
  );
};

export default Header;
