from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .utils import generate_short_code
from django.shortcuts import redirect
from .models import ShortURL
import requests
from django.http import JsonResponse
from .serializers import URLSerializer

# class ShortenURL(APIView):
#     def post(self, request):
#         serializer = URLSerializer(data = request.data)
#         if serializer.is_valid():
#             original_url = serializer.validated_data['url']
#             print(original_url)
#             short_code = generate_short_code()
#             print(short_code)
#             short_url = ShortURL.objects.create(original_url=original_url, short_code=short_code)
#             return Response({"short_url": f"http://localhost:8000/{short_code}"}, status=status.HTTP_201_CREATED)
        
#         if not serializer.is_valid():
#             print("Validation errors:", serializer.errors)
#             return Response(serializer.errors, status=400)


        # # Ensure we are sending JSON with correct headers
        # api_response = requests.post(
        #     "http://localhost:8000/api/shorten/",  # or use your domain
        #     json={"url": original_url},
        #     headers={"Content-Type": "application/json"}
        # )

        # try:
        #     data = api_response.json()
        # except ValueError:
        #     return JsonResponse({"error": "Invalid response from API"}, status=500)

        # return JsonResponse(data)

def shorten_via_api(request):
    if request.method == "POST":
        original_url = request.POST.get("url")

        # Ensure we are sending JSON with correct headers
        api_response = requests.post(
            "http://localhost:8000/api/shorten/",  # or use your domain
            json={"url": original_url},
            headers={"Content-Type": "application/json"}
        )

        try:
            data = api_response.json()
        except ValueError:
            return JsonResponse({"error": "Invalid response from API"}, status=500)

        return JsonResponse(data)

    return render(request, "shorten.html")

def redirect_view(request, short_code):
    try:
        url = ShortURL.objects.get(short_code=short_code)
        url.clicks += 1
        url.save()
        return redirect(url.original_url)
    except ShortURL.DoesNotExist:
        return Response(status=404)
