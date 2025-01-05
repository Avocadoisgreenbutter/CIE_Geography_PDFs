from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Path to base folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAPERS_DIR = BASE_DIR

@app.route('/')
def index():
    # Display available papers
    folders = ['Paper_1', 'Paper_2', 'Paper_3', 'Paper_4']
    return render_template('index.html', folders=folders)

@app.route('/view/<folder>')
def view_folder(folder):
    # List PDFs in the selected folder
    folder_path = os.path.join(PAPERS_DIR, folder)
    if os.path.exists(folder_path):
        # Detect question papers and mark schemes based on `qp` and `ms`
        question_pdfs = [f for f in os.listdir(folder_path) if 'qp' in f.lower() and f.endswith('.pdf')]
        ms_pdfs = [f for f in os.listdir(folder_path) if 'ms' in f.lower() and f.endswith('.pdf')]
        return render_template('folder.html', folder=folder, question_pdfs=question_pdfs, ms_pdfs=ms_pdfs)
    return "Folder not found", 404

@app.route('/pdf/<folder>/<filename>')
def serve_pdf(folder, filename):
    # Serve PDF files
    folder_path = os.path.join(PAPERS_DIR, folder)
    if os.path.exists(folder_path):
        return send_from_directory(folder_path, filename)
    return "File not found", 404

@app.route('/viewer/<folder>/<question>/<ms>')
def viewer(folder, question, ms):
    # Display question paper and MS toggle
    return render_template('pdf_viewer.html', folder=folder, question=question, ms=ms)

if __name__ == '__main__':
    app.run(debug=True)
	
