from resume_loader import load_resume_data
from pdf_generator import generate_resume
import os

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    resume_data_path = os.path.join(current_dir, "data", "resume_data.json")
    resume_data = load_resume_data(resume_data_path)
    generate_resume(resume_data)
