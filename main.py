import cv2
import pytesseract
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Function to perform number plate recognition on an image
def recognize_number_plate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng')
    return text.strip()

# Function to write data to Google Sheets
def write_to_google_sheets(data):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open('capstone').sheet1
    sheet.append_row(data)

# Main function for processing video
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform number plate recognition on the frame
        plate_text = recognize_number_plate(frame)

        # Store the extracted data in Google Sheets
        write_to_google_sheets([plate_text])

    cap.release()

# Main function for processing image
def process_image(image_path):
    image = cv2.imread(image_path)
    plate_text = recognize_number_plate(image)
    write_to_google_sheets([plate_text])

# Main function
if __name__ == "__main__":
    # Example video path
    video_path = '/home/naveenkumar/Desktop/Automatic_Number_Plate_Detection_Recognition_YOLOv8/runs/detect/train5/vedio.mp4'
    # Example image path
    image_path = ''

    # Process the video
    process_video(video_path)

    # Process the image
    process_image(image_path)
