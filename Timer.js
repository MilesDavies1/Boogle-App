import React from "react";

const Timer = ({ timeLeft }) => {
  return (
    <div className="timer">
      <h3>Time Left: {timeLeft}s</h3>
    </div>
  );
};

export default Timer;
