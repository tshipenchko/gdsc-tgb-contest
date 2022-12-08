import asyncio
import logging

from bot import cli


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(cli.run())
