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

Usage
-----

The file ``example.py`` contains an example about how to use this module.

Basically it's just a wrapper to get the JSON data from a given UUID which
represents the device.

.. code:: bash

    $ curl http://demo.volkszaehler.org/middleware.php/data/57acbef0-88a9-11e4-934f-6b0f9ecd95a8.json
    {
       "version":"0.3",
       "data":{
          "tuples":[
             [
                1521193871692,
                0.18,
                1
             ]
          ],
          "uuid":"57acbef0-88a9-11e4-934f-6b0f9ecd95a8",
          "from":1521193871682,
          "to":1521193871692,
          "min":[
             1521193871692,
             0.18
          ],
          "max":[
             1521193871692,
             0.18
          ],
          "average":0.18,
          "consumption":0,
          "rows":2
       }
    }

Development
-----------

For development is recommended to use a ``venv``.

.. code:: bash

    $ python3.6 -m venv .
    $ source bin/activate
    $ python3 setup.py develop

License
-------

``python-volkszaehler`` is licensed under MIT, for more details check LICENSE.
