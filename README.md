# Backgammon Tournament System

This is a Python-based system for organizing and managing a **Backgammon tournament**. It handles player registration, match scheduling, result entry, and winner determination. The system follows global tournament rules, including the "Mars" rule, and automatically tracks the scores and progress of the tournament.

---

## Features

- **Player Registration**: Add players with unique IDs and names.
- **Tournament Rounds**: Automatically schedules matches and tracks results.
- **Mars Rule**: If a player wins without the opponent moving any of their pieces off the board, the winner gets 2 points.
- **Manual Results Entry**: After each match, manually enter the winner's ID and whether the win was a Mars.
- **Bracket Display**: Shows the current status of the tournament, including players' scores and round progress.
- **Winner Announcement**: Declares the winner at the end of the tournament with their total score.

---

## Installation

To run this system, you need Python 3.x installed on your computer.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/backgammon-tournament.git
   cd backgammon-tournament
