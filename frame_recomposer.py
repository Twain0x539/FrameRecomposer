import cv2
import numpy as np
from PIL import Image
import os
from tqdm import tqdm


def extract(self, input_file: str, output_folder: str, force: bool = False, quiet: bool = False) -> None:

    cap = cv2.VideoCapture(input_file)
    totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if not cap.isOpened():
        print(f"Error opening video stream or file {input_file}")

    video_name, extension = os.path.splitext(input_file.split('/')[-1])  # extract video name and remove extension
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    output_subfolder = os.path.join(output_folder, video_name)
    if not os.path.exists(output_subfolder):
        os.mkdir(output_subfolder)

    if len(os.listdir(output_subfolder)) > 0:
        if not force:
            if not quiet:
                print("Output directory is not empty! Operation cancelled.")
                return
        else:
            if not quiet:
                print("Warning! Output directory is not empty")

    if not quiet:
        print(f"Extracting video frames to {output_subfolder}\\")
        pbar = tqdm(total=totalFrames)
    ctr = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        frame_name = str(ctr).zfill(7)
        save_path = os.path.join(output_subfolder, frame_name) + ".jpeg"
        im.save(save_path)
        ctr += 1
        if not quiet:
            pbar.update(1)

    cap.release()

def merge(self, input_folder: str, output_file: str, force: bool = False, quiet: bool = False) -> None:
    pass
