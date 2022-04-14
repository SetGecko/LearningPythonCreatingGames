import random
import time

def displayIntro():
    print('''Вы находитесь в землях, заселёнными драконами.
    Перед собой вы видите две пещеры. 
    В одной из них дружелюбный дракон,
    который готов поделиться с вами своими сокровищами.
    Во второй - жадный и голодный дракон, который мином вас съест.''')
    print()

def chooseCave():
    cave = ''
    while cave !='1' and cave != '2':
        print('В каку пещеру вы войдёте? (нажмите клавишу 1 или 2)')
        cave = input()
    return cave

def checkCave(choosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и ....')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if choosenCave == str(friendlyCave):
        print('... делится с вами сокровищами!')
    else:
        print('Моментально съедает вас!')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу ещё раз? (да или нет)')
    playAgain = input()
