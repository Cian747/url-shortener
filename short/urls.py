from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# from .views import redirect_view, shorten_via_api, post_url

urlpatterns = [
    path("api/sh", views.urlShort, name="home"),  # Home route for URL shortening form
    path("u/<str:slugs>", views.urlRedirect, name="redirect"),  # Redirect using the slug

    path('', views.url_test_view, name='shorten_url'),
    # path('<str:short_code>/', redirect_view, name='redirect'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)