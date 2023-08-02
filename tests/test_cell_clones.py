import pytest
import pandas as pd

from pandera.errors import SchemaError
from lintrec.cell_clones import CellClones


class TestCellClones:
    """Test that CellClones class behaves as expected."""

    def test_has_documentation(self):
        assert CellClones.__doc__ is not None

    def test_df_with_wrong_column(self):
        with pytest.raises(SchemaError):
            df = pd.DataFrame(
                [["a", "1"], ["a", "2"], ["b", "2"]],
                columns=["cell_type", "cla"],
            )
            CellClones(df)

    def test_df_missing_column(self):
        with pytest.raises(SchemaError):
            df = pd.DataFrame(["a", "a", "b"], columns=["cell_type"])
            CellClones(df)

    def test_ok_df(self):
        df = pd.DataFrame(
            [["a", "1"], ["a", "2"], ["b", "2"]], columns=["cell_type", "clone"]
        )
        CellClones(df)
