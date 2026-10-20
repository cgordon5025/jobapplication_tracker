from enum import Enum

class ApplicationStatus(Enum):
    APPLIED = "applied"
    REJECTED = "rejected"
    PHONE_SCREEN = "phone_screen"
    TECH_INTERVIEW = "tech_interview"
    INTERVIEW = "interview"