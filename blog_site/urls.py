from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('', views.index),
    path('register',views.register),
    path('login',views.login_page, name='login'),
    path('logout',views.logout_page),
    path('profile',views.profile),
    path('update_profile',views.update_profile),
    path('change_password',views.change_password),
    path('blog_editor',views.blog_editor),
    path('myblogs',views.my_blogs),
    path('theblog/<int:id>',views.the_blog),
    path('editblog/<int:b_id>',views.edit_blog,name='edit_blog'),
    path('theblog/<int:b_id>/add_comment',views.add_comments,name='add_comments'),
    path('deleteblog/<int:b_id>',views.delete_blog),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]