from pathlib import Path
from typing import Optional

import pandas as pd

from core.patient_model import Patient, SignatureName

CUR_DIR = Path(__file__).resolve().parent


class PatientsTSVRepository:
    def __init__(self):
        self._df = pd.read_csv(CUR_DIR / "signatures.tsv", delimiter="\t")
        self._df.rename(columns={"Unnamed: 0": "Name"}, inplace=True)
        self._df.set_index("Name", inplace=True)

    def get_signatures_by_patient(self, name: str, signatures: list[SignatureName]) -> Optional[Patient]:
        patients = self._deserialize_patients(self._df[self._df.index == name][signatures].T.to_dict())
        if patients:
            return patients[0]
        return None

    def get_all_signatures_by_patient(self, name: str) -> Optional[Patient]:
        patients = self._deserialize_patients(self._df[self._df.index == name].T.to_dict())
        if patients:
            return patients[0]
        return None

    def get_avg_by_signature(self, signature_name: SignatureName) -> float:
        return self._df[signature_name].mean()

    @staticmethod
    def _deserialize_patients(patients: dict[str, dict[str, float]]) -> list[Patient]:
        return [
            Patient.parse_obj(
                {
                    "name": patient_name,
                    "signatures": [
                        {"name": SignatureName(signature), "value": value}
                        for signature, value in patient_signatures.items()
                    ],
                }
            )
            for patient_name, patient_signatures in patients.items()
        ]
