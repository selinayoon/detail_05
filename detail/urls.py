from django.urls import path
from . import views

app_name="details"

urlpatterns = [
    path("",views.list, name="list"),
    path("qna/",views.qna, name="qna"),
    path("mypage/",views.mypage, name="mypage"),
    path("signup/",views.signup, name="signup"),
    path("<str:not_found>/",views.error, name="error"),
    ]