"""user model"""

from sqlalchemy import Boolean, Column, Integer, String
# from sqlalchemy.orm import relationship

from app.infrastructure.database import Base


class UserModel(Base):
    """user model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, )
    hashed_password = Column(String, )
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")
