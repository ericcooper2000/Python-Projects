import random
import time


def print_pause(string):
    print(string)
    time.sleep(2)


def get_valid_choice(prompt, choices):
    while True:
        choice = input(prompt)
        if choice in choices:
            return choice
        else:
            print_pause(f"Please enter one of {choices}")


def weapon_random():
    weapon = ["sword", "axe", "wand"]
    equipped_weapon = []
    equipped_weapon.append(random.choice(weapon))
    return equipped_weapon


def introduction(equipped_weapon):
    print_pause(
        "You are a warrior walking through the "
        "woods aimlessly looking for a way out"
    )
    print_pause("You stumble across something and pick it up")
    weapon_random()
    if "sword" in equipped_weapon:
        print_pause("It is a sword, lucky me!")
    if "axe" in equipped_weapon:
        print_pause("It is a axe, lucky me!")
    if "wand" in equipped_weapon:
        print_pause("It is a wand, lucky me!")
    print_pause("You sheath your weapon and move on.")
    print_pause("You are walking in the woods and the path stops at a sign.")


def choose_path():
    return get_valid_choice(
        """There are two choices....\n
1. Freezing Peaks
2. Valley of Death\n
Choose wisely Warrior...\n""",
        ["1", "2"],
    )


def frozen_path(path, equipped_weapon):
    if "1" in path:
        print_pause(
            "You set for the Freezing Peaks and"
            " brace your self for the cold"
        )
        print_pause("As you walk the peaks you run into a ice bear")
        print_pause("You unsheath your and weapon and prepare for battle")
        if "sword" in equipped_weapon:
            life = 100
            m_life = 100
            while True:
                print_pause("Bear slashes hero and take 20 hit points")
                life -= 20
                attack = get_valid_choice(
                    "choose a move!\n1. Slash Attack!"
                    "\n2. Double thrust!\n ",
                    ["1", "2"],
                )
                if "1" in attack:
                    m_life -= 10
                    print_pause("Slashes Bear")
                if "2" in attack:
                    m_life -= 30
                    print_pause("Double thrust's sword in bears chest!")
                if m_life <= 0:
                    print_pause("Frost Bear has been Slain!")
                    print_pause("You make it out of the "
                                "peaks and found a town")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break
        if "wand" in equipped_weapon:
            life = 100
            m_life = 100
            while True:
                print_pause("Bear slashes hero and take 20 hit points")
                life -= 20
                attack = get_valid_choice(
                    "choose a move!\n1. Water Whip!\n2."
                    " Thunder Beam!\n ", ["1", "2"]
                )
                if "1" in attack:
                    m_life -= 7
                    print_pause("Hits Bear with Water whip!")
                if "2" in attack:
                    m_life -= 40
                    print_pause("Hits Bear with Thunder Beam!")
                if m_life <= 0:
                    print_pause("Frost Bear has been Slain!")
                    print_pause("You make it out of the "
                                "peaks and found a town")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break
        if "axe" in equipped_weapon:
            life = 100
            m_life = 100
            while True:
                print_pause("Bear slashes hero and take 20 hit points")
                life -= 20
                attack = get_valid_choice(
                    "choose a move!\n"
                    "1. Slash Attack!"
                    "\n2. Falling Acorn"
                    " Suplex!\n",
                    ["1", "2"],
                )
                if "1" in attack:
                    m_life -= 1
                    print_pause("Hits Bear with Slash!")
                if "2" in attack:
                    m_life -= 100
                    print_pause("Hits Bear with Suplex")
                if m_life <= 0:
                    print_pause("Frost Bear has been Slain!")
                    print_pause("You make it out of the "
                                "peaks and found a town")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break


def valley_path(path, equipped_weapon):
    if "2" in path:
        print_pause(
            "You set for the Valley of Death, you"
            " brace youself as the shadows grow darker"
        )
        print_pause(
            "As you walk the treacherous "
            "valley you run into a undead skeleton!"
        )
        print_pause("You unsheath your and weapon and prepare for battle")
        if "sword" in equipped_weapon:
            life = 100
            m_life = 100
            while True:
                print_pause("Skeleton bites Warrior in the head 20 hit points")
                life -= 20
                attack = get_valid_choice(
                    "choose a move!\n1. Slash Attack!"
                    "\n2. Double thrust!\n ",
                    ["1", "2"],
                )
                if "1" in attack:
                    m_life -= 10
                    print_pause("Slashes Skeleton")
                if "2" in attack:
                    m_life -= 30
                    print_pause("Double thrust's sword in skeleton neck bone")
                if m_life <= 0:
                    print_pause("Skeleton has been killed!")
                    print_pause(
                        "You make it out of the valley and"
                        " found a oasis with settlers"
                    )
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break
        if "wand" in equipped_weapon:
            life = 100
            m_life = 100
            while True:
                print_pause("Skeleton bites Warrior in the head 20 hit points")
                life -= 20
                attack = get_valid_choice(
                    "choose a move!\n1. Water Whip!\n2."
                    " Thunder Beam!\n ", ["1", "2"]
                )
                if "1" in attack:
                    m_life -= 7
                    print_pause("Hits Skeleton with Water whip!")
                if "2" in attack:
                    m_life -= 40
                    print_pause("Hits Skeleton with Thunder Beam!")
                if m_life <= 0:
                    print_pause("Skeleton has been killed!")
                    print_pause(
                        "You make it out of the valley "
                        "and found a oasis with settlers"
                    )
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break
        if "axe" in equipped_weapon:
            life = 100
            m_life = 100
            while True:
                print_pause("Skeleton bites Warrior in the head 20 hit points")
                life -= 20
                attack = get_valid_choice(
                    "choose a move!\n"
                    "1. Slash Attack!"
                    "\n2. Falling Acorn"
                    " Suplex!\n",
                    ["1", "2"],
                )
                if "1" in attack:
                    m_life -= 1
                    print_pause("Hits Skeleton with Slash!")
                if "2" in attack:
                    m_life -= 100
                    print_pause("Hits Skeleton with Suplex!")
                if m_life <= 0:
                    print_pause("Skeleton has been killed!")
                    print_pause(
                        "You make it out of the valley "
                        "and found a oasis with settlers"
                    )
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break


def replay_option(equipped_weapon):
    while True:
        replay = get_valid_choice(
            "Do you want to play again?" "\n1.Yes\n2.No\n", ["1", "2"]
        )
        if "1" in replay:
            print_pause("Starting Over!")
            equipped_weapon.clear()
            Lost_Warrior()
        elif "2" in replay:
            print_pause("Exiting Game...")
            break


def paths(path, equipped_weapon):
    valley_path(path, equipped_weapon)
    frozen_path(path, equipped_weapon)


def Lost_Warrior():
    equipped_weapon = weapon_random()
    introduction(equipped_weapon)
    path = choose_path()
    paths(path, equipped_weapon)
    replay_option(equipped_weapon)


Lost_Warrior()
