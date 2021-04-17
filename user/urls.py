from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, SetPasswordForm, PasswordChange
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/edit/', views.editUser, name='edit-user'),


    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='user/password_change_form.html', form_class=PasswordChange, success_url = reverse_lazy('dashboard')), name='change_password'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='user/reset_password.html', form_class=UserPasswordResetForm), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html', form_class=SetPasswordForm), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/reset_password_complete.html'), name='password_reset_complete'),
]