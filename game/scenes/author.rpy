label author_start:

    python:
        if "author_asked_how_he_can_help" not in persistent.__dict__:
            persistent.author_asked_how_he_can_help = False

    while True:
        menu:
            Author "Well, what are you intrested in?"
            "Tell me about this project.":
                Author "Long story short. Mainly, it's a library for using Fate Core rules for conflict resolution between Gamer, his Character and Game world."
                extend "But Fate Core was desined to be played by humans. So I may brought some from myself."

                Author "Anyway, better ask Sprit about this"

            "Who is Spirit of Fate and how he can help me":
                Author "He is some kind of magical creature or so it seems. But I'm no expert here."
                Author "All I know he is fond of Fate Core and know the rules, and how game with them shold be played."

            "How you can help me?":
                $ persistent.author_asked_how_he_can_help = True
                Author "I'm developer, so ask me about how to use Fate Core library."

            "About using library you talked about..." if persistent.author_asked_how_he_can_help:
                call author_about_library

            "Ok, gotcha. Bye":
                return
    return

label author_about_library:

    while True:
       menu:
           "I have other questions":
               return

    return
