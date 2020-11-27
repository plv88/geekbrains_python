from sys import argv

script_name, production, rate, bonus = argv
result = (int(production) * int(rate)) + int(bonus)
print(f"Заработная плата состовляет {result}")
