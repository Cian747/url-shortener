from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import redirect_view, shorten_via_api, post_url

urlpatterns = [
    path('api/shorten/', post_url, name='shorten'),
    path('<str:short_code>/', redirect_view, name='redirect'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)