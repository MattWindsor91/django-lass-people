from people.models import Person, CreditType
from django.contrib import admin


## Person ##

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_joined')
    exclude = ('password',)


admin.site.register(Person, PersonAdmin)


## CreditType ##

admin.site.register(CreditType)
