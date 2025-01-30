from flask import Flask, render_template, request
import os
import PyPDF2
from werkzeug.utils import secure_filename
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def calculate_match_score(resume_text, job_description):
    """Calculate the ATS match score between resume and job description."""
    # Load stop words
    stop_words = set(stopwords.words('english'))
    
    # Tokenize and clean the text
    resume_tokens = [word.lower() for word in word_tokenize(resume_text) if word.isalnum() and word.lower() not in stop_words]
    print("Resume",resume_tokens)
    job_tokens = [word.lower() for word in word_tokenize(job_description) if word.isalnum() and word.lower() not in stop_words]

    # Find matches
    common_tokens = set(resume_tokens) & set(job_tokens)
    print("Common",common_tokens)

    match_score = len(common_tokens) / len(set(job_tokens)) * 100 if job_tokens else 0

    # Cap the score at 100
    match_score = min(match_score, 100)
    
    return round(match_score, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handle the main page and form submissions."""
    if request.method == 'POST':
        if 'resume' not in request.files:
            return "No resume uploaded", 400

        file = request.files['resume']
        job_description = request.form['job_description']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Extract text and calculate score
            resume_text = extract_text_from_pdf(file_path)
            match_score = calculate_match_score(resume_text, job_description)

            return render_template('result.html', score=match_score)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
