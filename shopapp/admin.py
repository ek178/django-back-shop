from django.contrib import admin
from .models import Product,Department,Profile,Order,DeliveryDetail,OrderProduct,Review,Profile2

admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(DeliveryDetail)
# admin.site.register(OrderProduct)
# admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Profile2)


class OrderProductInline(admin.TabularInline):
    model = OrderProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]