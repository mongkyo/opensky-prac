from django.shortcuts import redirect


def index(request):
    # 곧바로 polls로 redirect되도록 설정
    # /polls/라고 써도 작동한다. 하지만 뒤에 문제가 생기는 경우를 보기 위해 index라고 쓴다
    # 여기서의 index는 polls/urls의 name='index'설정의 index이다.
    return redirect('index')