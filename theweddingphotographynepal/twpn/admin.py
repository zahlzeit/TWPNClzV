from django.contrib import admin

# Register your models here.
from .models import Images, QuoteRequest, Review, Service, Vendor, Contact, MembershipForm

admin.site.register(Vendor)
admin.site.register(Review)
admin.site.register(Images)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(MembershipForm)
admin.site.register(QuoteRequest)
