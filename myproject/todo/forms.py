from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    """Todoモデルを編集するためのフォームクラス

    ModelFormクラスを継承しているため、
    Todoモデルのフィールドから自動的にフォームフィールドが生成されます
    """
    class Meta:
        model = Todo
        fields = ['name', 'done']
