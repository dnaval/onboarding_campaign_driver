from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    source = Column(String, nullable=False)

    drivers = relationship("Driver", back_populates="campaign")


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    license_number = Column(String, nullable=False)
    license_state = Column(String, nullable=False)

    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    campaign = relationship("Campaign", back_populates="drivers")
    vehicles = relationship("Vehicle", back_populates="driver")


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"))

    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    insurance_policy_number = Column(String, nullable=False)
    insurance_expiry_date = Column(Date, nullable=False)

    driver = relationship("Driver", back_populates="vehicles")