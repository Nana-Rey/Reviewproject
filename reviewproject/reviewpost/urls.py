from django.urls import path
from .views import signupview ,loginview, sampleview

urlpatterns=[
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('sample/', sampleview),
]