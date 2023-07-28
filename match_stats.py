from player import Player

class MatchStats:
    def __init__(self, match):
        self.match = match

    def get_shots_made(self, player):
        shots_made = 0
        for shot in self.match.get_shots():
            if shot.get_player() == player and shot.is_made():
                shots_made += 1
        return shots_made

    def get_shots_attempted(self, player):
        shots_attempted = 0
        for shot in self.match.get_shots():
            if shot.get_player() == player:
                shots_attempted += 1
        return shots_attempted

    def get_shooting_percentage(self, player):
        shots_made = self.get_shots_made(player)
        shots_attempted = self.get_shots_attempted(player)

        if shots_attempted == 0:
            return 0.0

        shooting_percentage = (shots_made / shots_attempted) * 100
        return shooting_percentage

    def overview(self):
        player_stats = []
        for player in self.match.get_visitor().get_players() + self.match.get_local().get_players():
            player_id = id(player)
            player_name = player.get_name()
            player_team = player.get_team()
            shots_made = self.get_shots_made(player)
            shots_attempted = self.get_shots_attempted(player)
            shooting_percentage = self.get_shooting_percentage(player)

            player_stat = {
                "Player ID": player_id,
                "Name": player_name,
                "Team": player_team,
                "Shots Made": shots_made,
                "Shots Attempted": shots_attempted,
                "Shooting Percentage": f"{shooting_percentage:.2f}%"
            }
            player_stats.append(player_stat)

        return player_stats
