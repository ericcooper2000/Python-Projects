import random
import time


def print_pause(string):
    print(string)
    time.sleep(2)


def weapon_random():
    weapon = ["sword", "axe", "wand"]
    equiped_weapon = []
    equiped_weapon.append(random.choice(weapon))
    return equiped_weapon


def introduction(equiped_weapon):
    print_pause("You are a warrior walking through the "
                "woods aimlessly looking for a way out")
    print_pause("You stumble across something and pick it up")
    weapon_random()
    if "sword" in equiped_weapon:
        print_pause("It is a sword, lucky me!")
    if "axe" in equiped_weapon:
        print_pause("It is a axe, lucky me!")
    if "wand" in equiped_weapon:
        print_pause("It is a wand, lucky me!")
    print_pause("You sheath your weapon and move on.")


def choose_path():
    print_pause("You are walking in the woods and the path stops at a sign.")
    while True:

        path = input("""There are two choices....\n
1. Freezing Peaks
2. Valley of Death\n
Choose wisely Warrior...\n""")
        if path == '1' or path == '2':
            return path

        else:
            print_pause("This is not a path, choose again.")


def frozen_path(path, equiped_weapon):
    if '1' in path:
        print_pause("You set for the Freezing Peaks and"
                    " brace your self for the cold")
        print_pause("As you walk the peaks you run into a ice bear")
        print_pause("You unsheath your and weapon and prepare for battle")
        if "sword" in equiped_weapon:
            life = 100
            M_Life = 100
            while True:
                print_pause("Bear slashes hero and take 20 hit points")
                life -= 20
                attack = input("""Choose a move!
1. Slash Attack!
2. Double thrust!\n """)
                if '1' in attack:
                    M_Life -= 10
                    print_pause("Slashes Bear")
                if '2' in attack:
                    M_Life -= 30
                    print_pause("Double thrust's sword in bears chest!")
                if int(attack) > 2 or int(attack) < 0:
                    print_pause("Forfit Attack due to wrong "
                                "input fight with 1 or 2")
                if M_Life <= 0:
                    print_pause("Frost Bear has been Slain!")
                    print_pause("You make it out of the "
                                "peaks and found a town")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break
        if 'wand' in equiped_weapon:
            life = 100
            M_Life = 100
            while True:
                print_pause("Bear slashes hero and take 20 hit points")
                life -= 20
                attack = input("""Choose a move!
1. Water Whip!
2. Thunder Beam!\n """)
                if '1' in attack:
                    M_Life -= 7
                    print_pause("Hits Bear with Water whip!")
                if '2' in attack:
                    M_Life -= 40
                    print_pause("Hits Bear with Thunder Beam!")
                if int(attack) > 2 or int(attack) < 0:
                    print_pause("Forfit Attack due to wrong"
                                " input fight with 1 or 2")
                if M_Life <= 0:
                    print_pause("Frost Bear has been Slain!")
                    print_pause("You make it out of the "
                                "peaks and found a town")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break
        if 'axe' in equiped_weapon:
            life = 100
            M_Life = 100
            while True:
                print_pause("Bear slashes hero and take 20 hit points")
                life -= 20
                attack = input("""Choose a move!
1. Tree Trunk Slash!
2. Falling Acorn Suplex!\n """)
                if '1' in attack:
                    M_Life -= 1
                    print_pause("Hits Bear with Slash!")
                if '2' in attack:
                    M_Life -= 100
                    print_pause("Hits Bear with Suplex")
                if int(attack) > 2 or int(attack) < 0:
                    print_pause("Forfit Attack due to wrong "
                                "input fight with 1 or 2")
                if M_Life <= 0:
                    print_pause("Frost Bear has been Slain!")
                    print_pause("You make it out of the "
                                "peaks and found a town")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break


def valley_path(path, equiped_weapon):
    if '2' in path:
        print_pause("You set for the Valley of Death, you"
                    " brace youself as the shadows grow darker")
        print_pause("As you walk the treacherous "
                    "valley you run into a undead skeleton!")
        print_pause("You unsheath your and weapon and prepare for battle")
        if "sword" in equiped_weapon:
            life = 100
            M_Life = 100
            while True:
                print_pause("Skeleton bites Warrior in the head 20 hit points")
                life -= 20
                attack = input("""Choose a move!
1. Slash Attack!
2. Double thrust!\n """)
                if '1' in attack:
                    M_Life -= 10
                    print_pause("Slashes Skeleton")
                if '2' in attack:
                    M_Life -= 30
                    print_pause("Double thrust's sword in skeleton neck bone")
                if int(attack) > 2 or int(attack) < 0:
                    print_pause("Forfit Attack due to wrong "
                                "input fight with 1 or 2")
                if M_Life <= 0:
                    print_pause("Skeleton has been killed!")
                    print_pause("You make it out of the valley and"
                                " found a oasis with settlers")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break
        if 'wand' in equiped_weapon:
            life = 100
            M_Life = 100
            while True:
                print_pause("Skeleton bites Warrior in the head 20 hit points")
                life -= 20
                attack = input("""Choose a move!
1. Water Whip!
2. Thunder Beam!\n """)
                if '1' in attack:
                    M_Life -= 7
                    print_pause("Hits Skeleton with Water whip!")
                if '2' in attack:
                    M_Life -= 40
                    print_pause("Hits Skeleton with Thunder Beam!")
                if int(attack) > 2 or int(attack) < 0:
                    print_pause("Forfit Attack due to wrong "
                                "input fight with 1 or 2")
                if M_Life <= 0:
                    print_pause("Skeleton has been killed!")
                    print_pause("You make it out of the valley "
                                "and found a oasis with settlers")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break
        if 'axe' in equiped_weapon:
            life = 100
            M_Life = 100
            while True:
                print_pause("Skeleton bites Warrior in the head 20 hit points")
                life -= 20
                attack = input("""Choose a move!
1. Tree Trunk Slash!
2. Falling Acorn Suplex!\n """)
                if '1' in attack:
                    M_Life -= 1
                    print_pause("Hits Skeleton with Slash!")
                if '2' in attack:
                    M_Life -= 100
                    print_pause("Hits Skeleton with Suplex!")
                if int(attack) > 2 or int(attack) < 0:
                    print_pause("Forfit Attack due to wrong "
                                "input fight with 1 or 2")
                if M_Life <= 0:
                    print_pause("Skeleton has been killed!")
                    print_pause("You make it out of the valley "
                                "and found a oasis with settlers")
                    print_pause("You Win!")
                    break
                if life <= 0:
                    print_pause("Warrior has died, game over.")
                    break


def replay_option(equiped_weapon):
    replay = input(""" Do you want to play again?
1. Yes
2. No\n""")
    if "1" in replay:
        print_pause("Starting Over!")
        equiped_weapon.clear()
        Lost_Warrior()
    elif '2' in replay:
        print_pause("Exiting Game...")
    else:
        print_pause("Did not understand you answer")
        replay_option()


def paths(path, equiped_weapon):
    valley_path(path, equiped_weapon)
    frozen_path(path, equiped_weapon)


def Lost_Warrior():
    equiped_weapon = weapon_random()
    introduction(equiped_weapon)
    path = choose_path()
    paths(path, equiped_weapon)
    replay_option(equiped_weapon)


Lost_Warrior()
