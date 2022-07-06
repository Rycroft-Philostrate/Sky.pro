from random import choice
dict_morse = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-",
  " ": "−···−"
}  # словарь кодов Морзе
list_words = ['code', 'bit', 'list', 'soul', 'next', 'little', 'well played']  # список слов для расшифровки
answers = []  # правильность ответов


def morse_encode(word_en):  # перевод слова в код морзе
    word_morse = []  # список букв слова представленного в коде Морзе
    for letter in word_en:
        word_morse.append(dict_morse[letter])
    return ' '.join(word_morse)


def get_word():  # выбор случайного слова
    return choice(list_words)


def print_statistics(answers_result):  # вывод статистики
    return len(answers_result), answers_result.count(True), answers_result.count(False)


print('Сегодня мы потренируемся расшифровывать азбуку Морзе.')
input('Нажмите Enter и начнем ')

for i in range(1, 4):
    word = get_word()
    print(f'Слово {i} — {morse_encode(word)}')
    if input().lower() == word:
        print(f'Верно, {word.capitalize()}!')
        answers.append(True)
    else:
        print(f'Неверно, {word.capitalize()}!')
        answers.append(False)
statistics = print_statistics(answers)
print(f'Всего задачек: {statistics[0]}', f'Отвечено верно: {statistics[1]}', f'Отвечено неверно: {statistics[2]}', sep='\n')
