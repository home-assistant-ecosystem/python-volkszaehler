"""Sample code to use the wrapper for interacting with the Volkszaehler API."""

import asyncio

import aiohttp

from volkszaehler import Volkszaehler, VolkszaehlerEntitiesClient

HOST = "demo.volkszaehler.org"
UUID = "57acbef0-88a9-11e4-934f-6b0f9ecd95a8"


async def main():
    """The main part of the example script."""
    async with aiohttp.ClientSession() as session:
        entitiesClient = VolkszaehlerEntitiesClient(
            session, host=HOST, port=443, tls=True
        )
        await entitiesClient.get_entities()
        print("Entity Title:", entitiesClient.entities[0]["title"])

        zaehler = Volkszaehler(session, UUID, host=HOST, port=443, tls=True)

        # Get the data
        await zaehler.get_data()

        print("Average:", zaehler.average)
        print("Max:", zaehler.max)
        print("Min:", zaehler.min)
        print("Consumption:", zaehler.consumption)
        print("Data tuples:", zaehler.tuples)
        print("Last:", zaehler.last)


if __name__ == "__main__":
    asyncio.run(main())
