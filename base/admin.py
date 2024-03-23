from django.contrib import admin
from base.models import Product, Notification, UserProduct
from image_uploader_widget.widgets import ImageUploaderWidget
from django.db import models

admin.site.site_header = 'Medmate'

@admin.register(UserProduct)
class UserProductAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'product', 'updated_on')
    list_filter = ('user__username', 'product', 'updated_on')

    def get_username(self, obj):
        return obj.user.username  # Access the username through the user field

    get_username.short_description = 'User'  # Customize the column header
@admin.register(Notification)
class Notification(admin.ModelAdmin):
    list_display = ('user', 'notify_time', 'tablet_name', 'quantity', 'total_tablet_quantity', 'last_updated_time')
    list_filter = ('user', 'notify_time', 'tablet_name', 'quantity', 'total_tablet_quantity', 'last_updated_time')


@admin.register(Product)
class Product(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }
    list_display = ('product_name', 'price', 'last_added_date')
    list_filter = ('price', 'last_added_date')

# Register your models here.
