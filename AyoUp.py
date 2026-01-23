#!/usr/bin/env python3
"""
Ayo Up — application launcher
"""

import sys
import os

# Upewnij się, że katalog projektu jest na PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from main import main


if __name__ == "__main__":
    main()
