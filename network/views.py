from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *
import json
from django.http import JsonResponse

def remove_like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = request.user
    Like.objects.filter(user=user, post=post).delete()
    return JsonResponse({"message": "Like removed!"})


def add_like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = request.user

    # Prevent duplicate likes (optional safeguard)
    if not Like.objects.filter(user=user, post=post).exists():
        Like.objects.create(user=user, post=post)
        return JsonResponse({"message": "Like added!"})
    else:
        return JsonResponse({"message": "Already liked."})

def index(request):
    allPosts = Post.objects.all().order_by("-id")  # Keep latest first

    # Pagination
    paginator = Paginator(allPosts, 5)
    page_number = request.GET.get('page')
    posts_of_the_page = paginator.get_page(page_number)

    # Get likes for current user only, more efficient
    whoYouLiked = []
    if request.user.is_authenticated:
        whoYouLiked = list(
            Like.objects.filter(user=request.user)
            .values_list('post__id', flat=True)
        )

    return render(request, "network/index.html", {
        "posts_of_the_page": posts_of_the_page,
        "whoYouLiked": whoYouLiked
    })


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    allPosts = Post.objects.filter(user=user).order_by("-id")

    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    if request.method == 'POST' and request.user == user:
        uploaded_image = request.FILES.get("profile_image")
        if uploaded_image:
            user.profile.image = uploaded_image
            user.profile.save()
            return redirect('profile', user_id=user.id)

    following = Follow.objects.filter(user=user)
    followers = Follow.objects.filter(user_follower=user)

    try:
        checkFollow = followers.filter(user=request.user)
        isFollowing = checkFollow.exists()
    except:
        isFollowing = False

    # ✅ Pagination
    paginator = Paginator(allPosts, 3)
    page_number = request.GET.get('page')
    posts_of_the_page = paginator.get_page(page_number)

    return render(request, "network/profile.html", {
        "posts_of_the_page": posts_of_the_page,
        "username": user.username.title(),
        "following": following,
        "followers": followers,
        "isFollowing": isFollowing,
        "user_profile": user,
        "profile_image": user.profile.image.url if user.profile.image else None
    })

def createPost(request):
    return render(request,"network/createPost.html")

def newPost(request):
    if request.method == "POST":
        content = request.POST['content']
        user=User.objects.get(pk=request.user.id)
        post=Post(content=content, user=user)
        post.save()
        return HttpResponseRedirect(reverse(index))
    

def follow(request):
    userfollow = request.POST['userfollow']
    currentUser = User.objects.get(pk=request.user.id)
    userfollowData=User.objects.get(username=userfollow)
    f=Follow(user=currentUser, user_follower=userfollowData)
    f.save()
    user_id = userfollowData.id
    return HttpResponseRedirect(reverse(profile,kwargs={'user_id':user_id}))

def unfollow(request):
    userfollow = request.POST['userfollow']
    currentUser = User.objects.get(pk=request.user.id)
    userfollowData = User.objects.get(username=userfollow)
    
    # Retrieve the Follow object from the database
    try:
        f = Follow.objects.get(user=currentUser, user_follower=userfollowData)
        f.delete()  # This deletes the retrieved object
    except Follow.DoesNotExist:
        # Handle the case where the Follow object doesn't exist
        return HttpResponse("Follow relationship does not exist", status=404)
    
    user_id = userfollowData.id
    return HttpResponseRedirect(reverse('profile', kwargs={'user_id': user_id}))



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        print(username+" "+password)
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def following(request):
    currentUser=User.objects.get(pk=request.user.id)
    followingPeople = Follow.objects.filter(user=currentUser)
    allPosts = Post.objects.all().order_by('id').reverse()

    followingPosts =[]

    for post in allPosts:
        for person in followingPeople:
            if person.user_follower == post.user:
                followingPosts.append(post)

    # Pagination
    paginator = Paginator(followingPosts, 3)
    page_number = request.GET.get('page')
    posts_of_the_page = paginator.get_page(page_number)

    return render(request, "network/following.html",{
        "posts_of_the_page":posts_of_the_page     
        })

def edit(request, post_id):
    if request.method =='POST':
        data = json.loads(request.body)
        edit_post = Post.objects.get(pk = post_id)
        edit_post.content = data["content"]
        edit_post.save()
        return JsonResponse({"message": "Change successful", "data":data["content"]})