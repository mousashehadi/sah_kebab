# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Run all tests:
```bash
python -m unittest discover
```

Run a single test file:
```bash
python -m unittest test_profit_calculator.py
```

Run the calculator and print a sample profit report:
```bash
python profit_calculator.py
```

## Architecture

The project is a profit calculator for a kebab shop (`sah_kebab`). It has two files:

- **`profit_calculator.py`** — core logic and CLI entry point. Contains two functions:
  - `calculate_profit(revenues, expenses)` — pure function that takes two lists of `{"name": str, "amount": float}` dicts and returns `{"total_revenue", "total_expenses", "profit", "is_profitable"}`.
  - `print_report(revenues, expenses)` — formats and prints a Russian-language report to stdout using the result of `calculate_profit`.

- **`test_profit_calculator.py`** — `unittest`-based tests for `calculate_profit` only (not `print_report`).

## Conventions

- No external dependencies — stdlib only (no `requirements.txt`).
- All user-facing strings (labels, report headers) are in Russian.
- The `{"name": ..., "amount": ...}` dict shape is the canonical data format for both revenues and expenses throughout the codebase.
- `is_profitable` is `False` at break-even (profit == 0), not just when profit < 0.
