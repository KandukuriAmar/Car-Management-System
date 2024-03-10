from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = 'sdp'


class Caruserinfo(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=100, default='')  # Added default value for password
    phonenumber = models.IntegerField()

    class Meta:
        db_table = 'userbooked'
