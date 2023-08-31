from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='Наименование комнаты')


class UserProfile(models.Model):
    name = models.ForeignKey(User, verbose_name='Никнейм пользователя')
    avatar = models.ImageField(upload_to='upload_image/')
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, verbose_name='Подключение к комнате')
    online = models.BooleanField(default=False)


class Message(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room_chat = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()



class Chat(models.Model):
    pass