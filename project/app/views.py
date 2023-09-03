from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    print('aaaaa')
    print(request)
    return HttpResponse("Hello, World!")

def my_view(request):
    # データの取得または計算
    dynamic_data = "これは動的なデータです。"
    # データをテンプレートに渡す
    return render(request, 'my_template.html', {'dynamic_data': dynamic_data})