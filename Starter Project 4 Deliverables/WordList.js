import React from "react";

const WordList = ({ words }) => {
  return (
    <div className="word-list">
      <h3>Words Found:</h3>
      <ul>
        {words.length > 0 ? (
          words.map((word, index) => <li key={index}>{word}</li>)
        ) : (
          <li>No words found yet!</li>
        )}
      </ul>
    </div>
  );
};

export default WordList;
