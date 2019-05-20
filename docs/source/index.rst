.. Workshift Engine documentation master file, created by
   sphinx-quickstart on Sun Apr 14 02:27:40 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Workshift Engine's documentation!
============================================

Getting started
###############

to getting started and use this package, we must have an *'Assignation model'* with at least these attributes:

    * strating_date
    * ending_date
    * person(FK)
    * person_id
    * workshift(FK)
    * workshift_id
    * start_day

Where *'person'* and *'workshift'* are relations. Also the you'll need a *'Workshift model'* with at least this attribute:

    * total_workshift_days

This attributes is the number of days that the workshift has.

Joining assignations
####################

For join assignation we just need to do:

.. code-block:: python

    assignation1 += assignation2

This code will try to join the assignation2 into the assignation1. You don't have to worry
about check if there can be joined, if they can't, the assignation1 won't change.

Removing a range in an assignation
##################################

For removing a range of dates we just need to do:

.. code-block:: python

    from operators.assignation_operator import AssignationOperator
    from datetime import datetime

    starting_date = datetime(2019, 5, 4).date()
    ending_date = datetime(2019, 5, 6).date()

    response = AssignationOperator.remove(
        assignation1,
        starting_date,
        ending_date)

These code will try to remove the range from 2019-5-1 to 2019-5-6 into the assignation1.
The result of this method will be a *'dict'* with 3 keys:

    * delete: The assignation that must be deleted in case that the range to remove covers all the assignation.
    * update: The assignation that must be updated in case that the range to remove take a part of the assignation.
    * create: The assignation tha must be created in case that the range to remove take a part from the middle of the assignation

If in the last example our assignation is from 2019-5-1 to 2019-5-10, the response will be:

.. code-block:: python

    {
        'delete': None,
        'update': assignation1 # where the range will be from 2019-5-1 to 2019-5-3
        'create': new_assignation # where the range will be from 2019-5-7 to 2019-5-10
    }

You can see the whole AssignationOperator class with the methods in the operator section

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   operators/index
   tests/index
   mappers/index



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
