# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)

    def move(self, instructions):
        directions = [NORTH, EAST, SOUTH, WEST]

        for instruction in instructions:
            index = directions.index(self.direction)
            if instruction == "R":
                new_index = (index + 1) % 4
                self.direction = directions[new_index]
            elif instruction == "L":
                new_index = (index - 1) % 4
                self.direction = directions[new_index]
            elif instruction == "A":
                if self.direction == NORTH:
                    self.y_pos += 1
                elif self.direction == SOUTH:
                    self.y_pos -= 1
                elif self.direction == EAST:
                    self.x_pos += 1
                elif self.direction == WEST:
                    self.x_pos -= 1
                    
            self.coordinates = (self.x_pos, self.y_pos)
