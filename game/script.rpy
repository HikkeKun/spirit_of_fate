# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define someone = Character("???")
define Author = Character("Author")
define Spirit = Character("Sprit of Fate")

# The game starts here.

label start:

    scene bg room

    show author hidden

    someone  "Hello Fellow!"

    someone  "Sorry about breacking forth wall, but this should be done."

    show author normal

    Author "Nice to meet you, i'm Author."

    Author "Not asking about you, as i would forget it immediately, sorry."

    Author "I'm the developer of this, so I can tell you something about this project and, or you can talk to Spirit of Fate."

    $ first_time_start_menu = True

    while True:
        menu:
            "Continue with Author." if first_time_start_menu:
                call author_start
            "Talk to Author" if not first_time_start_menu:
                call author_start
            "Talk to Spirit of Fate":
                call spirit_start
            "Main Menu":
                return
        $ first_time_start_menu = False
    return
