class Match:
    def __init__(self, visitor, local, time, match_type):
        self.visitor = visitor
        self.local = local
        self.time = time
        self.match_type = match_type
        self.shots = []

    def get_visitor(self):
        return self.visitor

    def set_visitor(self, new_visitor):
        self.visitor = new_visitor

    def get_local(self):
        return self.local

    def set_local(self, new_local):
        self.local = new_local

    def get_time(self):
        return self.time

    def set_time(self, new_time):
        self.time = new_time

    def get_match_type(self):
        return self.match_type

    def set_match_type(self, new_match_type):
        self.match_type = new_match_type

    def add_shot(self, shot):
        self.shots.append(shot)

    def get_shots(self):
        return self.shots
