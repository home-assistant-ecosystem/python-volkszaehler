"""Tests for volkszaehler."""

import aiohttp
import pytest

from volkszaehler import Volkszaehler
from volkszaehler.exceptions import VolkszaehlerApiConnectionError


class MockResponse:
    """A mock response for testing."""

    def __init__(self, status, json_data):
        """Initialize the mock response with a status and JSON data."""
        self.status = status
        self._json = json_data

    async def json(self):
        """Simulate the JSON response."""
        return self._json


class MockSession:
    """A mock session for testing."""

    def __init__(self, response):
        """Initialize the mock session with a response."""
        self._response = response

    async def get(self, url, timeout=None):
        """Simulate a GET request."""
        return self._response


@pytest.mark.parametrize(
    "mock_json",
    [
        {
            "data": {
                "average": 10,
                "max": [0, 20],
                "min": [0, 5],
                "consumption": 100,
                "tuples": [[0, 1], [1, 2], [2, 3]],
            }
        }
    ],
)

@pytest.mark.asyncio
async def test_get_data_success(mock_json):
    """Test successful data retrieval from Volkszaehler API."""
    mock_response = MockResponse(200, mock_json)
    mock_session = MockSession(mock_response)
    v = Volkszaehler(mock_session, uuid="abc123")
    await v.get_data()
    assert v.average == 10
    assert v.max == 20
    assert v.min == 5
    assert v.consumption == 100
    assert v.tuples == [[0, 1], [1, 2], [2, 3]]
    assert v.last == 3


@pytest.mark.asyncio
async def test_get_data_connection_error():
    """Test handling of connection errors when retrieving data from Volkszaehler API."""

    class FailingSession:
        """A session that simulates a connection error."""

        async def get(self, url, timeout=None):
            """Simulate a connection error."""
            raise aiohttp.ClientError()

    v = Volkszaehler(FailingSession(), uuid="abc123")
    with pytest.raises(VolkszaehlerApiConnectionError):
        await v.get_data()
