from django.db import models


# Create your models here.


class Student(models.Model):
    gender_choices = (
        (0, "男"),
        (1, "女"),
        (2, "未知"),
    )

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    number = models.IntegerField(max_length=20)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    phone = models.CharField(max_length=11, null=True, blank=True)
    pic = models.ImageField(upload_to="pic", default="pic/1.png")

    class Meta:
        db_table = "student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
