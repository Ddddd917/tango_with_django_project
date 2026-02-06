from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    # max_length=128:
    # unique=True:
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # 嵌套的 Meta 类用于设置后台显示的元数据
    class Meta:
        verbose_name_plural = 'Categories'  # 修正复数拼写，否则 Django 会显示 'Categorys'

    def __str__(self):
        return self.name  # 打印对象时显示名字，而不是 <Category object>


class Page(models.Model):
    # 外键关联：一个 Category 可以包含多个 Page
    # on_delete=models.CASCADE: 如果删除了 Category，关联的 Page 也会被删除
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title