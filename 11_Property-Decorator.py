class Classroom:
    standard = "9A"
    marks = 75
    marks_upgrade = 85

    @property
    def total_marks(self):
        return self.marks + self.marks_upgrade

    @total_marks.setter
    def total_marks(self, val):
        self.marks_upgrade = val - self.marks


e = Classroom()
print(e.total_marks)
e.total_marks = 200
print(e.total_marks)