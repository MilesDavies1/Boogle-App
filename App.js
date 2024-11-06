import React, { useState, useEffect } from "react";
import Board from "./Board";
import WordList from "./WordList";
import Timer from "./Timer";
import Controls from "./Controls";

const App = () => {
  const [board, setBoard] = useState(generateBoard());
  const [wordsFound, setWordsFound] = useState([]);
  const [currentWord, setCurrentWord] = useState("");
  const [timer, setTimer] = useState(60); // 60 seconds countdown
  const [isGameStarted, setIsGameStarted] = useState(false);
  const [isGameStopped, setIsGameStopped] = useState(false);

  useEffect(() => {
    let countdown;
    if (isGameStarted && !isGameStopped && timer > 0) {
      countdown = setInterval(() => {
        setTimer((prev) => prev - 1);
      }, 1000);
    } else if (timer === 0) {
      clearInterval(countdown);
      setIsGameStopped(true);
    }

    return () => clearInterval(countdown);
  }, [isGameStarted, isGameStopped, timer]);

  const handleStart = () => {
    setIsGameStarted(true);
    setIsGameStopped(false);
    setTimer(60); // Reset the timer
    setWordsFound([]);
  };

  const handleStop = () => {
    setIsGameStopped(true);
  };

  const handleWordSubmit = () => {
    if (wordsFound.includes(currentWord)) {
      alert("You've already found this word!");
    } else {
      setWordsFound((prevWords) => [...prevWords, currentWord]);
    }
    setCurrentWord("");
  };

  return (
    <div>
      <Controls
        onStart={handleStart}
        onStop={handleStop}
        isStarted={isGameStarted}
      />
      <Timer timeLeft={timer} />
      {isGameStarted && !isGameStopped && (
        <Board
          board={board}
          currentWord={currentWord}
          setCurrentWord={setCurrentWord}
        />
      )}
      <WordList words={wordsFound} />
    </div>
  );
};

export default App;
