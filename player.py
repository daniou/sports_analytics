class Player:
    def __init__(self, name, dorsal, position, team):
        self.name = name
        self.dorsal = dorsal
        self.position = position
        self.team = team

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_dorsal(self):
        return self.dorsal

    def set_dorsal(self, new_dorsal):
        self.dorsal = new_dorsal

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def get_team(self):
        return self.team

    def set_team(self, new_team):
        self.team = new_team

