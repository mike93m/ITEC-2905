from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.contrib import messages

# Create your views here.

def home(request):
    app_name = 'Fun viral videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):
    # Handle the form submission
    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            new_video_form.save()
            messages.success(request, 'Video added successfully!')
        else:
            messages.warning(request, 'Error adding video. Please check the form.')
            render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})