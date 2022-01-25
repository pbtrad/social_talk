from django.shortcuts import render, redirect
from .models import Profile, Chat
from .forms import ChatForm

def dashboard(request):
    form = ChatForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.save()
            return redirect("talk:dashboard")

    followed_chats = Chat.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(request, "talk/dashboard.html", {"form": form, "chats": followed_chats})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "talk/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "talk/profile.html", {"profile": profile})