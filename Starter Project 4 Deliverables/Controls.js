import React from "react";

const Controls = ({ onStart, onStop, isStarted }) => {
  return (
    <div className="controls">
      {!isStarted ? (
        <button onClick={onStart}>Start</button>
      ) : (
        <button onClick={onStop}>Stop</button>
      )}
    </div>
  );
};

export default Controls;
