from django.contrib import admin

from trains.models import Train


class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train
    list_display = ('name', 'from_city', 'to_city', 'travel_time')#'format_time')
    list_editable = ('travel_time',)

    # def format_time(self, obj):
    #     return obj.travel_time.strftime('%H:%M')
    # format_time.short_description = 'Travel Time'

admin.site.register(Train, TrainAdmin)