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
