from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    mobile = Column(String(15), nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String(50), default="Pending")

    def __repr__(self):
        return f"<Order {self.id} - {self.status}>"
