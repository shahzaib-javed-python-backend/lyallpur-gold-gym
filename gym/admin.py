from django.contrib import admin

from .models import Enquiry, Equipment, GymPlan, Member

admin.site.register(Enquiry)
admin.site.register(GymPlan)
admin.site.register(Equipment)
admin.site.register(Member)
