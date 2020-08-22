python-volkszaehler
===================

Python API for interacting with `Volkszaehler <https://volkszaehler.org>`_. At
the moment only the consumption of data is supported. Sorry, uploading is not
possible.

This module is not official, developed, supported or endorsed by Volkzaehler.

Installation
------------

The module is available from the `Python Package Index <https://pypi.python.org/pypi>`_.

.. code:: bash

    $ pip3 install volkszaehler

On a Fedora-based system or a CentOS/RHEL host with EPEL.

.. code:: bash

    $ sudo dnf -y install python3-volkszaehler

Usage
-----

The file ``example.py`` contains an example about how to use this module.

Basically it's just a wrapper to get the JSON data from a given UUID which
represents the device.

.. code:: bash

   $ http https://demo.volkszaehler.org/middleware.php/data/57acbef0-88a9-11e4-934f-6b0f9ecd95a8.json
   [...]
   {
       "data": {
           "average": 0.01,
           "consumption": 38.099,
           "from": 1584390593336,
           "max": [
               1597701600000,
               0.01
           ],
           "min": [
               1597701600000,
               0.01
           ],
           "rows": 3,
           "to": 1598106085887,
           "tuples": [
               [
                   1597701600000,
                   0.01,
                   1
               ],
               [
                   1598106085887,
                   0.01,
                   1
               ]
           ],
           "uuid": "57acbef0-88a9-11e4-934f-6b0f9ecd95a8"
       },
       "version": "0.3"
   }

Development
-----------

For development is recommended to use a ``venv``.

.. code:: bash

    $ python3 -m venv .
    $ source bin/activate
    $ python3 setup.py develop

License
-------

``python-volkszaehler`` is licensed under MIT, for more details check LICENSE.
