from django.contrib import admin
from django.urls import path, include
from polls_app.views import *
from django.contrib.auth.views import LoginView, LogoutView
from polls_app import views



urlpatterns = [
    path('', LoginView.as_view(template_name='Login.html'), name='Login'),
    path('Poll_Creation/', create_poll, name="Poll_Creation"),
    path('polls/<int:poll_id>/responses/', ResponseCreateView.as_view(), name="Submit_Response"),
    path('polls/<int:poll_id>/results/', PollResultsView.as_view(), name="Poll_Results"),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('vote/<int:poll_id>/<int:option_id>/', views.vote, name='vote'),
    path('register/', register, name='Register'),
    path('login/', LoginView.as_view(template_name='Login.html'), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('dashboard/', dashboard, name='Dashboard'),
    path('accounts/<int:user_id>/', views.UserPolls, name='UserPolls'),

    path('Delete_poll/<int:poll_id>/', views.Delete_poll, name='Delete_poll'),
]
