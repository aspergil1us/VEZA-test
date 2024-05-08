from datetime import date

need = int(input('Потребность: '))                                            # Потребность
order_point = int(input('Точка заказа: '))                                    # Точка заказа
stock = int(input('Склад: '))                                                 # Остаток на складе
nzp = int(input('НЗП: '))                                                     # Остаток НЗП
provider = int(input('Поставщик: '))                                          # Заказано у поставщиков
calculation = stock + nzp + provider - need - order_point                     # Расчет значений (Расчет)
remainder = stock + nzp + provider - need                                     # Свободный остаток (Расчет)
need_order = 0
supply = int(input('Срок поставки: '))                                        # Срок поставки
green_zone = 14                                                               # Устанавливаемое значение зеленой зоны
yellow_zone = 7                                                               # Устанавливаемое значение желтой зоны

if remainder <= 0:
    remainder = stock + nzp + provider
    need = 0
    while remainder > 0:
        need = int(input('Потребность по заказу: '))
        remainder = remainder - need
        today = date.today()                                                  # Текущая дата
        date_of_need = input('Дата потребности: ')                            # Ввод даты потребности
        date_of = date.fromisoformat(date_of_need)                            # Преобразуем строку в дату
        date_int = int((date_of - today).days)                                # Разница дней (числом)
        print(remainder)
        point = date_int - supply                                             # Считаем дни минус срок поставки

        if point < 0 and remainder
        if point >= green_zone and remainder > 0:
            print("\033[32m{}".format('Green'))                               # Красим в зелёный
            print(point)
        if point < green_zone and point >= yellow_zone and remainder > 0:
            print("\033[33m{}".format('Yellow'))                              # Красим в жёлтый
            print(point)
        if point <=0 and remainder > 0:                                   
            print("\033[37m{}".format('White'))                               # Красим в белый
            print(point)
        if point > 0 and point <= yellow_zone and remainder > 0:
            print("\33[31m{}".format('Red'))                                  # Красим в красный
            print(point)
    print('Проебали заказ материалов')