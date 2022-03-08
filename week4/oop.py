"""1) I use classes, inheritance and encapsulation
2), 3) Polymorphism
"""

from dataclasses import dataclass
from typing import List, Union


@dataclass
class Student:
    name: str
    age: int
    group: int


class EducationalInstitution:
    def __init__(self, students: List[Student]):
        self.__students = students


    def __add__(self, other_school: Union['School', 'Gimnasium']) -> 'EducationalInstitution':
        list_of_students = list()
        list_of_students.extend(self.__students) 
        list_of_students.extend(other_school.students)

        return EducationalInstitution(list_of_students)


    @property
    def students(self) -> list:
        return self.__students


    @students.setter
    def students(self, student: Student):
        self.__students.append(student)

    
    def add(self, other_school: Union['School', 'Gimnasium']) -> 'EducationalInstitution':
        list_of_students = list()
        list_of_students.extend(self.__students) 
        list_of_students.extend(other_school.students)

        return EducationalInstitution(list_of_students)


class School(EducationalInstitution):
    def __init__(self, students: List[Student]):
        super().__init__(students)

    
    def __add__(self, other_school: Union['School', 'Gimnasium']) -> Union['Gimnasium', EducationalInstitution]:
        list_of_students = list()
        list_of_students.extend(self.__students)
        list_of_students.extend(other_school.students)

        if isinstance(other_school, School):
            return Gimnasium(list_of_students)

        return EducationalInstitution(list_of_students)

    
    def add(self, other_school: Union['School', 'Gimnasium']) -> Union['Gimnasium', EducationalInstitution]:
        list_of_students = list()
        list_of_students.extend(self.__students)
        list_of_students.extend(other_school.students)

        if isinstance(other_school, School):
            return Gimnasium(list_of_students)

        return EducationalInstitution(list_of_students)


class Gimnasium(EducationalInstitution):
    def __init__(self, students: List[Student]):
        super().__init__(students)
    

    def __add__(self, other_school: Union['School', 'Gimnasium']) -> Union['Gimnasium', EducationalInstitution]:
        list_of_students = list()
        list_of_students.extend(self.__students)
        list_of_students.extend(other_school.students)

        if isinstance(other_school, Gimnasium):
            return Gimnasium(list_of_students)

        return EducationalInstitution(list_of_students)


    def add(self, other_school: Union['School', 'Gimnasium']) -> Union['Gimnasium', EducationalInstitution]:
        list_of_students = list()
        list_of_students.extend(self.__students)
        list_of_students.extend(other_school.students)

        if isinstance(other_school, Gimnasium):
            return Gimnasium(list_of_students)

        return EducationalInstitution(list_of_students)
