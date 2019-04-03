import pytest
from jp.function import impDino

def test_impDino():
    resp= impDino()
    assert resp is not None
    assert len(resp.json()) > 1
    assert len(resp.json()) == 7
    assert resp.status_code == 200

def testparam_impDino()