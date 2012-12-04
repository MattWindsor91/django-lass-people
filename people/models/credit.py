"""
credit
------

:mod:`people.models.credit` contains models concerning crediting
people for having performed roles with regards to other models.

"""

from django.conf import settings
from django.db import models

from people.models import Person
from people.mixins import CreatableMixin
from people.mixins import ApprovableMixin

from lass_utils.mixins import AttachableMixin
from lass_utils.mixins import EffectiveRangeMixin


class CreditType(models.Model):
    """
    A type of credit.

    Types of show credit might include "presenter", "director",
    "reporter" and so on.

    This is not yet a subclass of :doc:`lass_utils.models.Type` but
    this may change in a future API-breaking update.

    """

    def __unicode__(self):
        return self.name

    if hasattr(settings, 'CREDIT_TYPE_DB_ID_COLUMN'):
        id = models.AutoField(
            primary_key=True,
            db_column=settings.CREDIT_TYPE_DB_ID_COLUMN
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
        """
        Metadata for the :class:`CreditType` model.

        """
        ordering = ['name']
        app_label = 'people'
        if hasattr(settings, 'CREDIT_TYPE_DB_TABLE'):
            db_table = settings.CREDIT_TYPE_DB_TABLE


class Credit(ApprovableMixin,
             AttachableMixin,
             CreatableMixin,
             EffectiveRangeMixin):
    """Abstract base class for credit models."""
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
