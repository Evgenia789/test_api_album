from django.db import models


class Musician(models.Model):
    """A class used to represent a musician."""
    name = models.CharField(
        max_length=200,
         unique=True,
         verbose_name='Musician name'
    )

    class Meta:
        verbose_name = 'Musician'
        verbose_name_plural = 'Musicians'

    def __str__(self):
        return f'{self.name}'


class Song(models.Model):
    """A class used to represent a song."""
    name = models.CharField(max_length=200, verbose_name='Song name')

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return f'{self.name}'


class Album(models.Model):
    """A class used to represent an album."""
    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        related_name='albums',
        verbose_name='Musician name'
    )
    year = models.IntegerField(verbose_name='Year of release')
    songs = models.ManyToManyField(
        Song,
        through='Membership',
        verbose_name='Song name'
    )

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return f'Album {self.id}'


class Membership(models.Model):
    """A class used to represent a membership."""
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='songinalbum',
        verbose_name='Song name'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='songinalbum'
    )
    number = models.IntegerField(
        verbose_name='Sequential number in the album'
    )

    class Meta:
        verbose_name = 'Membership'
        verbose_name_plural = 'Memberships'
