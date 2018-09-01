from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('姓名',max_length=20)
    birthday = models.CharField('姓名',max_length=20)
    phone = models.CharField('姓名',max_length=20)
    age = models.CharField('姓名',max_length=20)
    score = models.CharField('姓名',max_length=20)
    Email = models.EmailField('邮箱')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '详细信息'


