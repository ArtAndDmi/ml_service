from enum import StrEnum


class JobStatus(StrEnum):
    CREATED = 'created'
    RUNNING = 'running'
    COMPLETED = 'completed'
    REJECTED = 'rejected'
    FAILED = 'failed'
