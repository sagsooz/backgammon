import random

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.wins = 0
        self.is_active = True
        self.score = 0  # Total score (includes wins and mars)

    def __str__(self):
        return f"{self.id}: {self.name} (Score: {self.score})"

    def win(self, mars=False):
        """Increase win count and adjust score with mars bonus if applicable."""
        self.wins += 1
        if mars:
            self.score += 2  # Mars gives 2 points
        else:
            self.score += 1

    def lose(self):
        """Set player as inactive after loss."""
        self.is_active = False


class Tournament:
    def __init__(self):
        self.players = []
        self.rounds = []
        self.current_round = 0

    def add_player(self, player_name):
        """Add a player with a unique ID."""
        player_id = len(self.players) + 1
        self.players.append(Player(player_id, player_name))

    def start_tournament(self):
        """Start the tournament and schedule the matches."""
        if len(self.players) < 2:
            print("At least two players are required to start the tournament.")
            return
        self.current_round = 1
        random.shuffle(self.players)  # Shuffle players for random pairing
        self.rounds.append(self.players.copy())  # Save players for the first round
        print(f"Starting tournament with {len(self.players)} players.")
        self.play_round()

    def play_round(self):
        """Play each round and schedule the next round automatically."""
        active_players = [p for p in self.players if p.is_active]
        
        if len(active_players) == 1:
            winner = active_players[0]
            print(f"\nTournament Winner: {winner.name} with {winner.score} points!")
            return

        next_round_players = []
        print(f"\n--- Round {self.current_round} ---")
        for i in range(0, len(active_players), 2):
            if i + 1 < len(active_players):
                player1 = active_players[i]
                player2 = active_players[i + 1]
                print(f"Match {i//2 + 1}: {player1} vs {player2}")
                winner_id = input("Enter the ID of the winner (1 or 2): ")
                mars = input("Was it a Mars win? (y/n): ").lower() == 'y'

                if winner_id == '1':
                    player1.win(mars)
                    player2.lose()
                    next_round_players.append(player1)
                    self.show_result(player1, player2, mars)
                elif winner_id == '2':
                    player2.win(mars)
                    player1.lose()
                    next_round_players.append(player2)
                    self.show_result(player2, player1, mars)
                else:
                    print("Invalid winner ID! Please enter 1 or 2.")
                    return
            else:
                print(f"{active_players[i]} automatically advances to the next round.")
                next_round_players.append(active_players[i])

        self.players = next_round_players
        self.current_round += 1
        self.rounds.append(self.players.copy())
        self.play_round()

    def show_result(self, winner, loser, mars):
        """Display the result of a match."""
        if mars:
            print(f"--- {winner.name} wins with a Mars! ---")
        else:
            print(f"--- {winner.name} wins! ---")
        print(f"Match Result: {winner.name} vs {loser.name}")
        print(f"Winner: {winner.name} - Current Score: {winner.score}")
        print(f"Loser: {loser.name} - Current Score: {loser.score}")
        print(f"----------------------------------\n")

    def show_bracket(self):
        """Display the current tournament bracket."""
        print("\nTournament Status:")
        for round_num, round_players in enumerate(self.rounds, 1):
            print(f"--- Round {round_num} ---")
            for p in round_players:
                status = "(Winner)" if p.wins > 0 else "(Active)"
                print(f"  {p} {status} {'(Eliminated)' if not p.is_active else ''}")


def main():
    tournament = Tournament()
    while True:
        print("\n1. Add Player")
        print("2. Start Tournament")
        print("3. Show Tournament Bracket")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            player_name = input("Enter player name: ")
            tournament.add_player(player_name)
        elif choice == '2':
            if len(tournament.players) < 2:
                print("You need at least two players to start the tournament.")
            else:
                tournament.start_tournament()
        elif choice == '3':
            tournament.show_bracket()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
