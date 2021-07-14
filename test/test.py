
    global hp
    global monster_counter
    global attack
    #monsters = ["Alex", "Antonio", "Kir", "Adel", "Aisylu"]
    monster_hp = ran.randint(1, 50)
    monster_attack = ran.randint(1,10 ) * 2
    monster = ran.choice(monsters)

    print(f"БОЙ! Вы встретили чудовище c {monster_hp} жизнями и с силой удара {attack}.")
    
    while monster_counter < 10 and hp > 0:
        barrier = ["apple", "sword", "monster1", "monster2", "monster3", "monster4","monster5"]

       """ choice = input("Что будешь делать: 1-атаковать чудовище, 2-убежать, чтобы набраться сил. Введи 1 или 2 для своего выбора действия.")
        if choice == "1":
            while   True:
                monster_hp -= attack
                if monster_hp <=0:
                    print("У чудовища осталось - 0 жизней. Тебе удалось победить чудовище!")
                    hp = hp - monster_attack
                    monster_counter += 1
                    break
                #elif monster_hp > 0:
                 #   hp -= monster_attack
                  #  print(f"Чудовище атаковало тебя! У тебя осталось {hp} жизней.")
                print(f"Ты атаковал чудовище и у него осталось {monster_hp} жизней.")
                hp = hp - monster_attack

                if hp <= 0:
                    print("ПОРАЖЕНИЕ! Вы умерли! Игра окончена.")
                    
        elif choice == "2":
            print("Ты бежишь с поля боя!")
        else:
            print("Ввод некорректен! Введи 1 или 2 для своего выбора действия.")
        
def find_apple():
    global hp
    apple_hp = ran.randint(1, 10)
    hp += apple_hp 
    print(f"Ты нашёл волшебное яблоко! Съедаешь яблоко, ты увеличил здоровье на {apple_hp} теперь у тебя {hp} жизней.")

def find_sword():
    global hp
    global monster_counter
    global attack
    swords = ["Мститель", "Экскалибур", "Грам"]
    sword_attack = ran.randint(1,10 ) 
    sword = ran.choice(swords)
    print(f"Ты нашёл меч с силой удара {sword_attack}.")
    choice = input("Что будешь делать: 1-взять меч себе выбросив старый, 2-пройти мимо меча. Введи 1 или 2 для своего выбора действия.")
    if choice == "1":
            attack = sword_attack
            print(f"Ты подобрал новый меч, твоя атака составляет {attack}.")
    elif choice == "2":
            print("Ты проходишь мимо меча!")
       # else:
       #     print("Ввод некорректен! Введи 1 или 2 для своего выбора действия.")

def game():
    global hp
    global monster_counter
    global attack
    situation = ran.randint (0,10)
    if situation == 0:
        #бой!
        find_monster()
    elif situation == 1:
        #яблочко
        find_apple()
    else situation == 2:
        #меч
        find_sword()
  """

while True:
    game()