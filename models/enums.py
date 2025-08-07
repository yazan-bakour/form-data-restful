from enum import Enum
from typing import Optional


class Title(str, Enum):
    MR = "Mr"
    MRS = "Mrs"
    MISS = "Miss"
    DR = "Dr"


class MaritalStatus(str, Enum):
    SINGLE = "Single"
    MARRIED = "Married"
    DIVORCED = "Divorced"
    WIDOWED = "Widowed"
    SEPARATED = "Separated"


class DegreeType(str, Enum):
    BACHELOR = "Bachelor's Degree"
    MASTER = "Master's Degree"
    PHD = "PhD"
    DIPLOMA = "Diploma"
    CERTIFICATE = "Certificate"
    ASSOCIATE = "Associate Degree"


class SkillLevel(str, Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    EXPERT = "Expert"


class ProficiencyLevel(str, Enum):
    BASIC = "Basic"
    CONVERSATIONAL = "Conversational"
    FLUENT = "Fluent"
    NATIVE = "Native"


class WorkType(str, Enum):
    REMOTE = "Remote"
    ONSITE = "On-site"
    HYBRID = "Hybrid"
    ANY = "Any"
