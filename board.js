import React from "react";

const Board = ({ board, currentWord, setCurrentWord }) => {
  const handleTileClick = (letter) => {
    setCurrentWord((prevWord) => prevWord + letter);
  };

  return (
    <div className="board">
      {board.map((row, rowIndex) => (
        <div key={rowIndex} className="row">
          {row.map((letter, colIndex) => (
            <button
              key={colIndex}
              className="tile"
              onClick={() => handleTileClick(letter)}
            >
              {letter}
            </button>
          ))}
        </div>
      ))}
      <div>
        <input
          type="text"
          value={currentWord}
          readOnly
          placeholder="Your word..."
        />
      </div>
    </div>
  );
};

export default Board;
