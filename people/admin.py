from people.models import Person, CreditType
from django.contrib import admin


## Person ##

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_joined')
    exclude = ('password',)


def register(site):
    """
    Registers hooks into the given admin site for the people system
    models.

    """
    site.register(Person, PersonAdmin)
    site.register(CreditType)
