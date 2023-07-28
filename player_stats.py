from match import Match
from player import Player
from shot import Shot
from spot import Spot
from team import Team
from time_utils import random_datetime

class PlayerStats:
    def __init__(self, player):
        self.player = player
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def get_shots_made(self):
        shots_made = 0
        for match in self.matches:
            for shot in match.get_shots():
                if shot.get_player() == self.player and shot.is_made():
                    shots_made += 1
        return shots_made

    def get_shots_attempted(self):
        shots_attempted = 0
        for match in self.matches:
            for shot in match.get_shots():
                if shot.get_player() == self.player:
                    shots_attempted += 1
        return shots_attempted

    def get_shooting_percentage(self):
        shots_made = self.get_shots_made()
        shots_attempted = self.get_shots_attempted()

        if shots_attempted == 0:
            return 0.0

        shooting_percentage = (shots_made / shots_attempted) * 100
        return shooting_percentage

    def get_spot_shooting_percentages(self):
        spot_stats = {}  # Diccionario para almacenar porcentajes de acierto por spot
        for match in self.matches:
            for shot in match.get_shots():
                if shot.get_player() == self.player:
                    spot_name = shot.get_spot().get_name()
                    if spot_name not in spot_stats:
                        spot_stats[spot_name] = {"shots_made": 0, "shots_attempted": 0}

                    spot_stats[spot_name]["shots_attempted"] += 1
                    if shot.is_made():
                        spot_stats[spot_name]["shots_made"] += 1

        # Calcular porcentaje de acierto para cada spot
        for spot_name, stats in spot_stats.items():
            shots_made = stats["shots_made"]
            shots_attempted = stats["shots_attempted"]
            if shots_attempted == 0:
                spot_stats[spot_name]["shooting_percentage"] = 0.0
            else:
                spot_stats[spot_name]["shooting_percentage"] = (shots_made / shots_attempted) * 100

        return spot_stats

    def get_best_and_worst_spot(self):
        spot_stats = self.get_spot_shooting_percentages()

        best_spot = None
        worst_spot = None
        best_percentage = 0.0
        worst_percentage = 100.0

        for spot_name, stats in spot_stats.items():
            shooting_percentage = stats["shooting_percentage"]
            if shooting_percentage > best_percentage:
                best_spot = spot_name
                best_percentage = shooting_percentage

            if shooting_percentage < worst_percentage:
                worst_spot = spot_name
                worst_percentage = shooting_percentage

        return best_spot, best_percentage, worst_spot, worst_percentage



# Supongamos que player1 es un objeto de la clase Player
player1 = Player("Lionel Messi", 10, "Forward", "Paris Saint-Germain")
player2 = Player("Cristiano Ronaldo", 7, "Forward", "Manchester United")

# Crear equipos y agregar jugadores
team1 = Team()
team1.add_player(player1)

team2 = Team()
team2.add_player(player2)

# Crear spots
spot1 = Spot("Three-point line", "Nylon")
spot2 = Spot("Free-throw line", "Metal")

# Crear partido
match1 = Match(team1, team2, "August 5, 2023", "La Liga")
match2 = Match(team1, team2, "August 6, 2023", "La Ligo")

# Registrar tiros
shot1 = Shot(spot1, random_datetime(), True, player1)
shot2 = Shot(spot2, random_datetime(), False, player2)

# Agregar tiros al partido
match1.add_shot(shot1)
match2.add_shot(shot2)
# Supongamos que match1 y match2 son objetos de la clase Match
player_stats = PlayerStats(player2)
player_stats.add_match(match1)
player_stats.add_match(match2)

# Obtener y mostrar estadísticas del jugador
print("Player:", player2.get_name())
print("Shots Made:", player_stats.get_shots_made())
print("Shots Attempted:", player_stats.get_shots_attempted())
print("Shooting Percentage:", player_stats.get_shooting_percentage(), "%")

best_spot, best_percentage, worst_spot, worst_percentage = player_stats.get_best_and_worst_spot()
print("Best Spot:", best_spot)
print("Best Percentage:", best_percentage, "%")
print("Worst Spot:", worst_spot)
print("Worst Percentage:", worst_percentage, "%")