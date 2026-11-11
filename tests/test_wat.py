import csv
import os
import sys
from pathlib import Path

# Ensure headless execution for CI
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

sys.path.insert(0, str(Path(__file__).parent.parent))
import wat

def test_wat_constants():
    assert wat.BLACK == (0, 0, 0)
    assert wat.WHITE == (255, 255, 255)
    assert hasattr(wat, "WATApp")

def test_csv_datasets():
    csv_files = ["wat.csv", "wat-chatgpt.csv"]
    for fname in csv_files:
        p = Path(fname)
        assert p.exists()
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f)
            rows = [r for r in reader if r]
            assert len(rows) > 10, f"{fname} should have multiple word entries"
