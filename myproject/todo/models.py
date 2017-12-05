from django.db import models

# Create your models here.
class Todo(models.Model):
    """
    TODOのデータを扱うモデルクラス
    このクラスのインスタンス1つが、データベース上の1レコードに相当します
    """
    name = models.CharField("名称", max_length=50)
    done = models.BooleanField("完了")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return self.name
