inport random as R

hp = 0
coins = 0
damage = 0

def printParams():
    print(f"У тебя {hp} жизней, {coins} монет и {damage} урона.")
    
    
def printHP()
    print(f"У тебя {hp} жизней")
    
def printCoins()
    print(f"У тебя {coins} монет")
        
def printDmg()
     print(f"У тебя {damage} урона")


def meetShop():
    global hp
    global coins
    global damage
    
def buy(cost):
    global coins
    if coins >= cost:
        coins-=cost
        printCoins()
        return True
    else:
        print("У тебя маловато денег!")
        return False
    
class Weapon():
    weaponLvl = R.randiant(1,3)
    weaponDmg = R.randiant (1,5) * weaponLvl
    weaponCost = R.randiant(3,10) * weaponLvl
    
class Sword(Weapon):
    def __init__(self, name = 'Меч', damage = 30):
        self.name = name
        self.damage = damage

class Bow(Weapon):
    def __init__(self, name = 'Лук', damage = 20):
        self.name = name
        self.damage = damage  
    
class Spellbook(Weapon):
    def __init__(self, name = 'Книга заклинаний', damage = 25):
        self.name = name
        self.damage = damage  
    
    
    
    
def initGame (initHp,initCoins, initDmg):
    global hp
    global coins
    global damage
    
    hp = initHp
    coins = initCoins
    damage = initDmg
    print("Добро пожаловать, Герой! Ты отправляешься в странствие навстречу приключениям и опасностям. Будь осторожен!")
    print("Ваша задача убить чудовищ и не умереть самому. Да прибудет с тобой сила!")
    printParams()

def loopGame():
    situation = R.randiant(0,1)
    if situation == 0:
        input("Monster")
    else:
        input("Путешествую по миру")
        
initGame (10, 5, 1)

while True:
    loopGame()
    
    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): "). lower() == "да":
            initGame (10, 5, 1)
        else:
            break
        
        
        
    
