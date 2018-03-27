from django.contrib import admin
from .models import Time, Partida

class TimeAdmin(admin.ModelAdmin):
  list_display = ('nome', 'sigla')
  fields = ['nome', 'sigla']
  search_fields = ['sigla', 'nome']
  

admin.site.register(Time, TimeAdmin)
admin.site.register(Partida)
