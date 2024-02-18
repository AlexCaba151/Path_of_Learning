'''Project: Clever Stories
Overview
Mad Libs are a type of funny story, where a person is asked for words without knowing their context. The words are then placed into a story in a pre-determined format, often resulting in funny statements.

For example, consider prompts for:

-Plural noun

-Verb

-Adjective

-Noun

And a story, such as:

When it comes to [plural-noun], you would never want to [verb], especially if you encountered a [adjective] [noun].

A person, may respond to the prompts with the following:

Plural noun: ducks

Verb: jump

Adjective: cold

Noun: taco

Then the story would read:

When it comes to ducks, you would never want to jump, especially if you encountered a cold taco.
Instructions
For this assignment, you will implement a program that asks the user for a series of words and then displays the story with the user's words inserted into the appropriate places.

The program should begin by asking the user for each of the words. It should then, fill those words into the appropriate places in the story.

To begin, please use the following story:

The other day, I was really in trouble. It all started when I saw a very
[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
I could think to do was to [verb] over and over. Miraculously,
that caused it to stop, but not before it tried to [verb]
right in front of my family.

Make sure to match the punctuation and spacing of the original story exactly (for example, you should not put your words on their own line, they should fit naturally into the story).

Also, make it so that the "exclamation" word is automatically capitalized, because it starts a new sentence.
'''
def clever_stories():
    print("Welcome to Clever stories program, write words and make an story!")
    print("\nPlease enter the following: ")
    print()
    
    #Words to create the story
    adjective= input("Abjective: ")
    animal =input("Animal: ")
    verb_1 = input("Verb: ")
    exclamation =input("Exclamation: ")
    verb_2 =input("Verb: ")
    verb_3 =input("Another verb: ")
    
    
    #Output prints
    print("\n YOUR STORY IS: ")
    print("-------------------------------------------------------------------------------------")
    
    print(f'The other day, I was really in trouble. It all started when I saw a very {adjective.upper()} {animal.upper()} {verb_1.upper()} down the hallway.\n"{exclamation.upper()}!" I yelled. But all I could think to do was to {verb_2.upper()} over and over. Miraculously,that caused\nit to stop, but not before it tried to {verb_3.upper()} right in front of my family.')
    
    print("-------------------------------------------------------------------------------------")

clever_stories()