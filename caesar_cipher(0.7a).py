from sys import exit
from os import name, system

def guide(option):
    if option == "welc":
        print(f'{"=" * 28}ШИФЦ ЦЕЗАРЯ{"=" * 28}')
        print('Шифр Цезаря — это вид шифра подстановки, в котором каждый символ')
        print('в открытом тексте заменяется символом, находящимся на некотором')
        print('постоянном числе позиций левее или правее (сдвиге) от него в')
        print('алфавите.', end='\n\n')
        print('По ходу выполнения программы вам будет предложено выбрать язык(-и),')
        print('буквы которого(-ых) будут читаться программой, ввести текст,')
        print('выбрать режим работы: шифрование или дешифрование, выбрать')
        print('значение сдвига.', end='\n\n')
        print('Учтите, что программа работает только с алфавитом выбранного(-ых)')
        print('языка(-ов). Она никак не взаимодействует с другими символами.')
        print("=" * 67, end='\n\n')

    elif option == "language":
        print(f'{"=" * 31}Справочная информация{"=" * 31}')
        print('Выберите язык(-и), буквы которого(-ых) будут (де)шифроваться. Учтите, ')
        print('что языки выбираются только один раз.')
        print("=" * 83, end='\n\n')

    elif option == "text":
        print(f'{"=" * 31}Справочная информация{"=" * 31}')
        print("Введите текст, который будет в дальнейшем подвержен (де)шифрованию.")
        print("=" * 83, end='\n\n')

    elif option == "mode":
        print(f'{"=" * 33}Справочная информация{"=" * 33}')
        print('Выберите режим работы программы: шифрование или дешифрование', end='\n\n')
        print('Если вы ранее указали зашифрованный по цезарю текст, и вы знаете')
        print('значение сдвига (или хотите его перебрать) в этом шифре, то выбирайте режим')
        print('дешифрования, чтобы получить корректный дешифрованный текст на выходе.', end='\n\n')
        print('Если же вы хотите зашифровать текст, то выбирайте режим шифрования.')
        print("=" * 87, end='\n\n')

    elif option == "final step":
        print(f'{"=" * 33}Справочная информация{"=" * 33}')
        print('Вы находитесь в меню выбора логики работы программы.')
        print('Выберите режим работы программы и значение шага.')
        print('Справа от "Превью текста" будут отображаться первые 30')
        print('символов вашего текста с текущей конфигурацией шифра.')
        print("=" * 87, end='\n\n')

def clear_console():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def only_num_and_minus(num):
    for sym in num:
        if sym not in '-1234567890':
            return False
    return True

