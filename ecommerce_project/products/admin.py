from django.contrib import admin
from .models import Product, Review

class ProductAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.is_authenticated:
            return False
        # return False
            

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_authenticated:
            return False
        # return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_authenticated:
            return False
        # return False

    def has_view_permission(self, request, obj=None):
        return True 


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
