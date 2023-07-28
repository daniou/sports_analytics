class Spot:
    def __init__(self, name, mesh):
        self.name = name
        self.mesh = mesh

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_mesh(self):
        return self.mesh

    def set_mesh(self, new_mesh):
        self.mesh = new_mesh



