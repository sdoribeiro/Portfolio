from django.contrib import admin
from .models import Portfolio, Sector, Asset, Trade, PorfolioComp

# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Sector)
admin.site.register(Asset)
admin.site.register(Trade)
admin.site.register(PorfolioComp)
