import React, { useState, useEffect } from "react";
import Board from "./Board";
import WordList from "./WordList"; // Import the WordList component
import Timer from "./Timer";
import Controls from "./Controls";
import './App.css';

// Helper function to generate a 4x4 Boggle board
const generateBoard = () => {
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const board = [];
  for (let i = 0; i < 4; i++) {
    const row = [];
    for (let j = 0; j < 4; j++) {
      row.push(letters.charAt(Math.floor(Math.random() * letters.length)));
    }
    board.push(row);
  }
  return board;
};

const App = () => {
  const [board, setBoard] = useState(generateBoard()); // Call generateBoard to set initial board
  const [wordsFound, setWordsFound] = useState([]);
  const [currentWord, setCurrentWord] = useState("");
  const [timer, setTimer] = useState(60); // 60 seconds countdown
  const [isGameStarted, setIsGameStarted] = useState(false);
  const [isGameStopped, setIsGameStopped] = useState(false);
  const [error, setError] = useState(""); // Error state for duplicate word notification

  // A predefined list of valid words (you could expand this or load from an external dictionary)
  const validWords = ["CAT", "DOG", "BAT", "TIGER", "RAT", "BAG", "GAT", "TIER"];

  // Timer countdown logic
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

  // Start button handler
  const handleStart = () => {
    setIsGameStarted(true);
    setIsGameStopped(false);
    setTimer(60); // Reset the timer
    setWordsFound([]);
    setError(""); // Clear error when the game starts
  };

  // Stop button handler
  const handleStop = () => {
    setIsGameStopped(true);
    const remainingWords = validWords.filter(
      (word) => !wordsFound.includes(word)
    );
    alert(`Game over! You found ${wordsFound.length} words. Remaining words: ${remainingWords.join(", ")}`);
  };

  // Submit word handler
  const handleWordSubmit = () => {
    if (wordsFound.includes(currentWord)) {
      setError("You've already found this word!"); // Show error message
    } else {
      setWordsFound((prevWords) => [...prevWords, currentWord]);
      setError(""); // Clear error if the word is new
    }
    setCurrentWord(""); // Clear input after submission
  };

  return (
    <div className="app-container">
      <Controls onStart={handleStart} onStop={handleStop} isStarted={isGameStarted} />
      <Timer timeLeft={timer} />
      {isGameStarted && !isGameStopped && (
        <Board
          board={board}
          currentWord={currentWord}
          setCurrentWord={setCurrentWord}
        />
      )}
      <WordList words={wordsFound} />
      {error && <p style={{ color: "red" }}>{error}</p>} {/* Display error message */}
    </div>
  );
};

export default App;
