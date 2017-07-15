from django.shortcuts import redirect
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from .models import Todo
from .forms import TodoForm


class Index(generic.ListView):
    """一覧表示
    """
    template_name = 'index.html'

    def get_queryset(self):
        # GETパラメータに ?all=1 と指定された場合は全件を表示
        if self.request.GET.get('all') == '1':
            queryset = Todo.objects.all()
        else:
            # 特に指定がない場合は未完了のレコードのみ
            queryset = Todo.objects.filter(done=False)
        # 作成日時で降順にソート
        todo_list = queryset.order_by('-created_at')
        return todo_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = context['object_list']
        return context


class Add(generic.CreateView):
    """追加
    """
    form_class = TodoForm
    template_name = 'add.html'
    success_url = reverse_lazy('index')


class Edit(generic.UpdateView):
    """編集
    """
    model = Todo
    form_class = TodoForm
    template_name = 'edit.html'
    success_url = reverse_lazy('index')


class Done(SingleObjectMixin, generic.View):
    """完了
    """
    model = Todo

    def get(self, request, *args, **kwargs):
        # データベースから既存のレコードを取得
        todo = self.get_object()
        todo.done = True  # 完了扱いとする
        todo.save()  # データベースに保存
        return redirect('index')
