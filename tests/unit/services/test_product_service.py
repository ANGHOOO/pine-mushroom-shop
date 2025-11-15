from unittest.mock import AsyncMock

import pytest
from fastapi_pagination.cursor import CursorParams, CursorPage

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


@pytest.mark.asyncio
async def test_get_products(
    sample_cursor_params: CursorParams, sample_read_product: CursorPage[Product]
):
    # given
    mock_repository = AsyncMock(spec=ProductRepository)
    mock_repository.get_products = AsyncMock(return_value=sample_read_product)
    product_service = ProductService(product_repository=mock_repository)

    # when
    result = await product_service.get_products(sample_cursor_params)

    # then
    mock_repository.get_products.assert_called_once_with(sample_cursor_params)
    assert result == sample_read_product
