Collisions
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

Where *'person'* and *'workshift'* are relations. Also you'll need a *'WorkShift model'* with at least this attribute:

    * **total_workshift_days:** the number of days that a workshift cycle lasts

This attribute only will be used when the *start_day* attribute has a value(*not None*). Otherwise is must be setted as *None*.

An this methods:

    * **get_days():** Get a list of the days

Services
########

.. toctree::
    :maxdepth: 1

    services/index
    services/cycle_and_week


