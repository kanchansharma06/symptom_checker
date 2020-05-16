from django.contrib import admin
from .models import log, contact
from .models import registeration,meddata,body_data1,body_loc1,sub_body1


admin.site.register(log)
admin.site.register(registeration)

admin.site.register(contact)


admin.site.register(meddata)
admin.site.register(body_data1)
admin.site.register(body_loc1)
admin.site.register(sub_body1)
# Register your models here.
