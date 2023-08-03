import pandera as pa
from pandera.dtypes import Category


class CellClones(pa.DataFrameModel):
    """CellClones is a DataFrame where each row contains cell type and identity
    of the clone of each cell. cell_type and clone need to be categoricals."""

    cell_type: Category
    clone: Category
