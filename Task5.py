income = float(input('Введите сумму дохода в руб.: '))
cost = float(input('Введите сумму расхода в руб.: '))


if cost > income:
    print('Увы, у вас отрицательный финансовый результат - убыток')

else:
    profit = income - cost
    efficiency = round(profit / income * 100, 2)
    print(f'Поздравляем! У вас положительный финансовый результат, сумма прибыли составила {profit} руб., рентабельность бизнеса {efficiency}%')
    num_staff = int(input('Введите количество сотрудников фирмы: '))
    print(f'Сумма прибыли на 1 сотрудника составила {profit / num_staff} руб.')


