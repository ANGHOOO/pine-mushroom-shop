from unittest.mock import AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture(scope="function")
def mock_db() -> AsyncMock:
    return AsyncMock(spec=AsyncSession)
