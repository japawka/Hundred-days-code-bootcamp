from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Pokemon Name", ['Pikachu','Jurek', 'Charmander'])
table.add_column("Type", ['Electric','Water', 'Fire'])
table.add_column("Strenght", [123, 456, 154])
print(table)
table.add_row(["Brisbane", 'Woodem', 5905])
table.align = "l"
print(table)