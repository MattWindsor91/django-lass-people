"""
Models
======

:mod:`people` contains several models: models that define the person
database, and models that form the credit system.

.. automodule:: people.models.person
    :deprecated:
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: people.models.credit
    :deprecated:
    :members:
    :undoc-members:
    :show-inheritance:

"""

# Import all models, in an order such that models only depend on
# models further up the list
from people.models.person import Person, Creator, Approver
from people.models.credit import Credit, CreditType
