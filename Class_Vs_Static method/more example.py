class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student

    @staticmethod
    def is_full_name(name_str):
        name = name_str.split(' ')
        return len(name) > 1


scott = Student.from_string('Scott Robinson')
scott1 = Student.is_full_name('Scott Robinson')
print(scott)
print(scott1)