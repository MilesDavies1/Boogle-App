import React from "react";

const Timer = ({ timeLeft }) => {
  return (
    <div className="timer">
      <h2>Time Left: {timeLeft} seconds</h2>
    </div>
  );
};

export default Timer;
