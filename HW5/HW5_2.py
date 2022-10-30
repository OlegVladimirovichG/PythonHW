import random

print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.'
      ' За один ход можно забрать не более чем 28 конфет')
lolipops = 2021
counter_lolipops_1, counter_lolipops_2 = 0, 0
nums_player_1, nums_player_2 = 0, 0
name_player_1 = input('Введите имя игрока: ')
name_player_2 = 'bot'
first_step = random.randint(0, 1)

if first_step == 0:
    print(f'Первым ходит {name_player_2}!')
    while lolipops > 0:
        nums_player_2 = random.randint(1, 28)
        print(f'{name_player_2} выбрал число {nums_player_2}')

        counter_lolipops_2 += 1
        lolipops -= nums_player_2
        print(f'Осталось {lolipops} конфет')
        if lolipops < 1:
            break
        nums_player_1 = int(input(f'{name_player_1}, ведите число от 1 до 28: '))

        if nums_player_1 < 1 or nums_player_1 > 28:
            while not 0 < nums_player_1 < 29:
                print('Число неверное!!!')
                nums_player_1 = int(input(f'{name_player_1}, ведите число от 1 до 28: '))
        counter_lolipops_1 += 1
        lolipops -= nums_player_1
        print(f'Осталось {lolipops} конфет')
    if counter_lolipops_1 > counter_lolipops_2:
        print(f'Поздравляем победителя! Выиграл {name_player_1}. Число ходов {counter_lolipops_1}')
    else:
        print(f'Поздравляем победителя! Выиграл {name_player_2}. Число ходов {counter_lolipops_2}')
else:
    print(f'Первым ходит {name_player_1}!')
    while lolipops > 0:
        nums_player_1 = int(input(f'{name_player_1}, ведите число от 1 до 28: '))

        if nums_player_1 < 1 or nums_player_1 > 28:
            while not 0 < nums_player_1 < 29:
                print('Число неверное!!!')
                nums_player_1 = int(input(f'{name_player_1}, ведите число от 1 до 28: '))
        counter_lolipops_1 += 1
        lolipops -= nums_player_1
        print(f'Осталось {lolipops} конфет')
        if lolipops < 1:
            break
        nums_player_2 = random.randint(1, 28)
        print(f'{name_player_2} выбрал число {nums_player_2}')
        counter_lolipops_2 += 1
        lolipops -= nums_player_2
        print(f'Осталось {lolipops} конфет')

    if counter_lolipops_1 > counter_lolipops_2:
        print(f'Поздравляем победителя! Выиграл {name_player_1}. Число ходов {counter_lolipops_1}')
    else:
        print(f'Поздравляем победителя! Выиграл {name_player_2}. Число ходов {counter_lolipops_2}')
