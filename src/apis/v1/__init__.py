from fastapi import APIRouter

from .product_controller import router as product_router

router = APIRouter(prefix="/v1")

router.include_router(product_router)
