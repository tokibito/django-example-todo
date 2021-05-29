from django.db import models

# Create your models here.
class Todo(models.Model):
    """
    TODOのデータを扱うモデルクラス
    このクラスのインスタンス1つが、データベース上の1レコードに相当します
    """
    name = models.CharField("Name", max_length=50)
    done = models.BooleanField("Done")
    created_at = models.DateTimeField("Created_at", auto_now_add=True)

    def __str__(self):
        return self.name
