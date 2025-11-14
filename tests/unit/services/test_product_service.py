from unittest.mock import AsyncMock

import pytest

from src.db import Product
from src.models.product_schema import ProductCreate
from src.repositories.product_repository import ProductRepository
from src.services.product_service import ProductService


@pytest.mark.asyncio
async def test_create_product(sample_product: ProductCreate, saved_product: Product):
    # given
    mock_repository = AsyncMock(spec=ProductRepository)
    mock_repository.create_product = AsyncMock(return_value=saved_product)
    product_service = ProductService(product_repository=mock_repository)

    # when
    result = await product_service.create_product(sample_product)

    # then
    mock_repository.create_product.assert_called_once_with(sample_product)
    assert result == saved_product
