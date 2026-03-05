# Quick-Calc

Quick-Calc is a desktop calculator built with Python backend and Tkinter UI. It supports addition, subtraction, multiplication, division, sign negation, and a clear button to set current value to 0, and a equals button to get the calculation result.

---

## Setup Instructions

**Requirements:** Python 3.9 or higher. Tkinter is included with standard Python installations on Windows.

```bash
# 1. Clone the repository
git clone https://github.com/Borinskii/swe-testing-assignment.git
cd swe-testing-assignment

# 2. Install pytest
pip install pytest
```

## Running the Application

```bash
python main.py
```

A calculator window will open. Use the on-screen buttons to perform calculations.

---

## How to Run Tests

```bash
pytest ./
```

All 14 tests (12 unit + 2 integration) should pass.

---

## Testing Framework Research

### Pytest vs Unittest

Python offers two main options for automated testing: the built-in `unittest` module and the third-party `pytest` framework.

`unittest` has been part of the Python standard library since Python 2.1, which means it doesn't require any additional installation, which is a big plus. Tests are written as classes in unittest and inherit from basic `unittest.TestCase`, and assertions use dedicated methods such as `assertEqual`, `assertRaises`, and `assertTrue`. Asserts and overall structure is familiar to developers that use Java, for example. However, even a simple test (similar to what was used in this project) requires a class, a method, and a specific assertion call, which can make test files very large and sometimes unclear.

`pytest` is a modern framework that is very popular in modern projects. Tests in this framework don't require inheritance, and plain 'assert' statements are used. Also Pytest can produce detailed, readable failure messages that clearly show what was expected vs what was received. The only trade-off is that it must be installed separately via `pip install pytest`.

**Chosen framework: `pytest`.** For this project I decided to use pytest because I have used it previously several times, and because it is very simple to use. Also it allows to launch all tests with a simple command and receive an informative feedback.

---