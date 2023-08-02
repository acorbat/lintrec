import pandera as pa


class CellClones(pa.DataFrameModel):
    """CellClones is a DataFrame where each row contains cell type and identity
    of the clone of each cell."""

    cell_type: str
    clone: str
