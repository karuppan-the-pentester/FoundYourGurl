from django.db import models

class UsersDataBase(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=255)
    RegNo = models.TextField(max_length=255, default='SOME STRING')
    PassWord = models.TextField(max_length=255)
    Department = models.TextField(max_length=255)
    Batch = models.TextField(max_length=255)

    FatherName = models.TextField(max_length=255)
    MotherName = models.TextField(max_length=255)
    DateOfBirth = models.TextField(max_length=255)
    Address = models.TextField(max_length=255)
    Phone = models.TextField(max_length=255)
    Photo = models.TextField(max_length=255, default='SOME STRING')

    def __str__(self):
        return self.RegNo


class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.TextField(max_length=255)
    title = models.TextField(max_length=255)
    message = models.TextField(max_length=255)
    time = models.TextField(max_length=255, default='Just Now')
    url = models.TextField(max_length=255, default='{% url "students_dashboard" %}')

    def __str__(self):
        return self.title



