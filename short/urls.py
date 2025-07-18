from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# from .views import redirect_view, shorten_via_api, post_url

urlpatterns = [
    path("", views.urlShort, name="home"),  # Home route for URL shortening form
    path("u/<str:slugs>", views.urlRedirect, name="redirect"),  # Redirect using the slug

    # path('api/shorten/', shorten_via_api, name='shorten'),
    # path('<str:short_code>/', redirect_view, name='redirect'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)