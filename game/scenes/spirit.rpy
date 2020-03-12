label spirit_start:

    python:
        if "spirit_told_about_character_creation" not in persistent.__dict__:
            persistent.spirit_told_about_character_creation = False

    while True:
        menu:
            Spirit "What are you intrested in?"
            "I have questions about Fate Core rules.":
                call spirit_about_rules
            "How do I create a character?" if not persistent.spirit_told_about_character_creation:
                $ persistent.spirit_told_about_character_creation = True
                call spirit_about_charater_creation
            "How do I create a character, once again?" if persistent.spirit_told_about_character_creation:
                call spirit_about_charater_creation
            "Ok, let's create character" if persistent.spirit_told_about_character_creation:
                call spirit_create_character
            "I'm done. Bye!":
                return
    return

label spirit_about_rules:

    while True:
        menu:
            Spirit "What exactly are you intrested in Fate Core rules?"
            "What is this thing and what is it all about?":
                call spirit_about_rules_general
            "A short introduction please.":
                call spirit_about_rules_intro
            "I have other questions.":
                return
    return

label spirit_about_rules_general:
    Spirit "Fate Core is about action, pulp and decision making."
    extend " It was designed as system for resolving confict between Player, his Character and Game World (represented by Game Master)."

    Spirit "In other words:"
    extend "\nPlayer cries: 'I'm doing this thing!'."
    extend "\nGM replies that this actions may fail and/or Character may face some Consequences in case of failure."
    extend " Will Character succeed? How harsh is outcome?"

    Spirit "The way to resolve this is Fate Core rules."

    Spirit "However we are in this game. So things are not that awesome, everything is pre-defined..."

    "Looks like spirit sighs"

    return

label spirit_about_rules_intro:
    Spirit "First things first. It's is proactive game. It should be however."
    extend " This means you define what you are doing. Find adventures and glorously overcome them."

    Spirit "Aspects."
    extend "\nBasically all meaningfull things in Fate Core system are called Aspects."

    Spirit "Is your Character have Turret syndrome? This is his aspect."
    extend "\nAre everything on fire in this room? It's scene aspect."
    extend "\nDoes your enemy have a Castle? Looks like game aspect. And so on."

    Spirit "When you try to do something it's eigther of four variants."
    extend "\nCreating an Advantage."
    extend " Overcomming."
    extend "\nAttacking someone."
    extend " And defending."

    Spirit "When you do something mentioned before and things may go south."
    extend " You roll four Fate dice. Fate die, 'DF', is regular 6-sided dice, but instead of 1 through 6 there is '+', noting and '-'."
    extend " After roll sum them up counting '+' as '+1', nothing as '0', and '-' as '-1'"

    Spirit "Oh, wait, we are in game. So..."
    extend " It means that this is done for you. No dice throwing. Sorry."
    extend "\nBut I'll ask Author to print them."

    Spirit "Coming back to what happens."
    extend " You get some number from dice. Something between -4 and 4. Mostly -2 from my experience."

    python:
        if "skills_explained" not in persistent.__dict__:
            persistent.skills_explained = False

    if persistent.skills_explained:
        extend " Add skill value to it. Oh, skills... I'll explain them later."
    else:
        extend " Add skill value to it."


    Spirit "Characters consist of bunch of Aspects and the first is High Concept."
    extend "\nIt should briefly but vastly describe Character."
    extend "\nA good High Concept also brings troubles. Like, Forgetfull Private Detective or Peacefull Orc Barbarian. "

    Spirit "Next is Trouble Aspect."
    extend " This what complicates Character life."
    extend " Mega-evil-lord-of-dark-arts persues him?"
    extend " Family man."
    extend " The bottle calls me. "
    extend "\nThey are all fine. "

    Spirit "Next is three other Aspects."
    extend " What connects him with other Characters and the World."


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
