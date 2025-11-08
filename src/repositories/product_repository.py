from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.exceptions import DatabaseError, ProductAlreadyExists, DatabaseConnectionError
from src.models import Product

import logging


logger = logging.getLogger(__name__)


class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_product(self, product: Product) -> Product:
        self.db.add(product)
        try:
            await self.db.commit()
            return product

        except IntegrityError as e:
            await self.db.rollback()
            logger.warning(f"데이터베이스 제약 조건 위배: {str(e)}")
            raise ProductAlreadyExists(e)

        except DatabaseConnectionError as e:
            await self.db.rollback()
            logger.error(f"데이터베이스 연결 오류: {str(e)}")
            raise DatabaseError(e)

        except SQLAlchemyError as e:
            await self.db.rollback()
            logger.error(f"SQLAlchemy 오류 발생: {str(e)}")
            raise DatabaseError(e)

        except Exception as e:
            logger.error(f"상품 등록 중 알 수 없는 오류 발생: {str(e)}")
            raise e
