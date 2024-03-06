Number Plate Recognition and Storing Data in Sheets - Capstone Project
Overview
This project aims to perform number plate recognition on images and videos using Python. The extracted number plate data is then stored in Google Sheets for further analysis and processing.

Steps to Run the Project
Step 1: Install Required Packages
Install the necessary Python packages using pip:

Copy code
pip install opencv-python
pip install pytesseract
pip install gspread
pip install oauth2client
Step 2: Download Credentials
Download the credentials.json file from your Google API Console and place it in your project folder.

Step 3: Configure File Paths
Update the file paths in the main.py file as follows:

python
Copy code
# Example Video Path
video_path = 'paste the file path'

# Example Image Path
image_path = 'paste the file path'
Step 4: Run the Script
Execute the main.py file by running the following command in the terminal:

css
Copy code
python3 main.py
This will start the execution of the script, performing number plate recognition on the specified image and video files, and storing the extracted data in Google Sheets.

Feel free to customize the project according to your requirements and explore additional functionalities as needed.

by Naveenkumar.s(Kgisl institute of technology)
