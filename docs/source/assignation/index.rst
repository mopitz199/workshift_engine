Assignations
============

First, we need to create a RAM database with all the assignation proxies. To do that we need to:

.. code-block:: python

    from proxies.proxy_factory import ProxyFactory
    from database.assignation_db import AssignationDB

    assignations = MyAssignationModel.objects.all()

    assignation_proxies = ProxyFactory.create_multiple_assignation_proxies(assignation)
    assignation_db = AssignationDB(assignation_proxies, None)

This code wil create a database with all the assignations. From here, we can use this class
to assign and unassign. For assignate:

.. code-block:: python

    new_assignation = MyAssignationModel(**data)
    new_assignation_proxy = ProxyFactory.create_assignation_proxy(new_assignation)
    assignation_db.assignate(new_assignation_proxy)

For unassign:

.. code-block:: python

    fake_assignation = MyAssignationModel(**data)
    fake_assignation_proxy = ProxyFactory.create_assignation_proxy(fake_assignation)
    assignation_db.unassign(fake_assignation_proxy)

The *'starting_day'* must be setted with the correct value according to the *'starting_date'*.

Finally after all your assign and unassign, you can get the difference between the begining state
of assignations and the current one. This is in order to check collisions. Something that
will discuss later.

To do that, just do:

.. code-block:: python

    from operators.differences_operator import DifferencesOperator
    differences_operator = DifferencesOperator(assignation_db)
    resp = differences_operator.process_differences()

To check each classes and elements of this process you can see our deep documentation below

.. toctree::
   :maxdepth: 1

   operators/index
   tests/index
   proxies/index