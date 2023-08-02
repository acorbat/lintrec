from lintrec.cell_clones import CellClones


class TestCellClones:
    """Test that CellClones class behaves as expected."""

    def test_has_documentation(self):
        assert CellClones.__doc__ is not None
