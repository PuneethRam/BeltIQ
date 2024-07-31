from django.urls import path
from admin_datta import views
from django.contrib.auth import views as auth_views

from . import views





urlpatterns = [
  #path('generate_pdf_report/<int:uploaded_image_id>/', views.generate_pdf_report, name='generate_pdf_report'),
  path('prediction/', views.prediction, name='prediction'),  
  path('profile/', views.profile, name='profile'),
  path('misleading_telegram/', views.misleading_telegram, name='misleading_telegram'),
  path(''       , views.index, name='index'),

  # Authentication
  path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),
  path('accounts/login/', views.UserLoginView.as_view(), name='login'),
  path('accounts/logout/', views.logout_view, name='logout'),

  path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
  path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
      template_name='accounts/auth-password-change-done.html'
  ), name="password_change_done"),

  path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
  path('accounts/password-reset-confirm/<uidb64>/<token>/',
    views.UserPasswrodResetConfirmView.as_view(), name="password_reset_confirm"
  ),
  path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
    template_name='accounts/auth-password-reset-done.html'
  ), name='password_reset_done'),
  path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    template_name='accounts/auth-password-reset-complete.html'
  ), name='password_reset_complete'),

  path('live_data/', views.live_data, name='live_data'),

  path('failure/', views.failure, name='failure'),

]
