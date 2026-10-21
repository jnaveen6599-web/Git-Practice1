import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import app

def test_add_task():
    assert app.add_task("x") == 1
