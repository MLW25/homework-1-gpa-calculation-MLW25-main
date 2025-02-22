import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch

@pytest.mark.parametrize(
    "test_input, expected_output",
    [ 
        (iter(["A", "B", "B", "A", ""]), "3.5"),
        (iter(["A", "B", "C", "A", ""]), "3.25"),
        (iter(["B", "B", "D", ""]), "2.3"),
        (iter(["F", "B", "C", "D", ""]), "1.5"),
    ],
)

def test_days_in_year_month(monkeypatch: MonkeyPatch, test_input, expected_output: str):
    mocked_input = lambda prompt="": next(test_input)
    #mocked_input_month = lambda prompt="": test_input_month
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        #m.setattr(builtins, "input", mocked_input_month)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("gpa_calculation", None)
        importlib.import_module(name="gpa_calculation", package="gpa_calculation")

    assert expected_output in mocked_stdout.getvalue().strip()
