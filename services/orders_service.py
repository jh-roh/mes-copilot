from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import Order

class OrderRepository:
    """
    주문(Order) 영속성 작업을 위한 저장소 클래스입니다.
    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체입니다.
    Methods:
        create(order_name: str, product_code: str) -> Order:
            새로운 주문을 생성하여 데이터베이스에 저장합니다.
            Args:
                order_name (str): 주문 이름.
                product_code (str): 제품 코드.
            Returns:
                Order: 생성된 주문 객체.
            Raises:
                SQLAlchemyError: 데이터베이스 작업 중 오류 발생 시.
        get_by_id(order_id: int) -> Optional[Order]:
            주문 ID로 주문을 조회합니다.
            Args:
                order_id (int): 주문의 고유 ID.
            Returns:
                Optional[Order]: 조회된 주문 객체 또는 None.
        get_all() -> List[Order]:
            모든 주문 목록을 조회합니다.
            Returns:
                List[Order]: 주문 객체 리스트.
        update(order_id: int, order_name: Optional[str] = None, product_code: Optional[str] = None) -> Optional[Order]:
            주문 정보를 수정합니다.
            Args:
                order_id (int): 수정할 주문의 ID.
                order_name (Optional[str]): 변경할 주문 이름.
                product_code (Optional[str]): 변경할 제품 코드.
            Returns:
                Optional[Order]: 수정된 주문 객체 또는 None.
            Raises:
                SQLAlchemyError: 데이터베이스 작업 중 오류 발생 시.
        delete(order_id: int) -> bool:
            주문을 삭제합니다.
            Args:
                order_id (int): 삭제할 주문의 ID.
            Returns:
                bool: 삭제 성공 여부.
            Raises:
                SQLAlchemyError: 데이터베이스 작업 중 오류 발생 시.
    """
    """Repository for Order persistence operations"""
    def __init__(self, db: Session):
        self.db = db

    def create(self, order_name: str, product_code: str) -> Order:
        order = Order(order_name=order_name, product_code=product_code)
        try:
            self.db.add(order)
            self.db.commit()
            self.db.refresh(order)
            return order
        except SQLAlchemyError:
            self.db.rollback()
            raise

    def get_by_id(self, order_id: int) -> Optional[Order]:
        return self.db.query(Order).filter(Order.id == order_id).first()

    def get_all(self) -> List[Order]:
        return self.db.query(Order).all()

    def update(self, order_id: int, order_name: Optional[str] = None, 
              product_code: Optional[str] = None) -> Optional[Order]:
        order = self.get_by_id(order_id)
        if not order:
            return None
        try:
            if order_name is not None:
                order.order_name = order_name
            if product_code is not None:
                order.product_code = product_code
            self.db.commit()
            self.db.refresh(order)
            return order
        except SQLAlchemyError:
            self.db.rollback()
            raise

    def delete(self, order_id: int) -> bool:
        order = self.get_by_id(order_id)
        if not order:
            return False
        try:
            self.db.delete(order)
            self.db.commit()
            return True
        except SQLAlchemyError:
            self.db.rollback()
            raise

# Service functions
def create_order(db: Session, order_name: str, product_code: str) -> Order:
    repo = OrderRepository(db)
    return repo.create(order_name, product_code)

def get_order(db: Session, order_id: int) -> Optional[Order]:
    repo = OrderRepository(db)
    return repo.get_by_id(order_id)

def get_all_orders(db: Session) -> List[Order]:
    repo = OrderRepository(db)
    return repo.get_all()

def update_order(db: Session, order_id: int, 
                order_name: Optional[str] = None,
                product_code: Optional[str] = None) -> Optional[Order]:
    repo = OrderRepository(db)
    return repo.update(order_id, order_name, product_code)

def delete_order(db: Session, order_id: int) -> bool:
    repo = OrderRepository(db)
    return repo.delete(order_id)