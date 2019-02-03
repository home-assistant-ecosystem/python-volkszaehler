"""Exceptions for wrapper to interact with the Volkszahler API."""


class VolkszaehlerError(Exception):
    """General Volkszaehler Error exception occurred."""

    pass


class VolkszaehlerApiConnectionError(VolkszaehlerError):
    """When a connection error is encountered."""

    pass


class VolkszaehlerNoDataAvailable(VolkszaehlerError):
    """When no data is available."""

    pass
