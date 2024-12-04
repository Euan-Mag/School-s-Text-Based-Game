##INCOMPLETE

import random
import time

### @@@ DEV TEST @@@
#Development testing. Used for developer-only things like debugging, etc.
class devTestClass:
    def __init__(self, isDevTestOn):
        self.isDevTestOn = isDevTestOn
    
    def startDTMarkdown(self):
        print("\n##### START OF DEVTEST #####\n")
        time.sleep(2)
    
    def endDTMarkdown(self):
        time.sleep(2)
        print("\n##### END OF DEVTEST #####\n")
        time.sleep(2)
devTest = devTestClass(False)

## @@@ CLASSES @@@
class Character:
    def __init__(self, Name, Health, Defense, DodgeChance):
        self.Name = Name
        self.Health = Health
        self.Defense = Defense
        self.DodgeChance = DodgeChance
        
    class Attack:
        def __init__(self, ActionName, ActionDescription, DamageDealt):
            self.ActionName = ActionName
            self.ActionDesc = ActionDescription
            self.DamageDealt = DamageDealt
    
    def Dodge(self, pluralOrSingle):
        if pluralOrSingle.lower() == "plural":
            print(self.Name, "dodges!")
        else:
            print(self.Name, "dodge!")
        time.sleep(1)

class Ally(Character):
    def __init__(self, Name, Health, Defense, DodgeChance, DeadOrAlive):
        super().__init__(Name, Health, Defense, DodgeChance)
        self.DeadOrAlive = DeadOrAlive

class Room:
    ContainsArray = []
    
    def __init__(self, Name, Description):
        self.Name = Name
        self.Description = Description

### @@@ OBJECTS @@@
### {{{ CHARACTERS }}}
Player = Character("You", 100, 85, 20)
PlayerAttack = Player.Attack("Swing sword", "You slash your old, medieval sword towards the", 17)

Ally = Ally("Chester Bennington", 80, 20, 36, "Alive")
AllyAttack = Ally.Attack("Shoot rifle", "Chester fires his worn-down M1 garand towards the chest of the", 27)

Enemy = Character("Zombie", 135, 85, 5)
EnemyAttack = Enemy.Attack("Swing hatchet", "The zombie hurls its hatchet down onto the shoulder of", 32)

### {{{ ROOMS }}}
Kitchen = Room("Kitchen", "DESCRIPTION: changes later")
Kitchen.ContainsArray = [Ally]
Kitchen.Description = "The kitchen is a ghost of its former self, draped in dust and decay. Faded tiles, once pristine, are cracked and missing in places, revealing the warped wooden floor beneath. Cabinet doors hang askew, their hinges rusted, while cobwebs weave intricate patterns in the corners. Faint sunlight filters through grimy, broken windows, casting eerie shadows across the cluttered countertops. The air carries a faint musty scent, a testament to years of neglect and abandonment."

MainHall = Room("Main Hall", "DESCRIPTION: changes later")
MainHall.ContainsArray = ["NA"]
MainHall.Description = "The main hall of the abandoned mansion is a cavernous space steeped in eerie silence. Dust-laden beams of light filter through shattered, stained-glass windows, casting fractured colors across the cracked marble floor. A grand, sweeping staircase dominates the room, its once-polished banister now dulled and splintered. Cobwebs drape the ornate chandeliers, which hang precariously from the vaulted ceiling. The faint scent of mildew mingles with the stale air, and faded tapestries hang limply on the walls, their stories lost to time. Amid the decay, hints of former grandeur linger—an intricately carved fireplace, tarnished gold accents, and the ghostly echoes of forgotten footsteps."

MasterBedroom = Room("Master Bedroom", "DESCRIPTION: changes later")
MasterBedroom.ContainsArray = ["Key"]
MasterBedroom.Description = "The master bedroom exudes an eerie, forgotten elegance. The once-plush carpet is matted and threadbare, its colors obscured by a layer of dust. The wallpaper peels in long, curling strips, revealing discolored plaster underneath. A tarnished mirror on the dresser reflects the faint glimmer of a shattered chandelier, its broken crystals scattered across the floor. Cobwebs lace the corners, and the air is heavy with the musty scent of decay, whispering stories of a bygone grandeur..."

