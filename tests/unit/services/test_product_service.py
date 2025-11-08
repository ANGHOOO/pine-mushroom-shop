from datetime import datetime
from unittest.mock import AsyncMock, patch

import pytest

from src.models import Product
from src.schemas.product_schema import ProductCreate
from src.services.product_service import ProductService


@pytest.mark.asyncio
async def test_create_product(sample_product: ProductCreate, mock_db: AsyncMock):
    # given
    saved_product = Product(
        product_id=1,
        product_name="테스트 송이",
        seller="강원송이총판",
        origin="국내",
        category="선물용",
        product_price=1000,
        stock_quantity=10,
        description="test",
        created_at=datetime.now(),
    )
    product_service = ProductService(mock_db)
    # when
    with patch.object(
        product_service.product_repository,
        "create_product",
        new_callable=AsyncMock,
        return_value=saved_product,
    ):
        result = await product_service.create_product(sample_product)
    # then
    assert result.product_id == saved_product.product_id
