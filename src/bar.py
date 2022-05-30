class Bar:
    def __init__(self, get_name, get_rooms, get_till):
        self.name = get_name
        self.rooms = get_rooms
        self.till = get_till

    def welcome_msg(self):
        print(f"Welcome to {self.name} which room would you like to join? ")
        self.i = 1
        for room in self.rooms:
            print(f"{self.i}: {room.name}")
            self.i += 1

        return "finished"

    def check_guest_cash(self, guest, room_to_join):
        if guest.cash >= room_to_join.admission:
            return True
        return False

    def check_room_cap(self, room_to_join):
        if room_to_join.capacity > room_to_join.num_guests:
            return True
        return False

    def add_guest_to_room(self, guest, room_to_join):
        room_to_join.guests_in_room.append(guest)

    def take_cash(self, guest, room_to_join):
        guest.cash -= room_to_join.admission

    def assign_room(self, guest):

        for room in self.rooms:

            for song in room.album.track_list:

                if room.album.track_list[song] == guest.song:
                    if (
                        self.check_room_cap(room) == True
                        and self.check_guest_cash(guest, room) == True
                    ):
                        self.add_guest_to_room(guest, room)
                        self.take_cash(guest, room)

                        return room.name
                    elif (
                        self.check_room_cap(room) == False
                        or self.check_guest_cash(guest, room) == False
                    ):
                        print(
                            f"Sorry {guest.name} that room isn't for you, how about some Spice Girls"
                        )
                        self.add_guest_to_room(guest, self.rooms[3])
                        self.take_cash(guest, self.rooms[3])

                        return self.rooms[3].name

        return "You have horrible taste in music, get out."
