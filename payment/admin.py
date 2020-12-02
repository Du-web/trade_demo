from django.contrib import admin

# Register your models here.
from payment.models import User, Accout, Trade


class TradeAdmin(admin.ModelAdmin):
    list_display = ['accout', 'user', 'trade_amount', 'trade_date', 'status', 'is_exceed_200']

    def is_exceed_200(self, obj):
        if obj.trade_amount >= 200:
            return 'yes'
        elif obj.trade_amount <= 200:
            return 'no'

    def trade_amount(self, obj):
        trade_amount = obj.trade_amount

        return trade_amount + 'RMB'

    trade_amount.short_description = '交易金额'


admin.site.register(User)
admin.site.register(Accout)
admin.site.register(Trade, TradeAdmin)
