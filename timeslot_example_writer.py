with open('timeslots.txt', 'w') as f:
	for i in range(20):
		for j in range(3):
			f.write(f'Day {i+1}, Lunch Slot {j + 1}\n')
		for j in range(3):
			f.write(f'Day {i+1}, After-School Slot {j + 1}\n')
