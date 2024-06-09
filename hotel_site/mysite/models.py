from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, unique=True, null=True, blank=True)
    last_name = models.CharField(max_length=20, unique=True, null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    country = models.CharField(max_length=20, unique=True, null=True, blank=True)
    photo = models.ImageField(upload_to='ing/', null=True, blank=False)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.user


class Hotel(models.Model):
    name = models.CharField(max_length=36)
    description = models.TextField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=36, unique=True)
    country = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ing/', null=True, blank=False)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7")
    )
    value = models.CharField(max_length=16, choices=room_number)
    Capacity = (
        ("1-3", "1-3"),
        ("3-5", "3-5"),
        ("5-10", "5-10"),
        ("10-15", "10-15"),
        ("15-20", "15-20"),
        ("20+", "20+")
    )
    capacity = models.CharField(max_length=16, choices=Capacity)
    price_per_night = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.hotel


class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ing/', null=True, blank=True)


class Comment(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField()
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    )
    value = models.CharField(max_length=16, choices=rating)

    def __str__(self):
        return f'{self.user} - {self.hotel}'


class Booking(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.PositiveSmallIntegerField()
    STATUS_CHOICES = (
        ("Бронированный", "Бронированный"),
        ("Занят", "Занят"),
        ("Свободный", "Свободный")
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.user} - {self.room}'
