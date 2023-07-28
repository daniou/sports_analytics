from match_stats import MatchStats
from player import Player
from match import Match
from spot import Spot
from shot import Shot
from team import Team
from time_utils import random_datetime


def initialize():
    # Crear jugadores
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
    match = Match(team1, team2, "August 5, 2023", "La Liga")

    # Registrar tiros
    shot1 = Shot(spot1, random_datetime(), True, player1)
    shot2 = Shot(spot2, random_datetime(), False, player2)

    # Agregar tiros al partido
    match.add_shot(shot1)
    match.add_shot(shot2)
    return match


def main():
    match = initialize()
    match_stats = MatchStats(match)
    # Obtener el resumen de estadísticas del partido
    overview = match_stats.overview()

    # Mostrar la información relevante del partido por cada jugador
    for player_stat in overview:
        print(player_stat)

if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()