from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .utils import generate_short_code
from django.shortcuts import redirect
from .models import ShortURL

class ShortenURL(APIView):
    def post(self, request):
        original_url = request.data.get('url')
        short_code = generate_short_code()
        short_url = ShortURL.objects.create(original_url=original_url, short_code=short_code)
        return Response({"short_url": f"http://localhost:8000/{short_code}"}, status=status.HTTP_201_CREATED)

def redirect_view(request, short_code):
    try:
        url = ShortURL.objects.get(short_code=short_code)
        url.clicks += 1
        url.save()
        return redirect(url.original_url)
    except ShortURL.DoesNotExist:
        return Response(status=404)
