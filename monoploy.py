import random

class Monopoly:
    def __init__(self, players):
        self.players = players
        self.positions = {p: 0 for p in players}
        self.money = {p: 1500 for p in players}
        self.current_turn = 0
        self.board_size = 40

    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def move_player(self, player):
        roll = self.roll_dice()
        new_pos = (self.positions[player] + roll) % self.board_size
        self.positions[player] = new_pos
        return roll, new_pos

    def play_turn(self):
        player = self.players[self.current_turn]
        roll, new_pos = self.move_player(player)
        action = f"{player} rolled {roll} and moved to position {new_pos}."
        self.current_turn = (self.current_turn + 1) % len(self.players)
        return action
    
        

num_players = int(input("Enter number of players: "))
players = []
for i in range(num_players):
    name = input(f"Enter name of player {i+1}: ")
    players.append(name)


game = Monopoly(players)
n=int(input("enter"))
for i in range(n):  
    print(game.play_turn())
    
