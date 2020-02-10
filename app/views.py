from django.shortcuts import render, redirect
from .models import Profile
from .forms import EditUserForm

def base(request):
	return render(request,'app/base.html')

def profiles(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, "app/profiles.html", context)

def profile(request, pk):
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance = Profile.objects.get(id=pk))
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile', pk)
    else:
        form = EditUserForm(instance = Profile.objects.get(id=pk))
    context = {
        'profile': Profile.objects.get(id=pk),
        'form': form,
    }
    return render(request, "app/profile.html", context)







"""

    profile_instance = Profile.objects.get(id=pk)
    form = EditUserForm(request.POST, request.FILES, instance = profile_instance)
    context = {
        'profile': profile_instance,
        'form': form,
    }
    if request.method == "POST":
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile', pk)
        else:
            print("form not valid")
            print(form.errors)
    else:
        context = {
        'profile': profile_instance,
        'form': form,
    }
        return render(request, "app/profile.html", context)
"""