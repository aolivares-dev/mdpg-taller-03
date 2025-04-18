from enum import Enum

class ResponseMessage(str, Enum):
    CREATED = "Medical examination created successfully"
    UPDATED = "Medical examination updated successfully"
    DELETED = "Medical examination deleted successfully"
    NOT_FOUND = "Medical examination not found"
    ERROR_CREATE = "An error occurred while creating the medical examination. Please try again."
    ERROR_UPDATE = "An error occurred while updating the medical examination. Please try again."
    ERROR_DELETE = "An error occurred while deleting the medical examination. Please try again."
    SPECIALTY_CREATED = "Specialty created successfully"
    SPECIALTY_UPDATED = "Specialty updated successfully"
    SPECIALTY_DELETED = "Specialty deleted successfully"
    SPECIALTY_NOT_FOUND = "Specialty not found"
    ERROR_CREATE_SPECIALTY = "An error occurred while creating the specialty. Please try again."
    ERROR_UPDATE_SPECIALTY = "An error occurred while updating the specialty. Please try again."
    ERROR_DELETE_SPECIALTY = "An error occurred while deleting the specialty. Please try again."
