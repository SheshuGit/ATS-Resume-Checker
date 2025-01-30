# ATS Resume Checker

## Overview
The **ATS Resume Checker** is a Flask-based web application that analyzes a resume (PDF) and compares it with a given job description. The application calculates a match score based on keyword similarities, helping job seekers optimize their resumes for Applicant Tracking Systems (ATS).

## Features
- Upload a **PDF** resume.
- Extract text from the uploaded resume.
- Compare resume content with the job description.
- Compute an ATS match score (capped at 100%).
- Simple web interface using Flask.

## Technologies Used
- **Python 3.11**
- **Flask** (for web framework)
- **PyPDF2** (for PDF text extraction)
- **NLTK** (for text processing)
- **HTML & CSS** (for frontend)

## Installation
### Prerequisites
Ensure you have **Python 3.11** installed on your system.

### Step 1: Clone the Repository
```bash
git clone https://github.com/SheshuGit/ATS-Resume-Checker.git
cd ATS-Resume-Checker
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Step 1: Run the Application
```bash
python app.py
```

### Step 2: Open the Web Interface
Go to `http://127.0.0.1:5000/` in your web browser.

### Step 3: Upload Resume & Enter Job Description
- Upload a **PDF** resume.
- Enter a job description in the text box.
- Click **Submit** to get the ATS match score.

## Project Structure
```
ATS-Resume-Checker/
│── app.py              # Main Flask application
│── requirements.txt    # List of dependencies
│── uploads/            # Directory for storing uploaded resumes
│── templates/
│   ├── index.html      # Upload form
│   ├── result.html     # Display match score
└── README.md           # Project documentation
```

## Notes
- The ATS score is calculated based on keyword matches.
- The score is **capped at 100%**.
- Currently, **only PDFs** are supported.

## Contributing
If you want to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your fork (`git push origin feature-branch`).
5. Submit a **Pull Request**.

## License
This project is licensed under the **MIT License**.

## Author
[SheshuGit](https://github.com/SheshuGit)
