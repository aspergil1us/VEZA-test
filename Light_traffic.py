from datetime import date

need = int(input('Потребность: '))                                                # Потребность
need_data = (input('Дата потребности: '))
need_data = date.fromisoformat(need_data)
order_point = int(input('Точка заказа: '))                                        # Точка заказа
stock = int(input('Склад: '))                                                     # Остаток на складе
nzp = int(input('НЗП: '))                                                         # Остаток НЗП
provider_data = (input('Введите дату поставки: '))                                # Дата поставки от поставщика
provider_data = date.fromisoformat(provider_data)                                 
provider_mat = int (input('Введите колличество поставляемого материала: '))       # Колличество материала поставщика
supply = int(input('Срок поставки: '))                                            # Срок поставки
green_zone = 14                                                                   # Устанавливаемое значение зеленой зоны
yellow_zone = 7                                                                   # Устанавливаемое значение желтой зоны
need_order = 0
remainder = 0

if True:
    remainder = stock + nzp
    need = 0
    while True:
        if provider_data >= need_data:
            remainder = remainder + provider_mat
            print (remainder)
            break
        if provider_data < need_data:
            print (remainder)
            break