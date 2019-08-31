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

Where *'person'* and *'workshift'* are relations. Also you'll need a *'Workshift model'* with at least this attribute:

    * total_workshift_days

This attributes is the number of days that the workshift has.

Use it
####################

First, we need to create a RAM database with all the assignation proxies. To do that we need to:

.. code-block:: python

    from proxies.proxy_factory import ProxyFactory
    from database.assignation_db import AssignationDB

    assignations = MyAssignationModel.objects.all()

    assignation_proxies = ProxyFactory.create_multiple_assignation_proxies(assignation)
    assignation_db = AssignationDB(assignation_proxies, None)

This code wil create a databse with all the assignations. From here, we can use this class
to assignate and unassign assignation like this. For assignate:

.. code-block:: python

    data = {
        'starting_date': datetime(2019, 1, 23).date(),
        'ending_date': datetime(2019, 1, 28).date(),
        'workshift_id': 4,
        'person_id': 1,
        'start_day': None}

    new_assignation = MyAssignationModel(**data)
    new_assignation_proxy = ProxyFactory.create_assignation_proxy(new_assignation)
    assignation_db.assignate(new_assignation_proxy)

For unassign:

.. code-block:: python

    data = {
        'starting_date': datetime(2019, 1, 23).date(),
        'ending_date': datetime(2019, 1, 28).date(),
        'workshift_id': 4,
        'person_id': 1,
        'start_day': None}

    fake_assignation = MyAssignationModel(**data)
    fake_assignation_proxy = ProxyFactory.create_assignation_proxy(fake_assignation)
    assignation_db.unassign(fake_assignation_proxy)

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   operators/index
   tests/index
   proxies/index



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
