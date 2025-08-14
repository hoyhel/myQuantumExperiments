class Queen:
    def __init__(self, row, column):
        # Validate row
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        # Validate column
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, other):
        # Check if both queens are in the same square
        if self.row == other.row and self.column == other.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        # Same row
        if self.row == other.row:
            return True

        # Same column
        if self.column == other.column:
            return True

        # Same diagonal: difference of row and column equal in absolute value
        if abs(self.row - other.row) == abs(self.column - other.column):
            return True

        # None of the above - cannot attack
        return False
