from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views  # isort:skip


router = DefaultRouter()

router.register(r'albums', views.AlbumViewSet, basename='album')
router.register(r'musicians', views.MusicianViewSet, basename='musician')
router.register(r'songs', views.SongViewSet, basename='song')
router.register(r'musicians/(?P<id>\d+)/albums',
                views.CatalogViewSet,
                basename='albums'
                )


urlpatterns = [
    path('v1/', include(router.urls)),
]
