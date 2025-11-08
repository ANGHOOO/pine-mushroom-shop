from unittest.mock import AsyncMock

import pytest

from src.models import Product
from src.repositories.product_repository import ProductRepository


@pytest.mark.asyncio
async def test_create_product_success(sample_product: Product, mock_db: AsyncMock):
    # given
    mock_db.commit = AsyncMock()
    product_repository = ProductRepository(mock_db)
    # when
    created_product = await product_repository.create_product(sample_product)
    # then
    assert created_product.product_id == 1
    assert created_product.product_name == sample_product.product_name
    assert created_product.stock_quantity == sample_product.stock_quantity

    mock_db.commit.assert_called_once()
