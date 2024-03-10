from django.urls import path
from app import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.home, name='home'),
    path('preview/', views.preview, name='preview'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.userLogin, name='login'),
    path('signup/', views.userSignUp, name='signup'),
    path('logout/', views.userLogOut, name='logout'),
    path('profile/', views.userProfile, name='profile'),
    path('delete/<int:pk>/', views.deleteUser.as_view(), name='delete'),
    path('password/reset/', authViews.PasswordResetView.as_view(template_name='passwordReset.html'), name='password_reset'),
    path('reset/done/', authViews.PasswordResetDoneView.as_view(template_name='resetDone.html'), name='password_reset_done'),
    path('set/new/password/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='resetConfirm.html'), name='password_reset_confirm'),
    path('reset/complete/', authViews.PasswordResetCompleteView.as_view(template_name='resetComplete.html'), name='password_reset_complete'),
]