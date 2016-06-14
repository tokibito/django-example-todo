from django.db import models

class Todo(models.Model):
    name = models.CharField("名称", max_length=50)
    done = models.BooleanField("完了")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return self.name
