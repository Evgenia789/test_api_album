from rest_framework import viewsets

from api.serializers import (AlbumSerializer, CatalogSerializer,  # isort:skip
                             MusicianSerializer, SongSerializer)
from catalog.models import Album, Musician, Song  # isort:skip


class MusicianViewSet(viewsets.ModelViewSet):
    """
    ViewSet to display a list or a single musician.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class SongViewSet(viewsets.ModelViewSet):
    """
    ViewSet to display a list or a single song.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    ViewSet to display a list or a single musician,
    edit, update and delete an album.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    """
    ViewSet to display a list of the musician's albums.
    """
    serializer_class = CatalogSerializer

    def get_queryset(self):
        musician_id = self.kwargs.get("id")
        return Musician.objects.filter(id=musician_id)
