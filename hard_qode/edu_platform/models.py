from django.db import models


class Product(models.Model):
    creator = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField()
    price = models.IntegerField()
    student_count_from = models.IntegerField(default=0)
    student_count_to = models.IntegerField()


class Lesson(models.Model):
    link = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Students(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
