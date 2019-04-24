class Meet:
    def __init__(self, name, lost_to, time):
        self.name = name
        self.lost_to = lost_to
        self.time = time
        self.place = len(self.lost_to) + 1
