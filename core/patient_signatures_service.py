from core.patient_model import SignatureName


class PatientSignaturesService:
    def __init__(self, patients_repository):
        self._patients_repository = patients_repository

    def get_patient_signatures(self, name: str, signatures: list[SignatureName]):
        if signatures:
            return self._patients_repository.get_signatures_by_patient(name, signatures)
        return self._patients_repository.get_all_signatures_by_patient(name)

    def get_avg_by_signature(self, signature_name: SignatureName):
        return self._patients_repository.get_avg_by_signature(signature_name)
