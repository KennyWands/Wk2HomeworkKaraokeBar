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
    Room("Early G'n'R", 1, album1, 5),
    Room("Late G'n'R", 5, album2, 4),
    Room("That one Axl did on his own", 0, album3, 1),
    Room("Spice Girls", 10, album4, 1),
]

guest_list = [
    Guest("Slash", 100, "Paradise City"),
    Guest("Gibby", 50, "Welcome to the Jungle"),
    Guest("Axl", 10, "Better"),
    Guest("Posh", 2, "Don't Care"),
    Guest("Phil Colins", 0, "Any thing by Phil Colins"),
]
