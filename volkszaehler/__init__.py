"""Wrapper for interacting with the Volkszahler API."""
import asyncio
import logging

import aiohttp
import async_timeout

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_RESOURCE = "http://{host}:{port}/middleware.php/data/{uuid}.json"


class Volkszaehler(object):
    """A class for handling the data retrieval."""

    def __init__(self, loop, session, uuid, host="localhost", port=80):
        """Initialize the connection to the API."""
        self._loop = loop
        self._session = session
        self.url = _RESOURCE.format(host=host, port=port, uuid=uuid)
        self.data = {}
        self.average = self.max = self.min = self.consumption = None
        self.tuples = []

    async def get_data(self):
        """Retrieve the data."""
        try:
            with async_timeout.timeout(5, loop=self._loop):
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
