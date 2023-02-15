from django.contrib import admin

from catalog.models import Album, Membership, Musician, Song


class MembershipInline(admin.TabularInline):
    """
    Класс IngredientInRecipeInline позволяет редактировать
    модель IngredientInRecipe на той же странице, что и модель Recipe.
    """
    model = Membership
    extra = 1


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    """
    MembershipAdmin class for editing
    Membership models in the admin zone interface.
    """
    list_display = ('number', 'song', 'album')
    list_display_links = ('album',)
    list_filter = ('album', 'song')
    search_fields = ('song__name',)


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    """
    MusicianAdmin class for editing
    Musician models in the admin zone interface.
    """
    list_display = ('name',)
    search_fields = ('name__istartswith', 'name__contains')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """
    SongAdmin class for editing
    Song models in the admin zone interface.
    """
    list_display = ('name',)
    search_fields = ('name__istartswith', 'name__contains')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """
    AlbumAdmin class for editing
    Album models in the admin zone interface.
    """
    inlines = (MembershipInline,)
    list_display = ('musician', 'year')
    list_filter = ('musician', 'year')
    search_fields = ('year', 'musician__name')
