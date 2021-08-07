from fastapi_utils.enums import StrEnum
from pydantic import BaseModel


class SignatureName(StrEnum):
    mhci = "MHCI"
    mhcii = "MHCII"
    coactivation_molecules = "Coactivation_molecules"
    effector_cells = "Effector_cells"
    t_cell_traffic = "T_cell_traffic"
    nk_cells = "NK_cells"
    t_cells = "T_cells"
    b_cells = "B_cells"
    m1_signatures = "M1_signatures"
    th1_signature = "Th1_signature"
    antitumor_cytokines = "Antitumor_cytokines"
    checkpoint_inhibition = "Checkpoint_inhibition"
    treg = "Treg"
    t_reg_traffic = "T_reg_traffic"
    neutrophil_signature = "Neutrophil_signature"
    granulocyte_traffic = "Granulocyte_traffic"
    mdcs = "MDSC"
    mdcs_traffic = "MDSC_traffic"
    macrophages = "Macrophages"
    macrophage_DC_traffic = "Macrophage_DC_traffic"
    th2_signature = "Th2_signature"
    protumor_cytokines = "Protumor_cytokines"
    caf = "CAF"
    matrix = "Matrix"
    matrix_remodeling = "Matrix_remodeling"
    angiogenesis = "Angiogenesis"
    endothelium = "Endothelium"
    proliferation_rate = "Proliferation_rate"
    emt_signature = "EMT_signature"


class Signature(BaseModel):
    name: SignatureName
    value: float


class Patient(BaseModel):
    name: str
    signatures: list[Signature]