def is_valid_digit_answer(answer, x1, x2):
    if answer.isdigit() and x1 != "any":
        if answer[0] == "0" and len(answer) != 1:
            return False
        else:
            return int(answer) in range(x1, x2 + 1)
    elif x1 == "any" and x2 == "any":
        if only_num_and_minus(answer):
            if (answer[0] == "0" and len(answer) != 1) or (answer[0] == "-" and answer[1] == "0"):
                return False
            elif (answer.count("-") == 1 and answer[0] == '-') or (answer.count("-") == 0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def is_valid_string_answer(answer, format='yesno'):
    if answer.isalpha:
        if format == 'yesno':
            return answer in 'lf l da d y yes ye да д нет не н net ne n no ytn yt'.split()
        else:
            return False
    else:
        return False

def switch_bool(bool_object):
    if bool_object:
        return False
    else:
        return True

def get_language(ru, eng):
    while True:
        clear_console()
        guide("language")
        print(f'1) Английский > {"Выбрано" if eng else "Не выбрано"}')
        print(f'2) Русский    > {"Выбрано" if ru else "Не выбрано"}', end='\n\n')
        print('3) Далее', end='\n\n')

        answer = input(">>> ").strip()

        if not is_valid_digit_answer(answer, 1, 3):
            continue

        if answer == "1":
            eng = switch_bool(eng)
        elif answer == "2":
            ru = switch_bool(ru)
        else:
            if ru + eng == 0:
                clear_console()
                print('Выберите хотя бы один язык для корректной работы программы', end='\n\n')
                input('>>> ')
            elif ru + eng == 2:
                clear_console()
                print('Вы можете выбрать только один язык.', end='\n\n')
                input('>>> ')
            else:
                return ru, eng

def is_valid_text(text):
    eng_upper = [chr(c) for c in range(65, 91)]
    eng_lower = [chr(c) for c in range(97, 123)]
    ru_upper = [chr(c) for c in range(1040, 1072)]
    ru_lower = [chr(c) for c in range(1072, 1104)]
    ru_letters, eng_letters = ru_upper + ru_lower, eng_upper + eng_lower

    ru_here = False
    eng_here = False

    for c in text:
        if c in ru_letters:
            ru_here = True
            break
    else:
        ru_here = False
    
    for c in text:
        if c in eng_letters:
            eng_here = True
            break
    else:
        eng_here = False
    return ru_here, eng_here

def get_user_text(ru, eng):
    while True:
        clear_console()
        guide("text")
        print(f"Выбранн{'ые' if ru and eng else 'ый'} язык{'и' if ru and eng else ''}:")
        print(f'{"Русский" if ru and not eng else "Английский" if eng and not ru else "Русский, Английский"}', end='\n\n')
        text = input("ВАШ ТЕКСТ >>> ").strip()

        ru_here, eng_here = is_valid_text(text)

        if not ru_here and not eng_here and ru and eng:
            clear_console()
            print("В тексте должны содержаться буквы хотя бы из одного алфавита выбранных вами языков.", end='\n\n')
            input('>>> ')
            continue
        elif (ru and not eng and not ru_here) or (eng and not ru and not eng_here):
            clear_console()
            print("В тексте должны содержаться буквы из алфавита выбранного вами языка.", end='\n\n')
            input('>>> ')
            continue
        elif ((ru_here and not eng_here) or (eng_here and not ru_here)) and ru and eng:
            while True:
                clear_console()
                print(f'{"=" * 34}Справочная информация{"=" * 34}')
                print(f"В тексте не содержиться букв из {'английского' if not eng_here else 'русского'} алфавита - одного из выбранных вами.")
                print('Если вы хотите соответственно отредактировать ваш текст, то заранее скопируйте его ниже:')
                print("=" * 89, end='\n\n')
                print(f"ИСХОДНЫЙ ТЕКСТ >>> {text}", end='\n\n')
                answer = input("Вы хотите продолжить? (д = да; н = нет): ").strip().lower()

                if not is_valid_string_answer(answer):
                    continue

                if answer in 'lf l da d y yes ye да д'.split():
                    return text
                else:
                    break
        else:
            return text

def processed_text(mode, rotate, text, language):
    eng_upper = [chr(c) for c in range(65, 91)]
    eng_lower = [chr(c) for c in range(97, 123)]
    ru_upper = [chr(c) for c in range(1040, 1072)]
    ru_lower = [chr(c) for c in range(1072, 1104)]
    new_text = ''

    if language == "ru":
        for sym in text:
            if sym in ru_lower:
                new_text += ru_lower[(ru_lower.index(sym) + rotate) % len(ru_lower) if mode else (ru_lower.index(sym) - rotate) % len(ru_lower)]
            elif sym in ru_upper:
                new_text += ru_upper[(ru_upper.index(sym) + rotate) % len(ru_lower) if mode else (ru_upper.index(sym) - rotate) % len(ru_lower)]
            else:
                new_text += sym
    elif language == "eng":
        for sym in text:
            if sym in eng_lower:
                new_text += eng_lower[(eng_lower.index(sym) + rotate) % len(eng_lower) if mode else (eng_lower.index(sym) - rotate) % len(eng_lower)]
            elif sym in eng_upper:
                new_text += eng_upper[(eng_upper.index(sym) + rotate) % len(eng_lower) if mode else (eng_upper.index(sym) - rotate) % len(eng_lower)]
            else:
                new_text += sym

    return new_text

def get_rotate_value():
    while True:
        clear_console()
        print('Введите значение шага (ключ).', end='\n\n')
        change_rotate = input('>>> ')

        if not is_valid_digit_answer(change_rotate, 'any', 'any'):
            continue

        return change_rotate

def final_process(text, mode, rotate, ru_include):

    while True:
        clear_console()
        guide('final step')

        print(f'1) Режим работы: {"Шифрование" if mode else "Дешифрование"}')
        print(f'2) Значение шага (ключ): {rotate}', end='\n\n')
        print(f'Превью текста: {processed_text(mode, int(rotate), text, "ru" if ru_include else "eng")[:31]}', end='\n\n')
        print(f"3) {'Зашифровать' if mode else 'Дешифровать'} текст", end='\n\n')

        answer = input('>>> ').strip()

        if not is_valid_digit_answer(answer, 1, 3):
            continue

        if answer == "1":
            mode = switch_bool(mode)
        elif answer == "2":
            rotate = get_rotate_value()
        else:
            clear_console()
            return processed_text(mode, int(rotate), text, "ru" if ru_include else "eng")

eng_upper = [chr(c) for c in range(65, 91)]
eng_lower = [chr(c) for c in range(97, 123)]
ru_upper = [chr(c) for c in range(1040, 1072)]
ru_lower = [chr(c) for c in range(1072, 1104)]

while True:
    mode = True  # True == программа в режиме шифрования, False == программа в режиме дешифрования
    ru_include, eng_include = False, False
    rotate = 0
    rotate_direction = True  # True == сдвиг идет вправо; False == сдвиг идет влево.
    text = ''

    clear_console()
    guide('welc')
    input(">>> ")

    ru_include, eng_include = get_language(ru_include, eng_include)

    text = get_user_text(ru_include, eng_include)

    print(final_process(text, mode, rotate, ru_include))
    print()
    input(">>> ")

    while True:
        clear_console()
        print('Хотите еще раз воспользовать программой? (д = да; н = нет)')
        answer = input('>>> ').strip().lower()

        if not is_valid_string_answer(answer):
            continue

        if answer in 'lf l da d y yes ye да д'.split():
            break
        else:
            clear_console()
            exit()