# example/views.py
from django.shortcuts import render, redirect
from .forms import UserDataForm, UserBlogForm
from .models import UserDataModel, UserBlogModel
import uuid

def signup(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        
        if form.is_valid():
            f = UserDataModel(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
                identifier = str(uuid.uuid4())
            )
            f.save()
            
            return redirect('/login/')
            
    return render(request, "signup.html")


# def home(request):
#     identifier = request.GET.get('identifier')
#     # filter user from UserDataModel
#     user = UserDataModel.objects.filter(identifier=identifier)
#     if user:
#         return render(request, "home.html", {'user': user[0]})
#     else:
#         return render(request, "login.html")


def post(request):
    identifier = request.GET.get('identifier')
    # filter user from UserDataModel
    user = UserDataModel.objects.filter(identifier=identifier)
            
    if user:
        form = UserBlogForm()
        if request.method == "POST":
            form = UserBlogForm(request.POST, request.FILES)
            
            
            if form.is_valid():
                f = UserBlogModel(
                    username = user[0].username,
                    content = form.cleaned_data['content'],
                    image = form.cleaned_data['image'],
                    numOfTrashPickedUp = form.cleaned_data['numOfTrashPickedUp'],
                    numOfPPl = form.cleaned_data['numOfPPl'],
                    isPicturePublic = form.cleaned_data['isPicturePublic']
                )
                
                # get a user model by the identifier
                users = UserDataModel.objects.filter(identifier=identifier)
                # increase the user's points by 1
                user = users.first()
                print(user.points)
                user.points += 1
                print(user.points)
                user.save()
                
                f.save()
                
                return redirect(f'/feed?identifier={identifier}')
                            
        return render(request, "post.html", {'user': user, "form": form})
    else:
        return redirect('/login/')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = UserDataModel.objects.filter(username=username, password=password)
        
        if user:
            return redirect(f'/feed?identifier={user[0].identifier}')
        else:
            return render(request, 'login.html', {'error': 'User not found'})
        
    return render(request, 'login.html')

def redeem(request):
    # make sure user is identified
    identifier = request.GET.get('identifier')
    user = UserDataModel.objects.filter(identifier=identifier)
    if user:
        return render(request, "redeem.html", {'user': user[0]})
    else:
        return redirect('/login/')

def leaderboard(request):
    users = UserDataModel.objects.all().order_by('-points')
    return render(request, "leaderboard.html", {'users': users})

def feed(request):
    # make sure user is identified
    identifier = request.GET.get('identifier')
    user = UserDataModel.objects.filter(identifier=identifier)
    if user:
        # get all of the user's blog posts
        posts = UserBlogModel.objects.all()
        return render(request, "feed.html", {'posts': reversed(posts), 'user': user[0]})
    else:
        return redirect('/login/')