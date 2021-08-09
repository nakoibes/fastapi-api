from typing import Optional

from fastapi import APIRouter, Query, HTTPException

from core.patient_model import Patient, SignatureName
from core.patients_repository import PatientsTSVRepository
from core.patient_signatures_service import PatientSignaturesService

router = APIRouter()
patient_signatures_service = PatientSignaturesService(PatientsTSVRepository())


@router.get("/patient", response_model=Patient)
def get_patient_signatures(name: str, metrics: Optional[list[SignatureName]] = Query(None)):
    patient = patient_signatures_service.get_patient_signatures(name, metrics)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.get("/average")
def get_average_signature_value(signature_name: SignatureName):
    value = patient_signatures_service.get_avg_by_signature(signature_name)
    return {"avg": value}
