from django.contrib import admin
from .models import FeedBack, TartipCategory, Tartip
# Register your models here.

class TartipCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', )
    }

admin.site.register(FeedBack)
admin.site.register(TartipCategory, TartipCategoryAdmin)
admin.site.register(Tartip)
