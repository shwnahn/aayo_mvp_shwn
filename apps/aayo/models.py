from django.db import models
from django.contrib.auth.models import User

class Cafe(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)  # 이미지 URL 필드 추가
    def __str__(self):
        return f"{self.name} ({self.cafe.name})"

class Room(models.Model):
    name = models.CharField(max_length=255)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    unique_link = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return f"(Room{self.id})[{self.cafe.name}] {self.name}"

# 각 방별로 계정 따로 파져야 함.
class RoomAccount(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.username} (Room{self.room.id}: {self.room.name})"

class Order(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(RoomAccount, on_delete=models.CASCADE)
    selected_menu = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.user.username}의 {self.selected_menu} 주문"