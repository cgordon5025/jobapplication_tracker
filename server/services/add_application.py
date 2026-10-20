import uuid
from sqlalchemy.orm import Session

from models.application_model import ApplicationModel
from models.application_status_enum import ApplicationStatus
from datetime import datetime, date

def add_application(
    db:Session,  ##similar to c-sharp's ApplicationDB Context,
    companyName: str,
    website: str|None,
    status: ApplicationStatus = ApplicationStatus.APPLIED
):
    application = ApplicationModel(
        companyName = companyName,
        website = website,
        status = status,
        lastUpdated = date.today()
    )
    db.add(application)
    db.commit()
    db.refresh(application)