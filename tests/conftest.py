"""Garante que a raiz do projeto está no sys.path (imports como calculadora_bugada)."""

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_path = str(_ROOT)
if _path not in sys.path:
    sys.path.insert(0, _path)
