from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.exceptions import ProductAlreadyExists
from src.schemas.product_schema import ProductCreate, ProductResponse
from src.services.product_service import ProductService

import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/product", tags=["product"])


def get_product_service(db: AsyncSession = Depends(get_db)) -> ProductService:
    return ProductService(db)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    product_service: ProductService = Depends(get_product_service),
):
    try:
        created_product = await product_service.create_product(product)
        logger.info(f"상품 등록에 성공하였습니다. 상품ID: {created_product.product_id}")
        return ProductResponse(**created_product.dict())

    except ProductAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="이미 등록된 상품입니다."
        )

    except Exception as e:
        logger.error(f"상품 등록 중 알 수 없는 오류가 발생했습니다. {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="죄송합니다. 서버 내부에서 오류가 발생했습니다. 다시 시도해주세요.",
        )
