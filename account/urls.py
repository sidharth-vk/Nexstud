
from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', views.login_attempt,name="login"),
    path('logout', views.logout_attempt,name="logout"),
    path('register', views.register,name="register"),
    path('profile', views.profilePage,name="profilepage"),
    path('profile/edit', views.profileform,name="profileform"),
    path('admission/register', views.addmission,name="formaddmision"),



    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] 
