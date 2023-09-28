import cv2
import os
from tqdm import tqdm

# Function to create video from image sequence
def create_video_from_sequence(sequence_folder, output_folder, output_subfolder, sequence_number, fps=10):
    images = []
    for filename in sorted(os.listdir(sequence_folder)):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust the file extensions as needed
            img = cv2.imread(os.path.join(sequence_folder, filename))
            if img is not None:
                images.append(img)

    if not images:
        print(f"No images found in {sequence_folder}")
        return

    height, width, layers = images[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use other codecs like 'XVID' or 'MJPG'
    
    # Create the output subfolder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    output_subfolder_path = os.path.join(output_folder, output_subfolder)
    os.makedirs(output_subfolder_path, exist_ok=True)
    
    # Change the output video name to include the sequence_number
    output_video_path = os.path.join(output_subfolder_path, f"{output_subfolder}_{sequence_number}.mp4")
    video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for img in tqdm(images, desc=f"Processing {os.path.basename(sequence_folder)}"):
        video.write(img)

    video.release()

# Root folder containing image sequences
root_folder = 'DeepAnnotateDataset2'
output_root_folder = 'Videos'  # Change this to your desired output folder

# Loop through each subfolder
for subfolder in os.listdir(root_folder):
    subfolder_path = os.path.join(root_folder, subfolder)
    if os.path.isdir(subfolder_path):
        # Create a video for each sequence in the subfolder
        sequence_number = 1
        for sequence_folder in os.listdir(subfolder_path):
            sequence_folder_path = os.path.join(subfolder_path, sequence_folder)
            if os.path.isdir(sequence_folder_path):
                create_video_from_sequence(sequence_folder_path, output_root_folder, subfolder, sequence_number)
                sequence_number += 1

print("Conversion completed.")
