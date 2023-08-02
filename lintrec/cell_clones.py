import pandera as pa


class CellClones(pa.DataFrameModel):
    cell_type: str
    clone: str
