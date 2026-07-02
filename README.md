# ✊ 📄 ✂️ Rock, Paper, Scissors

A classic Rock–Paper–Scissors game for your terminal — play against the computer, track your wins, losses, and draws, and challenge yourself to beat the odds!

```
        ROCK          PAPER         SCISSORS
       _______        _______        _______
   ---'   ____)    ---'   ____)__   ---'   ____)____
         (_____)          ______)        ______)
         (_____)         _______)       _______)
         (____)        __/               __/
   ---.__(___)     ---.__________)   ---.__________)
```

## 🎮 About the Game

This is a simple yet complete command-line implementation of Rock, Paper, Scissors built in Python. It features an interactive menu, input validation, a running scoreboard, and clean round-by-round results — all playable directly from your terminal.

## ✨ Features

| Feature | Description |
|---|---|
| 🖥️ Interactive Menu | Simple numbered menu to choose your move or exit |
| 🛡️ Input Validation | Handles invalid or non-numeric input gracefully |
| 🤖 Computer Opponent | Computer randomly picks Rock, Paper, or Scissors |
| 🏆 Live Scoreboard | Tracks Wins, Losses, and Draws across the session |
| 🔁 Replay Loop | Keep playing round after round until you choose to exit |
| 📊 Final Summary | Displays your final results when you quit |

## 🧩 The Rules

```
   ROCK      beats      SCISSORS
   SCISSORS  beats      PAPER
   PAPER     beats      ROCK
```

```
        🪨  Rock
         ╲
          ╲  crushes
           ╲
    ✂️ Scissors ──── cuts ──── 📄 Paper
           ╱
          ╱  covers
         ╱
        📄 Paper
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6+

### Run the game
```bash
python rock_paper_scissors.py
```

## 🕹️ How to Play

1. Run the script — you'll see the welcome menu.
2. Enter a number to choose your move:

   ```
   1 : Rock
   2 : Paper
   3 : Scissor
   4 : Exit
   ```
3. The computer randomly selects its move.
4. The winner of the round is announced, and your scoreboard updates.
5. Keep playing, or enter `4` to exit and see your final results.

### Example Round

```
....Welcome! to Rock, Paper, Scissors....
Here are your choices.
1 : Rock
2 : Paper
3 : Scissor
4 : Exit
Enter your choice :1

You Win!
You : Rock || Computer : Scissor
Scores...
You : 1
Computer : 0
Draws: 0
```

## 🗂️ Project Structure

```
rock_paper_scissors.py
├── display_menu()        # Prints the game menu
├── get_user_choice()     # Validates and returns the player's move
├── get_computer_choice() # Generates a random move for the computer
├── decide_winner()       # Core game logic — determines round outcome
├── update_score()        # Updates and prints the scoreboard
└── play_game()           # Main game loop
```

## 🧠 How the Winner Is Decided

The game uses modular arithmetic on the move values (`1 = Rock`, `2 = Paper`, `3 = Scissor`) to determine the outcome without a long chain of if/else comparisons:

- **Difference = 0** → Draw 🤝
- **(computer − user) % 3 == 1** → Computer wins 🤖
- **Otherwise** → User wins 🎉

## 📈 Sample Final Results

```
Thanks for playing.
Final Results:
You : 5 || Computer : 3 || Draws : 2
```

## 🛠️ Possible Future Improvements

- [ ] Add a "Best of N" tournament mode
- [ ] Add colored terminal output (e.g., using `colorama`)
- [ ] Add a GUI version with `tkinter` or a web version
- [ ] Save score history to a file
- [ ] Add difficulty levels for the computer opponent

## 📄 License

This project is open source and available for anyone to use, modify, and learn from.

---

<p align="center">Made with 🐍 Python — Have fun and may the odds be ever in your favor! 🏆</p>
