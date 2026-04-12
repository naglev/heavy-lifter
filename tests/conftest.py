import sys
import pytest
from pathlib import Path

path_src = Path(__file__).parents[1]
sys.path.insert(0, str(path_src))
