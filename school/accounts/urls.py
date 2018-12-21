from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpCreateView.as_view(), name='signup'),
]
