from django.contrib import admin
from FP_App.models import Contact,Contact_details 

class ContactAdmin(admin.ModelAdmin):
    list_display=['full_name','email','subject','message','ph','country']

 

class Contact_detailsAdmin(admin.ModelAdmin):
    list_display=['full_name','email','company_name','phone_number','subject','message','service_interested_in','budget']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Contact_details,Contact_detailsAdmin)


