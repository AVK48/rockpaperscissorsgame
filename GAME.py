print("The Lost Treasure of Arindor - Simple Text Adventure")
inventory = []
clues = []

def start_game():
    print("You wake up in a small clearing in the forest.")
    print("To your left is a narrow forest path.")
    print("To your right is a stone bridge over a rushing river.")

    choice = input("Do you go 'forest' or 'bridge'? ").lower()
    if choice == "forest":
        forest_path()
    elif choice == "bridge":
        stone_bridge()
    else:
        print("Invalid choice. Try again.")
        start_game()

def forest_path():
    print("\nYou walk deeper into the forest.")
    print("You see a mysterious hut ahead and a hidden trail to the right.")

    choice = input("Do you go to the 'hut' or 'trail'? ").lower()
    if choice == "hut":
        enter_hut()
    elif choice == "trail":
        hidden_trail()
    else:
        print("Invalid choice.")
        forest_path()

def enter_hut():
    print("\nYou enter the hut and meet a wise hermit.")
    answer = input("He asks: 'What has to be broken before you can use it?' ").lower()
    if "egg" in answer:
        print("Correct! The hermit gives you a treasure map.")
        inventory.append("treasure map")
        clues.append("lever step 1")
    else:
        print("Wrong! The hermit laughs and sends you away.")
    stone_bridge()

def hidden_trail():
    print("\nYou follow the hidden trail and encounter a wild animal.")
    if "food" in inventory:
        print("You throw some food to distract it and continue safely.")
        clues.append("lever step 2")
    else:
        print("You have nothing to distract it. You run back.")
    stone_bridge()

def stone_bridge():
    print("\nYou cross the stone bridge.")
    print("You see an ancient temple and a cliffside path.")

    choice = input("Do you go to the 'temple' or 'cliff'? ").lower()
    if choice == "temple":
        enter_temple()
    elif choice == "cliff":
        cliffside_path()
    else:
        print("Invalid choice.")
        stone_bridge()

def enter_temple():
    print("\nYou enter the temple and see a puzzle on the floor.")
    answer = input("Solve this: What is 5 + 7? ")
    if answer == "12":
        print("Correct! You unlock a clue to the treasure cave.")
        clues.append("lever step 3")
    else:
        print("Wrong! The temple remains silent.")
    treasure_cave()

def cliffside_path():
    print("\nYou climb the cliff and reach a watchtower.")
    print("From here you spot the location of the treasure cave.")
    clues.append("lever step 3")
    treasure_cave()

def treasure_cave():
    print("\nYou arrive at the Cave of Arindor.")
    if len(clues) >= 2:
        order = input("Enter the lever order (hint from clues: step 1, step 2, step 3): ")
        if order == "1 2 3":
            print("The cave opens! You found the lost treasure of Arindor! 🎉")
        else:
            print("Wrong order! The cave collapses. Game over.")
    else:
        print("You don't have enough clues. You are lost forever in the wilderness.")

# Start the game
start_game()
