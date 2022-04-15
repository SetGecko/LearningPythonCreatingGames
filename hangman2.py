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
    ===''', '''
 +---+
[0   |
/|\  |
/ \  |
    ===''', '''
 +---+
[0]  |
/|\  |
/ \  |
    ===''']

words = {'Цвета':'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
'Фигуры':'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
'Фрукты':'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
'Животные':'муравей бабуин барсук летучая мышь медведь бобр верблюд кошка моллюск кобра пума койот ворона олень собака осел утка орел хорек лиса лягушка коза гусь ястреб лев ящерица лама крот обезьяна лось мышь мул тритон выдра сова панда попугай голубь питон кролик баран крыса ворон носорог лосось тюлень овца скунс ленивец змея паук аист лебедь тигр жаба форель индейка черепаха ласка кит волк вомбат зебра'.split()}

def getRandomWord(wordDict):
    # Эта функция возвращает случайную строку из переданного словаря списков строк, а так же ключ
    # Во первых, случайным образом выбираем ключ из словаря:
    wordKey = random.choice(list(wordDict.keys))

    # Во вторых, случайным образом выбираем слово из списка ключей в словаре:
    wordIndex = random.randint(0, len(wordDict[wordKey] - 1))

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
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

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

def playAgain():
    # эта функция возвращает True если игрок хочет сыграть заново, в противном случае возвращает False.
    print('Хотите сыграть ещё? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Проверяет, выйграл ли игрок.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверяет, превысил ли игрок лимит попыток и проиграл
        if len(missedLetters) == len(hangmanPics) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНеугадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + ' Было загадано слово "' + secretWord + '".')
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
