# 🎮 Tank Battle

An interactive shooting game built with **Python** and **Pygame**, inspired by the game *Identity V*.

> Note: Although it's called "Tank Battle," it's technically not a tank — we used the image of **"Jack the Dog"** (adapted from the hunter *Jack* in *Identity V*) as the player, and **"Naib the Edamame"** (adapted from the survivor *Naib*) as the target. The background is set in the **"Red Church"** map from *Identity V*.

---

## 👥 Team Information

This project was developed by:

- **Yunxian Ding**
- **Xiangyu Peng**

Since we both play *Identity V* and appreciate the relationship between two of its characters, we decided to create this fun interactive game together.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `main.py` | The main entry point. Initializes the menu and launches game modes. |
| `menu.py` | Handles the main menu (Infinite Mode, Time-Limited Mode, Help, Quit, View Score). |
| `game_module.py` | Core game loop logic — background, movement, shooting, collision, sound, game over screen. |
| `player.py` | Defines the `Player` class to handle the tank's movement and drawing. |
| `bullet.py` | Defines the `Bullet` class — moves bullets upward and detects collisions. |
| `character.py` | Defines the `Character` class — the target that moves randomly when hit. |
| `scores_manager.py` | Manages loading, saving, and updating player scores via `scores.json`. |
| `help_screen.py` | Displays the help/instructions screen. |
| `infinite_mode.py` | Starts the game in **Infinite Mode** (no time limit). |
| `time_limited_mode.py` | Starts the game in **Time-Limited Mode** (60 seconds). |
| `user_input.py` | Prompts the user to input their name at the start. |
| `scores.json` | Stores player scores as a JSON object. |
| `assets/` | Contains all images and sound effects used in the game. |

### 🎨 Assets

- `tank.png` — Jack the Dog (player)
- `character.png` — Naib the Edamame (target)
- `background.png` — Red Church
- `shoot.wav` — Shooting sound effect

---

## 🚀 How to Run

### Step 1: Prerequisites

Make sure you have **Python 3.8 or later** installed. Then install Pygame:

```bash
pip install pygame
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/pengxiangyu1003-ops/tank-battle.git
cd "tank-battle/Tank-Battle powerful ver"
```

### Step 3: Run the Game

```bash
python main.py
```

---

## 🎯 Gameplay

When you open the game, you'll see five buttons:

- **Infinite Mode** — Play without any time limit.
- **Time-Limited Mode** — Score as much as possible in 60 seconds.
- **Help** — View game controls and rules.
- **Quit** — Exit the game.
- **View Scores** — Check your previous scores.

### 🎮 Controls

| Key | Action |
|-----|--------|
| Arrow Keys | Move the tank |
| `Space` | Shoot bullets |
| `Esc` | Exit the help page |
| `X` (top-right corner) | Exit the game at any time |

---

## 📝 Notes

- The game automatically saves the highest score for the current player.
- Enjoy the game and have fun! 🎉
