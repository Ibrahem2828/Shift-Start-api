from django.urls import path
from django.views.generic import RedirectView 
from .Login import user_list,register_user,login_user,home_view  ,index,delete_user             

urlpatterns = [
    path('', RedirectView.as_view(url='index/', permanent=False)), 
    path('users/', user_list, name='user_list'),  
    # path('users/<str:username>/<str:user_id>/', user_list, name='user_list'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('home/<str:username>/<str:user_id>/', home_view, name='home'), 
    path('delete_user/<str:username>/', delete_user, name='delete_user'), # تعديل هنا
    path('index/', index, name='index'),
]