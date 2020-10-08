from django.contrib import admin
from .models import Friend
# Register your models here.


class FriendAdmin(admin.ModelAdmin):
    list_display = ('slate_id', 'first_name', 'last_name', 'grade', 'treble_grade', 'bass_grade', 'insert_barline_grade', 'major_keys', 'minor_keys')
    
admin.site.register(Friend, FriendAdmin)

# admin.site.register(Friend)
