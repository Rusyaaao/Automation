
from RPG.main import game
import random as ran

monster_hp = ran.randint(1, 50)
monster_attack = ran.randint(1,10 ) 

print("Добро пожаловать, Герой! Ты отправляешься в странствие навстречу приключениям и опасностям. Будь осторожен!")
print("Ваша задача убить 10 чудовищ и не умереть. Да прибудет с тобой сила!")
print(f"У тебя {hp} жизней")

def enter_number():
    number = input("введите 1 или 2:")
    while number != "1" and number != "2":
            print("Ввод некорректен!")
            number = input(" Введи 1 или 2 для своего выбора действия.")
    return number

    def game():
        global hp
        global monster_counter
        global attack

        while monster_counter < 10 and hp > 0:
            barrier = ["Apple", "Sword", "Monster"]
            step = choice(barrier)
            if step == "Apple":
                apple_hp = ran.randint(1, 10)
                hp += apple_hp 
                print(f"Ты нашёл волшебное яблоко! Съедаешь яблоко, ты увеличил здоровье на {apple_hp} теперь у тебя {hp} жизней.")
            if step == "Sword":
                sword_attack = ran.randint(10,50 ) 
                print(f"Ты нашёл меч с силой удара {sword_attack}.")
                print("Что будешь делать: 1-взять меч себе выбросив старый, 2-пройти мимо меча. Введи 1 или 2 для своего выбора действия.")
                plus_sword = enter_numberr()
                if  plus_sword != 1:
                    continue
                atack = sword_attack
            if step == "Monster":
                monster_attack = ran.randint(1, 20)
                monster_hp = ran.randint(1, 30)
                print(f"БОЙ! Вы встретили чудовище c {monster_hp} жизнями и с силой удара {monster_attack}.")
                print("Что будешь делать: 1-атаковать чудовище, 2-убежать, чтобы набраться сил. Введи 1 или 2 для своего выбора действия.")
                print(f"Сейчас твоя сила удара {attack},  количество жизней {hp}\n")  
                print(f"Вы убили: {monster_counter}")

                kol = enter_number()
                if kol == "1":
                    if monster_hp > attack:
                        hp = hp - monster_attack * (hp_monster // attack + 1)
                        monster_counter += 1
                    else:
                        hp = hp - attack_monster
                        monster_counter += 1
            if monster_counter >= 10 and hp > 0:
                print("ПОБЕДА! Все чудовища уничтожены вами!")
            else:
                print("ПОРАЖЕНИЕ")

            while True:
                a = input("Хотите сыграть еще? введите 1")
                if a != "1":
                    print("Спасибо за игру!")
                    exit()
                else:
                     monster_counter = 0
                     hp = ran.randint(10, 100)  
                     attack = ran.randint(10, 100)  

