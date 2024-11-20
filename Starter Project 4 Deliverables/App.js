import React, { useState, useEffect } from "react";
import axios from "axios"; 
import Board from "./Board";
import WordList from "./WordList"; 
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
  const [board, setBoard] = useState(generateBoard());
  const [wordsFound, setWordsFound] = useState([]);
  const [currentWord, setCurrentWord] = useState("");
  const [timer, setTimer] = useState(60);
  const [isGameStarted, setIsGameStarted] = useState(false);
  const [isGameStopped, setIsGameStopped] = useState(false);
  const [error, setError] = useState("");
  const [validWords, setValidWords] = useState([]);
  const [playerName, setPlayerName] = useState(""); 
  const [gameSaved, setGameSaved] = useState(false); 
  const [savedGames, setSavedGames] = useState([]); // State to hold saved games

  // Fetch valid words and saved games from the backend when the component mounts
  useEffect(() => {
    axios.get("http://localhost:8000/api/words/") 
      .then((response) => {
        setValidWords(response.data); // Save valid words in state
      })
      .catch((error) => {
        console.error("Error fetching words:", error);
      });

    axios.get("http://localhost:8000/api/saved_games/") // Fetch saved games
      .then((response) => {
        setSavedGames(response.data); // Save saved games in state
      })
      .catch((error) => {
        console.error("Error fetching saved games:", error);
      });
  }, []);  // This effect runs once when the component is mounted

  const handleStart = () => {
    setIsGameStarted(true);
    setIsGameStopped(false);
    setTimer(60);
    setWordsFound([]); 
    setError(""); 
    setGameSaved(false); 
  };

  const handleStop = () => {
    setIsGameStopped(true);
    const remainingWords = validWords.filter(
      (word) => !wordsFound.includes(word)
    );
    alert(`Game over! You found ${wordsFound.length} words. Remaining words: ${remainingWords.join(", ")}`);
  };

  const handleWordSubmit = () => {
    if (wordsFound.includes(currentWord)) {
      setError("You've already found this word!");
    } else if (validWords.includes(currentWord)) {
      setWordsFound((prevWords) => [...prevWords, currentWord]);
      setError(""); 
    } else {
      setError("Invalid word!");
    }
    setCurrentWord(""); 
  };

  // Handle game save
  const handleSaveGame = () => {
    if (!playerName) {
      setError("Please enter a player name to save the game!");
      return;
    }

    const gameData = {
      playerName,
      wordsFound,
      remainingTime: timer,
    };

    axios
      .post("http://localhost:8000/api/save_game/", gameData) 
      .then((response) => {
        setGameSaved(true); 
        setError(""); 
        alert("Game saved successfully!");
      })
      .catch((error) => {
        console.error("Error saving game:", error);
        setError("Error saving the game. Please try again.");
      });
  };

  // Load a saved game
  const handleLoadSavedGame = (game) => {
    setPlayerName(game.player_name);
    setWordsFound(game.words_found);
    setTimer(game.remaining_time);
    setIsGameStarted(true);
    setIsGameStopped(false);
    setGameSaved(true);
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
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Input field for player name */}
      {!gameSaved && (
        <div className="save-game-container">
          <input
            type="text"
            placeholder="Enter your name to save the game"
            value={playerName}
            onChange={(e) => setPlayerName(e.target.value)}
          />
          <button onClick={handleSaveGame}>Save Game</button>
        </div>
      )}

      {/* Display list of saved games and load option */}
      <div className="saved-games-container">
        <h3>Saved Games</h3>
        <ul>
          {savedGames.map((game) => (
            <li key={game.id}>
              <span>{game.player_name}</span>
              <button onClick={() => handleLoadSavedGame(game)}>Load Game</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default App;
