from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def index(request):
    """一覧表示
    """
    # GETパラメータに ?all=1 と指定された場合は全件を表示
    if request.GET.get('all') == '1':
        queryset = Todo.objects.all()
    else:
        # 特に指定がない場合は未完了のレコードのみ
        queryset = Todo.objects.filter(done=False)
    # 作成日時で降順にソート
    todo_list = queryset.order_by('-created_at')
    return render(request, 'index.html', {'todo_list': todo_list})

def add(request):
    """追加
    """
    # GETメソッドの場合は、データを渡していないフォーム
    # POSTメソッドの場合は、POSTされたデータを渡したフォームを生成
    form = TodoForm(request.POST or None)
    if form.is_valid():  # 入力内容の検証を実行(データが渡されていないフォームの場合は常にFalse)
        form.save()  # データベースに保存 (ModelForm.save()メソッド)
        return redirect('index')  # 一覧表示にリダイレクト
    return render(request, 'add.html', {'form': form})

def edit(request, pk):
    """編集
    """
    # データベースから既存のレコードを取得
    # 指定されたpkと一致するレコードがない場合には404 NotFoundのレスポンスを返す
    todo = get_object_or_404(Todo, pk=pk)
    # 既存のデータ(Todoクラスのインスタンスを指定したフォーム)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()  # データベースに保存
        return redirect('index')  # 一覧にリダイレクト
    return render(request, 'edit.html', {'form': form})

def done(request, pk):
    """完了
    """
    # データベースから既存のレコードを取得
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = True  # 完了扱いとする
    todo.save()  # データベースに保存
    return redirect('index')
