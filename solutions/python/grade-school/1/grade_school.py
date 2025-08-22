class School:
    def __init__(self):
        self.students = {}
        self.added_list = []

    def add_student(self, name, grade):
        if any(name in student_list for student_list in self.students.values()):
            self.added_list.append(False)
        else:
            if grade in self.students:
                self.students[grade].append(name)
            else:
                self.students[grade] = [name]
            self.added_list.append(True)

    def roster(self):
        if not self.students:
            return []
        sorted_grades = sorted(self.students.keys())
        result = []
        for grade in sorted_grades:
            result.extend(sorted(self.students[grade]))
        return result

    def grade(self, grade_number):
        if grade_number in self.students:
            return sorted(self.students[grade_number])
        else:
            return []

    def added(self):
        return self.added_list