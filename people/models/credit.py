"""Models concerning crediting URY members for the existence of data.

"""

# IF YOU'RE ADDING CLASSES TO THIS, DON'T FORGET TO ADD THEM TO
# __init__.py

from django.conf import settings
from django.db import models
from people.models import Person
from people.mixins import CreatableMixin
from people.mixins import ApprovableMixin
from lass_utils.mixins import EffectiveRangeMixin


CREDIT_TYPE_DB_TABLE = getattr(
    settings,
    'CREDIT_TYPE_DB_TABLE',
    'credit_type'
)
CREDIT_TYPE_DB_ID_COLUMN = getattr(
    settings,
    'CREDIT_DB_ID_COLUMN',
    'credit_type_id'
)


class CreditType(models.Model):
    """A type of credit, as used in ShowCredit.

    Types of show credit might include "presenter", "director",
    "reporter" and so on.

    """

    def __unicode__(self):
        return self.name

    id = models.AutoField(
        primary_key=True,
        db_column=CREDIT_TYPE_DB_ID_COLUMN
    )
    name = models.CharField(
        max_length=255,
        help_text='Human-readable, singular name for the type.')
    plural = models.CharField(
        max_length=255,
        help_text='Human readable plural for the type.')
    is_in_byline = models.BooleanField(
        default=False,
        help_text='If true, credits of this type appear in by-lines.')

    class Meta:
        ordering = ['name']
        db_table = CREDIT_TYPE_DB_TABLE
        app_label = 'people'


class Credit(ApprovableMixin,
             CreatableMixin,
             EffectiveRangeMixin):
    """Abstract base class for credit models."""
    # Don't forget to put an `id` column in when overriding!
    credit_type = models.ForeignKey(
        CreditType,
        db_column='credit_type_id',
        help_text='The type of credit the credit is assigned.')
    credit = models.ForeignKey(
        Person,
        db_column='creditid',
        help_text='The credit being credited.',
        related_name='credited_%(app_label)s_%(class)s_set')

    ## MAGIC METHODS ##

    def __unicode__(self):
        return self.credit.full_name()

    class Meta(EffectiveRangeMixin.Meta):
        ordering = ['credit']
        abstract = True
