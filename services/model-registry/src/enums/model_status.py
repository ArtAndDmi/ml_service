from enum import StrEnum


class ModelStatus(StrEnum):
    REGISTERED = 'registered'
    PRODUCTION = 'production'
    ARCHIVED = 'archived'
    REJECTED = 'rejected'
    ACTIVATED = 'activated'
