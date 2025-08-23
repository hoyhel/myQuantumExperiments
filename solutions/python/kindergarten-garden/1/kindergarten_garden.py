class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram
        self.students = sorted(students)
        self.final_diagram = self.diagram_generator()

    def diagram_generator(self):
        self.final_diagram = []
        
        rows = self.diagram.split("\n")
        # Seperate the strings by 2 letters
        row_0 = [rows[0][i:i+2] for i in range(0, len(rows[0]), 2)]
        row_1 = [rows[1][i:i+2] for i in range(0, len(rows[1]), 2)]
        for index, row in enumerate(row_0):
            row_0[index] += row_1[index]
            
        return row_0

    def plants(self, name):
        index = self.students.index(name)
        plant_letters_str = self.final_diagram[index]
        plants = []

        for plant in plant_letters_str:
            if plant == "G":
                plants.append("Grass")
            elif plant == "C":
                plants.append("Clover")
            elif plant == "R":
                plants.append("Radishes")
            elif plant == "V":
                plants.append("Violets")
        return plants

        
        
        
