from lessons.lesson_1 import Car

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

car_subaru = Car(color="blue", model="Subaru")
print(car_subaru)
