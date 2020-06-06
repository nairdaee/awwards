from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Rating, categories, technologies
from .forms import ProfileForm, UploadForm, RatingForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    projects = Project.objects.order_by('-overall').all()
    top = projects[0]
    runners=Project.objects.all()[:4]
    try:
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit')
    return render(request, 'index.html', locals())

@login_required(login_url='/accounts/login')
def profile(request):
    current_user=request.user
    profile =Profile.objects.get(user=current_user)
    projects = Project.objects.filter(user=current_user)
    my_profile = Profile.objects.get(user=current_user)
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()
            return redirect('myprofile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', {'form': form, 'profile':profile})

@login_required(login_url='/accounts/login')
def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            return redirect('index')
    else:
        form = UploadForm()
    return render(request, 'new_project.html', {'form': form,'profile':profile})
