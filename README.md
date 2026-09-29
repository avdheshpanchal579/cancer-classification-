# Cancer Classification - Python Essentials Project

## 1. Project Overview

This project is a simple command-line Python application that demonstrates basic Python programming concepts through a rule-based cancer risk classification example.

The program collects:
- Patient name
- Age
- Tumor size
- Pain (yes/no)
- Lump (yes/no)
- Weight loss (yes/no)

It then calculates a simple score using predefined rules and displays a classification of Low Risk, Medium Risk, or High Risk.

**Important:** This is an educational programming project only. It is not a medically validated cancer screening or diagnosis system and must not be used for medical decisions.

## 2. Technologies Used

- Python 3
- Standard Python input/output
- Conditional statements
- Functions
- Variables and data types
- Exception handling
- Loops

No external Python packages are required.

## 3. Project Structure

```text
cancer-classification/
├── main.py
├── README.md
├── requirements.txt
├── PROJECT_REPORT.md
└── .gitignore
```

## 4. Requirements

Install Python 3.8 or newer.

Check your Python installation:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

## 5. Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd YOUR-REPOSITORY
```



## 6. Run the Project

Run:

```bash
python main.py
```

Or, on systems using `python3`:

```bash
python3 main.py
```

The program will ask for patient information through the terminal.

## 7. Example

Example input:

```text
Name: Rahul
Age: 45
Tumor size in cm: 2.5
Pain (yes/no): yes
Lump (yes/no): yes
Weight loss (yes/no): no
```

The program calculates the score and displays the corresponding educational classification.

## 8. Classification Logic

The program uses the following simple rules:

### Tumor size

- Greater than 2 cm → 3 points
- Greater than 1 cm and up to 2 cm → 2 points
- 1 cm or less → 1 point

### Symptoms

- Pain = yes → +1 point
- Lump = yes → +2 points
- Weight loss = yes → +2 points

### Final classification

- Score 6 or above → High Risk
- Score 3 to 5 → Medium Risk
- Score below 3 → Low Risk

These rules are created solely for demonstrating programming logic and should not be interpreted as clinical criteria.

## 9. Features

- Command-line execution
- User input handling
- Input validation
- Yes/no validation
- Rule-based scoring
- Risk classification
- Clear output formatting
- No external dependencies

## 10. Disclaimer

This project is intended for educational purposes and demonstrates Python programming concepts. The classification rules are not based on a validated medical model. The output should not be considered a diagnosis, medical advice, or a substitute for consultation with a qualified healthcare professional.

## 11. Author

Student Project - Python Essentials
