import cv2

# Open the video file
video = cv2.VideoCapture('v1.mp4')

# Initialize a variable to keep track of the frame count
frame_count = 0

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = video.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Increment the frame count
    frame_count += 1

    # Extract the frame and save it to a file
    cv2.imwrite(f'frames/frame{frame_count}.jpg', frame)

# Release the video object
video.release()
