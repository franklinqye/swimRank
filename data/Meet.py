"""
Class containing information about who a specific swimmer lost
to in a specific meet. An array of Meet objects is used
as the value in the create_dictionary script.
"""
class Meet:
    """
    NAME is name of the meet.
    LOST_TO is an array of opponents that a specific
    swimmer lost to at this meet.
    TIME is their 100m time at this meet.
    PLACE is their overall ranking at this meet, with 1
    being the fastest.
    """
    def __init__(self, name, lost_to, time):
        self.name = name
        self.lost_to = lost_to
        self.time = time
        self.place = len(self.lost_to) + 1
