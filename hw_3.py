# Homework #3

class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_cpu(self):
        return self.__cpu

    def set_memory(self, memory):
        self.__memory = memory

    def get_memory(self):
        return self.__memory

    def make_computations(self):
        return f"Вычисления с CPU: {self.__cpu}, памятью: {self.__memory} выполнены!"

    def __str__(self):
        return f"Computer: CPU = {self.__cpu}, Memory = {self.__memory}GB"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory



class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def set_sim_cards(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards(self):
        return self.__sim_cards_list

    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} ({sim_card})")

    def __str__(self):
        return f"Phone with SIM cards: {', '.join(self.__sim_cards_list)}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone: {super(Computer, self).__str__()}, SIM cards = {super(Phone, self).__str__()}"


computer = Computer("Intel i7", 16)
phone = Phone(["Beeline", "O", "Megacom"])
smartphone1 = SmartPhone("Poco X3", 8, ["Beeline", "O"])
smartphone2 = SmartPhone("iPhone 14", 12, ["Beeline", "Megacom"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(computer.make_computations())
phone.call(1, "+996 777 77 77 77")
smartphone1.use_gps("Karakol")

computer2 = Computer("AMD Ryzen 5", 8)
print(computer > computer2)
