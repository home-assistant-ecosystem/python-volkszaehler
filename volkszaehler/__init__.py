"""Wrapper for interacting with the Volkszahler API."""
import asyncio
import logging

import aiohttp
import async_timeout

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_RESOURCE = "{schema}://{host}:{port}/middleware.php/data/{uuid}.json"
_RESOURCE_NO_MIDDLEWARE = "{schema}://{host}:{port}/data/{uuid}.json"
_RESOURCE_FROM = "from={param_from}"
_RESOURCE_TO = "to={param_to}"


class Volkszaehler(object):
    """A class for handling the data retrieval."""

    def __init__(
        self,
        session,
        uuid,
        host="localhost",
        port=80,
        tls=False,
        param_from="",
        param_to="",
        middleware=True,
    ):
        """Initialize the connection to the API."""
        self._session = session

        if middleware:
            self.url = _RESOURCE.format(
                schema="https" if tls else "http", host=host, port=port, uuid=uuid
            )
        else:
            self.url = _RESOURCE_NO_MIDDLEWARE.format(
                schema="https" if tls else "http", host=host, port=port, uuid=uuid
            )

        self.data = {}
        self.average = self.max = self.min = self.consumption = None
        self.tuples = []

        _PREFIX = "?"
        if param_from:
            self.url += _PREFIX + _RESOURCE_FROM.format(param_from=param_from)
            _PREFIX = "&"
        if param_to:
            self.url += _PREFIX + _RESOURCE_TO.format(param_to=param_to)

    async def get_data(self):
        """Retrieve the data."""
        try:
            with async_timeout.timeout(5):
                response = await self._session.get(self.url)

            _LOGGER.debug("Response from Volkszaehler API: %s", response.status)
            self.data = await response.json()
            _LOGGER.debug(self.data)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Can not load data from Volkszaehler API")
            self.data = None
            raise exceptions.VolkszaehlerApiConnectionError()

        self.average = self.data["data"]["average"]
        self.max = self.data["data"]["max"][1]
        self.min = self.data["data"]["min"][1]
        self.consumption = self.data["data"]["consumption"]
        self.tuples = self.data["data"]["tuples"]
        self.last = self.data["data"]["tuples"][-1][1]
