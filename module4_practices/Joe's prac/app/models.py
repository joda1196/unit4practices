from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    dob = models.DateField(blank=True)
    grade_level = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    student_year = models.IntegerField()
    home_teacher = models.TextField()
    present = models.BooleanField(default=False)


def create_student(name, age, grade_level, student_year, home_teacher, present, dob):
    student = Student(
        name=name,
        age=age,
        grade_level=grade_level,
        student_year=student_year,
        home_teacher=home_teacher,
        present=present,
        dob=dob,
    )
    if student.grade_level < 0 or student.grade_level > 100:
        raise ValueError("Invalid Grade")
    student.save()
