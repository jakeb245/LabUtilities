
from course import Course


class Section(Course):
    def __init__(self, name):
        super().__init__(name)

    def _add_student(self):
        pass