### FUNCTIONS
def fightMode(ally, enemy, isAllyAlive):
    while True:
        if devTest.isDevTestOn:
            devTest.startDTMarkdown()
            print("ally length:", len(ally))
            print("enemy length:", len(enemy))
            devTest.endDTMarkdown()
        
        ##FIGHT MODE RESULTS
        
        if Player.Health <= 0:
            print(Player.Name, "dies!")
            return "playerDead"
        elif ally.Health <= 0 and isAllyAlive:
            print(ally.Name, "dies!")
            isAllyAlive = False
        elif enemy.Health <= 0:
            print(enemy.Name, "dies!")
            return "enemyDead"
        
        ##DISPLAY ALL CHARACTERS' HEALTH
        print("You have", Player.Health, "HP")
        time.sleep(1)
        
        if isAllyAlive: #checks if the ally is dead
            print(ally.Name, "has", ally.Health, "HP")
            time.sleep(1)
            
            enemyDecidesWhoToAttack = 100 / 2
        else:
            enemyDecidesWhoToAttack = 100
        
        print()
        time.sleep(1)
        
        print(enemy.Name, "has", enemy.Health, "HP")
        time.sleep(1)
            
        print()
        
        ##DECISION MAKING FOR PLAYER
        statementArray = ["What do you do?", " (1) Attack enemy"]
        for i in range(0, len(statementArray)):
            print(statementArray[i])
            time.sleep(1)
    
        userOption = int(input("\nOPTION: "))
    
        if userOption < 1 or userOption > 1:
            print("Looks like that isn't an option.")
            time.sleep(1)
        elif userOption == 1:
            print(PlayerAttack.ActionDesc, enemy.Name)
            time.sleep(1)
            
            chanceOfAttack = random.randint(1, 100)
            
            if chanceOfAttack <= enemy.DodgeChance:
                enemy.Dodge("plural")
            else:
                print(enemy.Name, "takes damage!")
                enemy.Health -= PlayerAttack.DamageDealt
        
        time.sleep(1)
        print()
        
        ##DECISION MAKING FOR ALLY
        if isAllyAlive:
            print(AllyAttack.ActionDesc, enemy.Name)
            time.sleep(1)
                
            chanceOfAttack = random.randint(1, 100)
                
            if chanceOfAttack <= enemy.DodgeChance:
                enemy.Dodge("plural")
            else:
                print(enemy.Name, "takes damage!")
                enemy.Health -= AllyAttack.DamageDealt
            
            time.sleep(1)
            print()
        
        ##DECISION MAKING FOR ENEMY
        enemyDecidesWhoToAttack = 100 / 2
        if random.randint(1, 100) <= enemyDecidesWhoToAttack or (not isAllyAlive): #latter condition checks if the ally is dead or not
            personToAttack = Player
            singleOrPluralForDodge = "single"
        else:
            personToAttack = ally
            singleOrPluralForDodge = "plural"
        
        print(EnemyAttack.ActionDesc, personToAttack.Name)
        time.sleep(1)
        
        chanceOfAttack = random.randint(1, 100)
        if chanceOfAttack <= personToAttack.DodgeChance:
            personToAttack.Dodge(singleOrPluralForDodge)
        else:
            print(personToAttack.Name, "takes damage!")
            personToAttack.Health -= EnemyAttack.DamageDealt
        
        time.sleep(1)
        print()
        
        time.sleep(1)
        print("-----")

### @@@ MAIN @@@ ###

isGameOn = True
isAllyFound = False
isKeyFound = False

print("You wake up to find yourself in a dilapidated hall. " + MainHall.Description + "\n")
roomsDict = {Kitchen.Name: 1, MainHall.Name: 2, MasterBedroom.Name: 3}
rooms = ["index 0", Kitchen, MainHall, MasterBedroom] #"index 0" prevents a logic error (likely an off-by-one error)
roomPlayerIsIn = roomsDict[MainHall.Name]

while isGameOn:
    if Player.Health <= 0: # BAD ENDING -- player dies
        isGameOn = False
        print("Your body lies twisted and broken, skin pale and stretched tightly over decaying muscles that are covering the deep crimson pooling beneath. Maggots crawl through empty eye sockets, where your once-vivid gaze has rotted away to darkness. The stench of decomposition clings to the air as your flesh sloughs off in patches, revealing the bone beneath.")
        break
    
    arrayOfStatements = ["What room do you go to?", " (1) Kitchen", " (2) Main Hall", " (3) Master Bedroom"]
    rangeOfRoomOptions = len(arrayOfStatements)
    for statement in arrayOfStatements:
        print(statement)
        time.sleep(1)
    
    roomToGoTo = int(input("OPTION: "))
    print()
    if (not (roomToGoTo >= 1 and roomToGoTo <= rangeOfRoomOptions)): #if the integer the user enters exceeds the amount of rooms they can go to
        print("Looks like that isn't an option.")
    elif roomToGoTo == roomPlayerIsIn:
        print("You're already in this room.")
    else:
        print("You enter", rooms[roomToGoTo].Name)
        
        
        chanceOfEncounteringEnemy = random.randint(1, 100)
        rangeForEncounteringEnemy = 50
        
        if chanceOfEncounteringEnemy >= rangeForEncounteringEnemy:
            print("A", Enemy.Name, "appears!")
            fightMode(Ally, Enemy, isAllyFound)
        else:
            roomPlayerIsIn = roomsDict[rooms[roomToGoTo].Name]
            print(roomPlayerIsIn)
