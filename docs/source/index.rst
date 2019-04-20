.. Workshift Engine documentation master file, created by
   sphinx-quickstart on Sun Apr 14 02:27:40 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Workshift Engine's documentation!
============================================

Getting started
###############

For a simple use of these library let's go by parts. First you need to create the asignation mapper.

Let assume that you assignation obj has these attr:

    * startingDate
    * endingDate
    * workshiftId
    * personId
    * startDay

We need to mapping to these names:

.. code-block:: python

    mapping = {
        'starting_date': 'startingDate',
        'ending_date': 'endingDate',
        'workshift_id': 'workshift_id,
        'person_id': 'person_id',
        'start_day': 'startDay'}

With we are ready to create our assignation mapper. Assume that you assignaton model
is called *'Assignation'*:

.. code-block:: python

    from mappers.assignation_mapper import AssignationMapper

    mapping = {
            'starting_date': 'startingDate',
            'ending_date': 'endingDate',
            'workshift_id': 'workshift_id,
            'person_id': 'person_id',
            'start_day': 'startDay'}

    my_assignation_obj = Assignation()

    assignation_mapper = AssignationMapper(my_assignation_obj, mapping)

And that's it, now we are ready to operate through this mapper

From here until the end we will call the assination mapper, just assignation.

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
