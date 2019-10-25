Cycle and Weekly
============================================

This services helps you to check any collision and get their detail between a cycle assignation and a weekly assignation.

How to use it
-------------

.. code-block:: python

    from proxies.proxy_factory import ProxyFactory
    from collision.services import cycle_and_weekly_collision

    cycle_assignation = ProxyFactory.create_assignation_proxy(assignation1)
    weekly_assignation = ProxyFactory.create_assignation_proxy(assignation2)

    has_collision, collision_detail = cycle_and_weekly_collision(
        cycle_assignation,
        weekly_assignation,
        detail=True)

    if has_collision:
        # show collisions (collision_detail)


If you just need to know if there's a collision instead of also get the detail, just
ignore the *detail* parameter:

.. code-block:: python

    has_collision, collision_detail = cycle_and_weekly_collision(
        cycle_assignation,
        weekly_assignation)

    # collision_detail will be None   

**This setting can be much faster**


.. autofunction:: collisions.services.cycle_and_weekly_collision