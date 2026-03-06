from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user, name='login'),
    path('register/',views.register_user,name='register'),
    path("home/",views.home, name='home'),
    path("note<int:pk>/",views.get_note, name='notes'),
    path("add_note/",views.add_note, name='add_note'),
    path("del_note/<int:id>/",views.delete_note,name='del_note'),
    path("update_note/<int:id>/",views.update_note,name='update_note'),
    path('register_user/',views.register_user,name='register'),
    path("logout_user/",views.logout_user, name='logout')
]
