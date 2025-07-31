# url/views.py
import random
import string
from django.shortcuts import render, redirect
from .models import UrlData
from .forms import Url
from django.shortcuts import redirect
from .serializers import URLSerializer
from rest_framework.response import Response
from rest_framework import status

def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        # print(form.data)
        if form.is_valid():
            # Generate a random 10-character slug
            slug = ''.join(random.choice(string.ascii_letters) for _ in range(10))
            url = form.cleaned_data["url"]  # Get the original URL from the form
            new_url = UrlData(url=url, slug=slug)  # Save the URL and slug
            new_url.save()
            return redirect('/')  # Redirect to the homepage after saving
    else:
        form = Url()  # Empty form if it's a GET request

    data = UrlData.objects.all()  # Get all shortened URLs
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'shorten.html', context)

def urlRedirect(request, slugs):
    # Find the original URL by the slug
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)  # Redirect to the original URL

def url_test_view(request):
    if request.method == 'POST':
        url = request.POST.get('original_url')
        slug = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        new_url = UrlData(url=url,slug=slug)
        new_url.save()
        return redirect('/')

    data = UrlData.objects.all()

    context = {
        'short_url': data
    }

    return render(request, 'test.html',context)