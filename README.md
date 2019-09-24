# posturefix
Python + OpenCV to alert you when you're slouching

WHen it detects a face, it sends an alert if the face is lower in the image (adjust the threshold for your setup - currently at 250px). ALerts repeat every 10 seconds if you don't sit up.

Used https://github.com/gigafide/simple_opencv_pi_face_detector for cv2 code

Currently set to run at 1fps - remove time.sleep(1) to have it run continuously.

COde is simple, but feel free to reach out for explanations or suggested improvements.

