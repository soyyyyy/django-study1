from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    image = models.CharField(max_length=500, default=None, null=True)
    password = models.CharField(max_length=20, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # Relation 정의
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # on_delete CASCADE: 식당이 삭제시 같이 삭제

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)