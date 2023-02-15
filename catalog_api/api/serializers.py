from catalog.models import Musician, Album, Song, Membership
from rest_framework import serializers
from django.shortcuts import get_object_or_404


class SongSerializer(serializers.ModelSerializer):
    """The SongSerializer serializer for the Song model."""

    class Meta:
        fields = ("name",)
        model = Song
    
    def create(self, validated_data):
        """
        Return complete object instances based on the validated data.
        """
        return Song.objects.create(**validated_data)
    
    def to_internal_value(self, data):
        """
        The `to_internal_value` method returns validated data.
        """
        return get_object_or_404(Song, id=data)


class MemberShipSerializer(serializers.ModelSerializer):
    """The MemberShipSerializer serializer for the MemberShip model."""
    id = SongSerializer()
    name = serializers.CharField(required=False)
    number = serializers.IntegerField()

    class Meta:
        fields = ('id', 'name', 'number')
        model = Membership
    
    def to_representation(self, instance):
        """
        The `to_representation` method returns views.
        """
        data = SongSerializer(instance.song).data
        data['number'] = instance.number
        return data


class AlbumSerializer(serializers.ModelSerializer):
    """The AlbumSerializer serializer for the Album model."""
    musician = serializers.CharField(required=False)
    songs = MemberShipSerializer(source='songinalbum', many=True)

    class Meta:
        fields = ('musician', 'year', 'songs') # ('id', 'musician', 'year', 'songs')
        model = Album
    
    def create(self, validated_data):
        """
        Return complete object instances based on the validated data.
        """
        songs = validated_data.pop('songinalbum')
        album = Album.objects.create(**validated_data)
        for song in songs:
            if song['number'] <= 0:
                raise serializers.ValidationError(
                    'Номер песни в альбоме должен быть больше 0!'
                )
            
            Membership.objects.create(
                song=song['id'],
                album=album,
                number=song['number'])
        return album



class MusicianSerializer(serializers.ModelSerializer):
    """The MusicianSerializer serializer for the Musician model."""
    albums = AlbumSerializer(many=True,)

    class Meta:
        fields = ('name', 'albums')
        model = Musician
    
    def create(self, validated_data):
        """
        Return complete object instances based on the validated data.
        """
        return Musician.objects.create(**validated_data)
