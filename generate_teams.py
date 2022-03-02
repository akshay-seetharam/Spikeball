import names
with open('teams.txt', 'w') as f:
	for i in range(80):
            f.write(f'{names.get_first_name()} and {names.get_first_name()}\n')
