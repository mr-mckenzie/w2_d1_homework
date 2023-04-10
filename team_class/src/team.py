class Team:
    def __init__ (self, input_team_name, input_players, input_coach):
        self.name = input_team_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_to_check):
        return player_to_check in self.players
    
    def play_game(self, win_or_lose):
        if win_or_lose == True:
            self.points += 3