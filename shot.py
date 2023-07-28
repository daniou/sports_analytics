from player import Player


class Shot:
    def __init__(self, spot, time, made, player, is_free_throw=False):
        self.spot = spot
        self.time = time
        self.was_made = made
        self.was_free_throw = is_free_throw
        self.player = player

    def get_spot(self):
        return self.spot

    def set_spot(self, new_spot):
        self.spot = new_spot

    def get_time(self):
        return self.time

    def set_time(self, new_time):
        self.time = new_time

    def is_made(self):
        return self.was_made

    def set_made(self, made_status):
        self.was_made = made_status

    def get_player(self):
        return self.player

    def set_player(self, new_player):
        self.player = new_player

