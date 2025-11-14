import pytest

from src.models.product_schema import ProductCreate, ProductStatus, ProductCategory


@pytest.fixture
def sample_product() -> ProductCreate:
    return ProductCreate(
        product_name="테스트 송이",
        seller="강원송이총판",
        origin="국내",
        category=ProductCategory.GIFT,
        product_status=ProductStatus.SOLD_OUT,
        product_price=1000,
        stock_quantity=10,
        description="test",
    )
