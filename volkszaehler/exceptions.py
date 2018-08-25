"""
Copyright (c) 2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""


class VolkszaehlerError(Exception):
    """General Volkszaehler Error exception occurred."""

    pass


class VolkszaehlerApiConnectionError(VolkszaehlerError):
    """When a connection error is encountered."""

    pass


class VolkszaehlerNoDataAvailable(VolkszaehlerError):
    """When no data is available."""

    pass
