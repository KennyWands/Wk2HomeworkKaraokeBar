# from src.bar import Bar
from src.room import Room
from src.album import Album
from src.guest import Guest

album1 = Album(
    "Appetite for Destruction",
    "Guns 'n' Roses",
    {1: "Welcome to the Jungle", 2: "Paradise City", 3: "Mr Brownstone"},
)

album2 = Album(
    "Use your Illusion II",
    "Guns 'n' Roses",
    {
        1: "Civil War",
        2: "Yesterdays",
        3: "Get In The Ring",
    },
)

album3 = Album(
    "Chinese Democracy",
    "Guns 'n' Roses",
    {
        1: "Chinese Democracy",
        2: "Better",
        3: "Riad n' The Bedouins",
    },
)

album4 = Album(
    "Something with spice in the title",
    "Spice Girls",
    {
        1: "Don't Know",
        2: "Don't Care",
        3: "Another One",
    },
)

room_list = [
    Room("Early G'n'R", 1, album1, 1),
    Room("Late G'n'R", 2, album2, 1),
    Room("That one Axl did on his own", 3, album3, 1),
    Room("Spice Girls", 10, album4, 1),
]

guest_list = [
    Guest("Slash", 100, "Paradise City"),
    Guest("Duff", 50, "Get In The Ring"),
    Guest("Axl", 10, "Better"),
    Guest("Posh", 5, "Don't Care"),
]
