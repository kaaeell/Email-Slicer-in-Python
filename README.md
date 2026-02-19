# Email Slicer in Python

A simple Python CLI tool that extracts useful information from an email address.

This project started as a beginner exercise and was later improved to include better validation, cleaner structure, and command-line support.

---

## Features

- Validate email format using Regex
- Extract:
  - Username
  - Domain
  - Extension
- Optional username masking (for privacy)
- Option to save results to a JSON file
- Interactive mode
- Command-line argument support

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kaaeell/Email-Slicer-in-Python.git
cd Email-Slicer-in-Python
```

Run the program:

```bash
python email_slicer.py
```

---

## Usage

### Interactive Mode

```bash
python email_slicer.py
```

Type the email manually when prompted.

---

### Pass Email Directly

```bash
python email_slicer.py -e example@gmail.com
```

---

### Mask Username

```bash
python email_slicer.py -e example@gmail.com -m
```

---

### Save Results to JSON

```bash
python email_slicer.py -e example@gmail.com -s
```

The results will be saved in:

```
email_results.json
```

---

## Example Output

```
--- Email Info ---
Username  : example
Domain    : gmail
Extension : .com
```

---

## Why I Built This

I built this project to practice:

- String manipulation
- Regular expressions
- Writing modular Python code
- Using argparse
- Structuring small CLI tools properly

---

## Future Improvements

- Export to CSV
- Add GUI version (Tkinter)
- Add unit tests
