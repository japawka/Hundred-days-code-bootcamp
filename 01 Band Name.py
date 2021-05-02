for x in range(1, 11):
    line = ''
    for y in range(1, 11):
        line += f"\t{x*y:3}"
    print(line[1:])