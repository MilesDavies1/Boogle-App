import React from "react";

const Board = ({ board, currentWord, setCurrentWord }) => {
  // Handle tile click to build the word
  const handleTileClick = (letter) => {
    setCurrentWord(currentWord + letter);
  };

  return (
    <div className="board">
      {board.map((row, rowIndex) => (
        <div key={rowIndex} className="row">
          {row.map((tile, colIndex) => (
            <div
              key={colIndex}
              className="tile"
              onClick={() => handleTileClick(tile)}
            >
              {tile}
            </div>
          ))}
        </div>
      ))}
      <div className="input-container">
        <input
          type="text"
          value={currentWord}
          onChange={(e) => setCurrentWord(e.target.value)}
          placeholder="Type your word here"
        />
        <button onClick={() => setCurrentWord("")}>Clear</button>
      </div>
      <button onClick={() => setCurrentWord(currentWord)}>Submit</button>
    </div>
  );
};

export default Board;
