from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg":60},
         {"name": "Thunder", "cost": 12, "dmg":80},
         {"name": "Blizzard", "cost": 10, "dmg":60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("======================================")
    player.choose_magic()
    choice = input("Choose action:")
    index = int(choice) - 1


    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)

    running = False
