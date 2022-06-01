import random

print('Здравейте, приятели!\n\nДобре дошли на "Викторина за Празника на Буквите"!')
print()
print('Честит празник!')
print()
print('Да поиграем! Успех!')
print()

questions = ['Как се нарича азбуката създадена от двамата братя Св. св. Кирил и Методий?',
             'Колко букви съдържа съвременната българска азбука?',
             'Колко са учениците на светите братя Кирил и Методий, които идват в България?',
             'Как се нарича националната ни библиотека намираща се в гр. София?',
             'Управлението на кой български владетел е известно под името "Златният век"']

answered_questions = []
guessed = 0
current_question_counter = 0

for _ in range(len(questions)):
    current_question = random.choice(questions)

    if current_question not in answered_questions:
        answered_questions.append(current_question)
        current_question_counter += 1
        print(current_question)

    else:
        continue

    if current_question == 'Как се нарича азбуката създадена от двамата братя Св. св. Кирил и Методий?':
        print(f'A: Глаголица\nB: Кирилица\nC: Наумица')

        answer = input('отговор:').lower()

        if answer == "a":
            print('Браво, верен отговор!\n')
            guessed += 1
        else:
            print('Грешен отговор!\n')

    elif current_question == 'Колко букви съдържа съвременната българска азбука?':
        print(f'A: 30\nB: 31\nC: 29')

        answer = input('отговор:').lower()

        if answer == "a":
            print('Браво, верен отговор!\n')
            guessed += 1
        else:
            print('Грешен отговор!\n')

    elif current_question == 'Колко са учениците на светите братя Кирил и Методий, които идват в България?':
        print(f'A: 9\nB: 5\nC: 17')

        answer = input('отговор:').lower()

        if answer == "b":
            print('Браво, верен отговор!\n')
            guessed += 1
        else:
            print('Грешен отговор!\n')

    elif current_question == 'Как се нарича националната ни библиотека намираща се в гр. София?':
        print(f'A: Св. Александър Невски\nB: Св. св. Кирил и методий\nC: Св. Софроний Врачански')

        answer = input('отговор:').lower()

        if answer == "b":
            print('Браво, верен отговор!\n')
            guessed += 1
        else:
            print('Грешен отговор!\n')

    elif current_question == 'Управлението на кой български владетел е известно под името "Златният век"':
        print(f'A: Цар Симеон\nB: Цар Борис III\nC: Хан Кубрат')

        answer = input('отговор:').lower()

        if answer == "a":
            print('Браво, верен отговор!\n')
            guessed += 1
        else:
            print('Грешен отговор!\n')

if guessed >= 3:
    print('Познахте 3 от 3 зададени въпроса! Имате добри знания! Похвално!')

else:
    print('Трябва да отделяте повече време за четене! :)')