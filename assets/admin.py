from django.contrib import admin
from .models import Portfolio, Sector, Asset, Trade, PortfolioComp, Operation

# Register your models here.

class TradeAdmin(admin.ModelAdmin):
    list_display = ("id", "ticker", "date", "quantity", "price", "tax", "operator")

class PortfolioCompAdmin(admin.ModelAdmin):
    list_display = ("id", "portfolio", "asset", "percentage")

admin.site.register(Portfolio)
admin.site.register(Sector)
admin.site.register(Asset)
admin.site.register(Trade, TradeAdmin)
admin.site.register(PortfolioComp, PortfolioCompAdmin)
admin.site.register(Operation)

