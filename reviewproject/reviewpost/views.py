from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signupview(request):
    if request.method == 'POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        user=User.objects.create_user(username_data,'',password_data)
    else:
        return render(request, 'signup.html',{})
    return render(request, 'signup.html',{})
