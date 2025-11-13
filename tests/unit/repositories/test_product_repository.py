from unittest.mock import AsyncMock, ANY, MagicMock

import pytest

from src.db import Product
from src.models.product_schema import ProductCreate
from src.repositories.product_repository import ProductRepository


@pytest.mark.asyncio
async def test_create_product_success(sample_product: ProductCreate):
    # given
    mock_db = AsyncMock()
    mock_db.add = MagicMock()
    mock_db.commit = AsyncMock()
    mock_repository = ProductRepository(mock_db)

    # when
    created_product = await mock_repository.create_product(sample_product)

    # then
    mock_db.add.assert_called_once_with(ANY)
    product = mock_db.add.call_args.args[0]
    assert isinstance(product, Product)

    assert isinstance(created_product, Product)

    mock_db.commit.assert_called_once_with()
