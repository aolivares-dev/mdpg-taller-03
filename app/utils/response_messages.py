from enum import Enum

class ResponseMessage(str, Enum):
    CREATED = "Examen médico creado exitosamente"
    UPDATED = "Examen médico actualizado exitosamente"
    DELETED = "Examen médico eliminado exitosamente"
    NOT_FOUND = "Examen médico no encontrado"
    ERROR_CREATE = "Ocurrió un error al crear el examen médico. Por favor, intenta nuevamente."
    ERROR_UPDATE = "Ocurrió un error al actualizar el examen médico. Por favor, intenta nuevamente."
    ERROR_DELETE = "Ocurrió un error al eliminar el examen médico. Por favor, intenta nuevamente."
    
    SPECIALTY_CREATED = "Especialidad creada exitosamente"
    SPECIALTY_UPDATED = "Especialidad actualizada exitosamente"
    SPECIALTY_DELETED = "Especialidad eliminada exitosamente"
    SPECIALTY_NOT_FOUND = "Especialidad no encontrada"
    ERROR_CREATE_SPECIALTY = "Ocurrió un error al crear la especialidad. Por favor, intenta nuevamente."
    ERROR_UPDATE_SPECIALTY = "Ocurrió un error al actualizar la especialidad. Por favor, intenta nuevamente."
    ERROR_DELETE_SPECIALTY = "Ocurrió un error al eliminar la especialidad. Por favor, intenta nuevamente."

