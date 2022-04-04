from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user, name='register-user'),
    path('register-clerk/', register_clerk, name='register-clerk'),
    path('login/', login_user, name='login-user'),
    path('logout/', logout_user, name='logout-user'),
    path('email-verify/<str:token_id>/', verify_email, name='email-verify'),
    path('view-clerks/', view_clerks, name='view-clerks'),
    path('inactivate/<str:id>/', inactivate_clerk, name='inactivate-clerk'),
    path('activate/<str:id>/', activate_clerk, name='activate-clerk'),
    path('delete/<str:id>/', delete_clerk, name='delete-clerk'),
]