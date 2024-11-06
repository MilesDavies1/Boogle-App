import React from "react";

const WordList = ({ words }) => {
  return (
    <div className="word-list">
      <h2>Words Found</h2>
      <ul>
        {words.map((word, index) => (
          <li key={index}>{word}</li>
        ))}
      </ul>
    </div>
  );
};

export default WordList;
