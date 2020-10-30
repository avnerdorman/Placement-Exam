import io
from django.contrib import admin
from .models import Friend
# Register your models here.


class FriendAdmin(admin.ModelAdmin):
    admin.site.disable_action('delete_selected')
    actions = ['download_csv']
    list_display = ('slate_id', 'first_name', 'last_name', 'grade', 'treble_grade', 'bass_grade', 'insert_barline_grade', 'major_keys', 'minor_keys')

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        f = io.StringIO()
        writer = csv.writer(f)
        writer.writerow(['slate_id', 'first_name', 'last_name', 'grade', 'treble_grade', 'bass_grade', 'insert_barline_grade', 'major_keys', 'minor_keys'])

        for s in queryset:
            writer.writerow([s.slate_id, s.first_name, s.last_name, s.grade, s.treble_grade, s.bass_grade, s.insert_barline_grade, s.major_keys, s.minor_keys])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

admin.site.register(Friend, FriendAdmin)

# admin.site.register(Friend)
