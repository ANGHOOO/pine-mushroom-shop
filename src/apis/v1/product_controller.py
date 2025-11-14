from fastapi import APIRouter, Depends, status, HTTPException

from src.core.logging_config import logger
from src.errors.exceptions import ProductAlreadyExists
from src.models.product_schema import ProductCreate, ProductResponse
from src.services.product_service import ProductService

router = APIRouter(prefix="/product", tags=["product"])


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    product_service: ProductService = Depends(ProductService),
) -> ProductResponse:
    try:
        created_product = await product_service.create_product(product)
    except ProductAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="이미 등록된 상품입니다."
        )
    logger.info(f"상품 등록에 성공하였습니다. 상품ID: {created_product.product_id}")
    return ProductResponse.model_validate(created_product)
