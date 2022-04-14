import random
hangmanPics = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
0   |
    |
    |
   ===''', '''
+---+
0   |
|   |
    |
   ===''', '''
 +---+
 0   |
/|   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''']

words = 'муравей бабуин барсук летучая мышь медведь бобр верблюд кошка моллюск ' \
        'кобра пума койот ворона олень собака осел утка орел хорек лиса лягушка коза ' \
        'гусь ястреб лев ящерица лама крот обезьяна лось мышь мул тритон выдра сова ' \
        'панда попугай голубь питон кролик баран крыса ворон носорог лосось тюлень овца ' \
        'скунс ленивец змея паук аист лебедь тигр жаба форель индейка черепаха ласка кит волк вомбат зебра'.split()

def getRandomWord(wordList):
    # эта функция возвращает случайную строку из переданного списка.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangmanPics[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord + blanks[i+1:]

    for letter in blanks: # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Возвращает букву, введённую игроком. Эта функция проверяет, что игрок ввёл только одно букву и ничего больше.
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

