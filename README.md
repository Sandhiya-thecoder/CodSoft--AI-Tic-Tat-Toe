
<h1 align="center">🎮 Tic-Tac-Toe AI (with Minimax Algorithm)</h1>

<p align="center">
A classic <b>Tic-Tac-Toe</b> game built in Python where you play against an unbeatable AI powered by the <b>Minimax Algorithm</b>.  
Test your strategy and see if you can force a draw against the computer! 🤖✨
</p>

---

## 🧠 Overview

This project implements a **human vs AI Tic-Tac-Toe game** in the terminal.  
The AI uses the **Minimax algorithm** — a decision-making algorithm commonly used in game theory and artificial intelligence — to always make the best possible move.

---

## ⚙️ Features

- 🧍 Play as **X** against the AI (**O**)  
- 🧩 Smart AI powered by **Minimax Algorithm** (always optimal)  
- 🖥️ Simple console interface  
- 🏆 Detects **wins**, **draws**, and **invalid moves**  
- 🔁 Fully replayable — just run it again to start fresh

---

## 🎯 Learning Objectives

By studying this project, you will:
- Understand **game logic implementation** in Python  
- Learn how to apply the **Minimax algorithm** for decision-making  
- Practice **recursive functions** and **AI evaluation logic**  
- Strengthen skills in **Python conditionals, loops, and data structures**

---

## 🧩 How It Works

1. The board is represented as a list of 9 positions.  
2. The player goes first as `"X"`.  
3. The AI uses **Minimax** to simulate all possible future moves and chooses the best one.  
4. The game ends when either player wins or the board is full.

---

## 🕹️ How to Play

1. Run the Python script:

   ```bash
   python tic_tac_toe_ai.py
   ```

2. Enter your move (1–9) according to the following board layout:

   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

3. The AI will automatically make its move after yours.  
4. Keep playing until someone wins or the game ends in a draw.

---

## 📘 Example Gameplay

```
Welcome to Tic-Tac-Toe!
You are 'X'. AI is 'O'.

 |   |  
---------
 |   |  
---------
 |   |  

Enter your move (1-9): 5

AI is thinking...

🤖 AI wins! Better luck next time.
```

---

## 🧩 Algorithm Explained (Minimax)

The **Minimax algorithm** recursively explores all possible moves:
- **Maximizing player (AI)** tries to maximize its score.
- **Minimizing player (human)** tries to minimize AI’s score.
- Each terminal state (win/loss/draw) is assigned a value:
  - `+1` → AI wins  
  - `-1` → Human wins  
  - `0` → Draw  

The AI always chooses the move with the **maximum score** possible.

---

## 🧰 Requirements

- Python 3.x  
- No external libraries needed (uses only `math` and built-in functions)

---

## 🏁 Future Enhancements

- Add a **GUI** using `tkinter` or `pygame`
- Enable **AI difficulty levels** (Easy / Medium / Hard)
- Track game statistics and win rate

---

<p align="center">
Made with ❤️ in Python — because even classic games can teach modern AI logic!
</p>

