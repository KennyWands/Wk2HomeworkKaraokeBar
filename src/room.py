class Room:
    def __init__(self, get_name, get_capacity, get_album, get_admission):
        self.name = get_name
        self.capacity = get_capacity
        self.album = get_album
        self.admission = get_admission
        self.guests_in_room = []
        self.num_guests = len(self.guests_in_room)
