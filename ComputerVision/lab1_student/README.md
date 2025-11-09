# CV Python Environment for Lab1

This folder contains a Python virtual environment and a small verification script to confirm common computer vision packages are installed.

Files:
- `requirements.txt` - packages to install
- `verify_env.py` - script that prints package versions and writes a small test image using OpenCV

Quick steps (Windows PowerShell):

1. Open PowerShell and change to this folder:
   cd "c:\Users\Tyler Marino\OneDrive\Desktop\GradSchool\Saclay\ComputerVision\lab1_student"

2. Create venv and activate it:
   python -m venv .venv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force; . .\.venv\Scripts\Activate.ps1

3. Upgrade pip and install packages:
   python -m pip install --upgrade pip
   pip install -r requirements.txt

4. Run the verification script:
   python verify_env.py

