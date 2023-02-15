# from http import HTTPStatus

# from django.db.models import Sum
# from django.http import FileResponse
from django.shortcuts import get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response

from api.serializers import (MusicianSerializer,  # isort:skip
                             AlbumSerializer, SongSerializer)
from catalog.models import Musician, Album, Song  # isort:skip


class MusicianViewSet(viewsets.ModelViewSet):
    """
    ViewSet для отображения списка или одного ингредиента.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class SongViewSet(viewsets.ModelViewSet):
    """
    ViewSet для отображения списка или одного тега.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    ViewSet для отображения списка или одного рецепта,
    редактирования, обновления и удаления рецепта. Для
    добавления или удаления рецепта в избранное или список покупок.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
