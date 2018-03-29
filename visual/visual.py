#!/usr/bin/python
import sys
import re
import drawer as dr
from classes import Room, Farm



def read_data():
	
	farm = Farm()
	moves = []
	for line in sys.stdin:
		line = line.rstrip('\n')
		#Read number of ants
		if (re.match('^\d+$', line)):
			farm.ants = int(line)
		#Execute ##start/##end instruction
		elif (line == "##start" or line == "##end"):
			temp = line.strip('#')
			line = sys.stdin.next().strip('\n')
			farm.add_room(line, temp)
			continue
		#Room parameter (smth like 'A 2 3')
		elif (re.match('\w+ \d+ \d+', line)):
			farm.add_room(line, "common")
		#Link between rooms (smth like 'A-B')
		elif (re.match('^(?!L)(\w|\d)+-(\w|\d)+$', line)):
			farm.add_link(line)
		#Moves of ants (smth like 'L3-B')
		elif (re.match('^L+', line)):
			moves.append(line.strip())
	return(farm, moves)

def main():
	farm, moves = read_data()
	# if (len(rooms) == 0):
	# 	print ("Error")
	# 	exit (1)
	#dr.draw_graph(rooms, links)
	print (farm.ants)
	print(farm.room_index)
	for room in farm.rooms:
		print ("name: {}\nx: {}\ny: {}\n".format(room.name, room.x, room.y))
	print (farm.links)
	print (moves)
	print(farm.start_room, farm.end_room)

if __name__ == "__main__":
	main()