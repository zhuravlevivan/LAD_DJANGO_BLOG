from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('addpost/', views.AddPost.as_view(), name='add_post'),
    path('edit/<int:pk>', views.UpdatePost.as_view(), name='post_update'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name='post_delete'),
    path('search/', views.post_search, name='post_search'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/registration/logged_out.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # url-адреса смены пароля
    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='blog/registration/password_change_form.html'),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='blog/registration/password_change_done.html'),
         name='password_change_done'),
    # url-адреса сброса пароля
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='blog/registration/password_reset_form.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='blog/registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='blog/registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='blog/registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
