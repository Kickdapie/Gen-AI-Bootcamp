import pytest
from unittest.mock import AsyncMock

from kafka_consumer import consume_todos

@pytest.mark.asyncio
async def test_consume_todos():
    consumer = AsyncMock(AIOKafkaConsumer)
    session_factory = AsyncMock(return_value=AsyncMock())

    await consume_todos(consumer, "bootstrap_servers", "topic", session_factory)

    consumer.start.assert_called_once()
    consumer.stop.assert_called_once()
    session_factory.assert_called_once()