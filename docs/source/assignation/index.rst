Assignations
============================================

Getting started
###############

to getting started and use this package, we must have an *'Assignation model'* with at least these attributes:

    * **starting_date:** the date where your assignation starts
    * **ending_date:** the date where your assignation ends
    * **person(FK):** the person realted to this assignation
    * **person_id:** the person_id related to this assignation
    * **workshift(FK):** the workshift related to this assignation
    * **workshift_id:** the workshift_id related to this assignation
    * **start_day:** is an offset, is the number from where the assignation is valid

Where *'person'* and *'workshift'* are relations. Also you'll need a *'Workshift model'* with at least this attribute:

    * **total_workshift_days:** the number of days that a workshift cycle lasts

This attribute only will be used when the *start_day* attribute has a value(*not None*). Otherwise is must be setted as *None*.

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

The *'start_day'* must be setted with the correct value according to the *'starting_date'*.

Finally after all your assign and unassign, you can get the difference between the begining state
of assignations and the current one. This is in order to check collisions. Something that
will discuss later

To do that, just do:

.. code-block:: python

    from operators.differences_operator import DifferencesOperator
    differences_operator = DifferencesOperator(assignation_db)
    resp = differences_operator.process_differences()

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   operators/index
   tests/index
   proxies/index