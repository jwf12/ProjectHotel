from django.contrib import admin
from .models import *

class TillAdmin(admin.ModelAdmin):
    list_display = (
        'till_res',
        
    )


admin.site.register(Till, TillAdmin)
admin.site.register(Item_Till)
admin.site.register(Payment)

