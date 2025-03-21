from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    description = Column(String(255))
    image_url = Column(String(255))

    def __repr__(self):
        return f"<Menu {self.name}>"
