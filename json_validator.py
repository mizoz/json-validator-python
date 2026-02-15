#!/usr/bin/env python3
"""Validate JSON syntax."""
import sys, json
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: json_validator.py <file.json>"); sys.exit(1)
    try: json.loads(Path(sys.argv[1]).read_text()); print("Valid JSON ✓")
    except json.JSONDecodeError as e: print(f"Invalid: {e}"); sys.exit(1)
