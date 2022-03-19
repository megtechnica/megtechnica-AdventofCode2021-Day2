from directions import puzzle_input
import copy

input = copy.copy(puzzle_input)

def get_directions(input):
  horizontal = 0
  depth = 0
  aim = 0

  
  for line in input.splitlines():
    position = line.split()
    command = position[0]
    move = int(position[1])
    if command == "down":
      aim += move
    elif command == "up":
      aim -= move
    else:
      horizontal += move
      depth += (move * aim)

  return(horizontal * depth)

print(get_directions(input))
