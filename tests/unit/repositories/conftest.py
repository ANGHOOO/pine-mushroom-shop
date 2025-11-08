import pytest

from src.models import Product


@pytest.fixture
def sample_product() -> Product:
    return Product(
        product_id=1,
        product_name="테스트 송이",
        seller="강원송이총판",
        origin="국내",
        category="선물용",
        product_price=1000,
        stock_quantity=10,
        description="test",
    )
