label spirit_start:

    python:
        if "spirit_told_about_character_creation" in persistent.__dict__:
            persistent.spirit_told_about_character_creation = False

    $ sprit_menu_continue = True

    while sprit_menu_continue:
        menu:
            Spirit "What are you intrested in?"
            "What are Fate Core rules about?":
                call spirit_about_rules
            "How do I create a character?" if not persistent.spirit_told_about_character_creation:
                $ persistent.spirit_told_about_character_creation = True
                call spirit_about_charater_creation
            "How do I create a character, once again?" if persistent.spirit_told_about_character_creation:
                call spirit_about_charater_creation
            "Ok, let's create character" if persistent.spirit_told_about_character_creation:
                call spirit_create_character
            "I'm done. Bye!":
                $ sprit_menu_continue = False
    return

label spirit_about_rules:
    Spirit "Fate Core is about action, pulp and decision making. It was designed as system for resolving confict between Player, his Character and Game World (represented by Game Master)."
    Spirit "In other words: Player says his Charater doing 'A' thing. GM thinks that this action may fail and/or Character may face some Consequences in case of failure. Will Character succeed? How sever Consequences are? Way to resolve is Fate Core rules."
    Spirit "And here them are..."
    Spirit "Basically all meaningfull things in Fate core world called Aspects."
    Spirit "Is your Character have Turret syndrome? It's his aspect. Are everything is on fire in this room? It's scene aspect. Does your enemy have a Castle? Looks like game aspect. And so on."
    Spirit "Characters consist of High concept - his main Aspect, this Describes what Character ARE, a good High Concept also may bring troubles. Like, Forgetfull Private Detective or Impatient Barbarian."
    return

label spirit_about_charater_creation:
    return

label spirit_create_character:
    Spirit "Let's start creating your character!"

    python:
        character_name = renpy.input("First, tell me his name?")
        character_name = character_name.strip()

        character_concept = renpy.input("Got it, now his High Concept, it's what this character is all about, good concept has also some downsides.")

        character_trouble = renpy.input("And his trouble aspect. What makes his days harder.")

    Spirit "Nice. Let's flash him out a bit. Make two phrases about him. What is he seeking, what antagonising? Maybe something that makes him very special."

    python:
        character_first_aspect = renpy.input("First phrase -> First aspect")

        character_second_aspect = renpy.input("Second phrase -> Second aspect")

    Spirit "Half way. Now to the skill section. Note that skill list may vary in game to game."

    Spirit "Oh noooo. This is not implemeted yet. I'll report to Author about it."

    # TODO: skill creation
    return

    #define gg = FateCharacter(name=character_name, high_concept=character_concept, trouble=character_trouble, first_aspect=character_first_aspect, second_aspect=character_second_aspect)
