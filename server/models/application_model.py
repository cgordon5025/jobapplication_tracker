from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Enum as SQLAlchemyEnum

from database import Base;
import uuid

from models.application_status_enum import ApplicationStatus


class ApplicationModel(Base):
    __tablename__ = "application"

    id: Mapped[uuid.uuid4()] = mapped_column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    companyName: Mapped[str] = mapped_column(String, nullable=False)
    website: Mapped[str|None] = mapped_column(String, nullable=True)
    status: Mapped[ApplicationStatus] = mapped_column(SQLAlchemyEnum(ApplicationStatus),
    nullable=False,
    default = ApplicationStatus.APPLIED)