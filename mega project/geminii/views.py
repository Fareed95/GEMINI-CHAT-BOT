from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Chat  # Import your Chat model
from .bot_algo import bot_gemini

def home(request):
    if request.user.is_authenticated:
        username = request.user.username
        recent_chats = Chat.objects.filter(user=request.user).order_by('-timestamp')[:3]
        return render(request, "index.html", {'username': username, 'recent_chats': recent_chats})
    else:
        return redirect('login')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'login.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')
        pass1 = request.POST.get('login_password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        response_text = bot_gemini(message)
        
        # Save the chat message to the database
        Chat.objects.create(user=request.user, message=message, response=response_text)
        
        return JsonResponse({'response': response_text})
    else:
        return JsonResponse({'error': 'Invalid request method'})
