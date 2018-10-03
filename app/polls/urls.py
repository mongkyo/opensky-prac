from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # config.urls 에서 include로 /polls/라고 왔을 때 이 polls/urls를 참조하게 만들었으므로
    # 아래의 식이 실행되는 경우는 http://127.0.0.1:8000/pol ls/ 이다.
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
