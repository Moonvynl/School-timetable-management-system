import django_setup
from project.models import Subject, Teacher, Class, Student


#subj1 = Subject(
#    name='Math',
#    description = 'Math'
#).save()
#
#subj2 = Subject(
#    name='English',
#    description = 'English'
#).save()
#
#subj3 = Subject(
#    name='History',
#    description = 'History'
#).save()
#
#teacher1= Teacher(
#    name='John Doe',
#    subjects=Subject.objects.get(id=1)
#).save()
#
#teacher2 = Teacher(
#    name='Dark Bat',
#    subjects=Subject.objects.get(id=2)
#).save()
#
#teacher3 = Teacher(
#    name='Batman',
#    subjects=Subject.objects.get(id=3)
#).save()
#
#class1 = Class(
#    name='1A',
#    teacher=Teacher.objects.get(id=1)
#).save()
#
#student1 = Student(
#    name='Spider man',
#    age=18,
#    address = 'Gotham City 32',
#    classes=Class.objects.get(id=1)
#).save()
