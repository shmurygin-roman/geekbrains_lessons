# Урок 8. Задание 4
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Урок 8. Задание 5
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# Урок 8. Задание 6
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка:
# постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class OfficeEquipment:
    def __init__(self, type_equipment, firm, model):
        """type_equipment - вид оборудования
        firm - производитель
        model - модель
        """
        self.type_equipment = type_equipment
        self.firm = firm
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, firm, model, type_printer, type_equipment='printer'):
        """type_printer - тип принтера: 1 - лазерный, 0 - струйный"""
        super().__init__(type_equipment, firm, model)
        self.type_printer = type_printer


class Scanner(OfficeEquipment):
    def __init__(self, firm, model, image_method, type_equipment='scanner'):
        """image_method - способ формирования изображения: 1 - линейный, 0 - матричный"""
        self.image_method = image_method
        super().__init__(type_equipment, firm, model)


class Copier(OfficeEquipment):
    def __init__(self, firm, model, copy_speed, type_equipment='copier'):
        """copy_speed - скорость копирования"""
        self.copy_speed = copy_speed
        super().__init__(type_equipment, firm, model)


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:
    def __init__(self):
        self.store = {'printer': [], 'scanner': [], 'copier': []}
        self.log = []

    def in_store(self, type_id, firm, model, qty, feature):
        """type_id - код вида оборудования: 1 - printer, 2 - scanner, 3 - copier
        qty - количество оборудования
        """
        if type_id == 1:
            a = Printer(firm, model, feature)
        elif type_id == 2:
            a = Scanner(firm, model, feature)
        elif type_id == 3:
            a = Copier(firm, model, feature)

        list_equipment = self.store.get(a.type_equipment)
        new = True
        try:
            for i in list_equipment:
                if i.get('firm') == a.firm and i.get('model') == a.model:
                    new = False
                    i.update({'qty': i.get('qty') + int(qty)})
        except ValueError:
            self.log.append('Error! При поступлении на склад указано не верное значение количества оборудования!')
        else:
            self.log.append(f'Поступление на склад: {a.type_equipment} {firm} {model} в кол-ве {qty} шт.')
        if new:
            if type_id == 1:
                list_equipment.append({'firm': a.firm, 'model': a.model, 'type_printer': a.type_printer, 'qty': qty})
            elif type_id == 2:
                list_equipment.append({'firm': a.firm, 'model': a.model, 'image_method': a.image_method, 'qty': qty})
            elif type_id == 3:
                list_equipment.append({'firm': a.firm, 'model': a.model, 'copy_speed': a.copy_speed, 'qty': qty})

    def out_store(self, type_id, firm, model, qty, to):
        if type_id == 1:
            __a = 'printer'
            list_equipment = self.store.get(__a)
        elif type_id == 2:
            __a = 'scanner'
            list_equipment = self.store.get(__a)
        elif type_id == 3:
            __a = 'copier'
            list_equipment = self.store.get(__a)

        try:
            for i in list_equipment:
                if i.get('firm') == firm and i.get('model') == model:
                    if i.get('qty') < qty:
                        raise OwnError('Error! На складе недостаточно оборудования!')
                    else:
                        self.log.append(f'Перемещение со склада в {to}: {__a} {firm} {model} в кол-ве {qty} шт.')
                        i.update({'qty': i.get('qty') - qty})
        except OwnError as err:
            self.log.append(f'Попытка перемещения со склада в {to}: {__a} {firm} {model} в кол-ве {qty} шт.')
            self.log.append(f'{err}')


my_store = Store()
my_store.in_store(1, 'Canon', 'V1', 10, 1)
my_store.in_store(1, 'Canon', 'V1', 'десять', 1)
my_store.in_store(1, 'Canon', 'V2', 5, 0)
my_store.in_store(2, 'Epson', '122', 12, 0)
my_store.in_store(2, 'Epson', '122', 3, 0)
my_store.in_store(3, 'Xerox', 'X1000', 25, 100)
my_store.in_store(3, 'Xerox', 'X1000', 7, 100)
my_store.out_store(1, 'Canon', 'V1', 11, 'Бухгалтерия')
my_store.out_store(3, 'Xerox', 'X1000', 15, 'ПТО')
print(my_store.store)
print('\n'.join(str(my_store.log).split(',')))

