def adventure_game():
    print("WELCOME TO THE CHOICE!")
    print("TYPE A LETTER AND CHOOSE:")
    print("========================================================")
    print("LEVEL 1: The Fork in the Path.")
    print("========================================================")
    print("You find yourself standing at the edge of a dense forest, its ancient trees looming ominously overhead.\nThe air is thick with the scent of moss and earth, and the only sound is the distant hoot of an owl.\nBefore you lies a fork in the path, with two trails disappearing into the shadows of the trees.")
    print()
    #Choice 1
    print("You stand before a fork in the forest path:\nA): Through a grove of oak trees.\nB): Deeper into the heart of the forest.\nC): Along a narrow, vine-covered trail.Back: Retrace your steps.")
    
    l1_choices = input("TYPE YOUR CHOICE: ")
    if l1_choices.upper == ("A"):
        print("You reach a crossroads!")
    elif l1_choices == ("B"):
        print()


adventure_game()