time = int(input('Введите время в секундах: '))
hour = time // 3600
minute = (time // 60) - (hour * 60)
second = time % 60
print(f'Это составляет:{hour:02}:{minute:02}:{second:02}')