import cv2
import numpy as np
from PIL import Image
import os
from tqdm import tqdm


class FrameRecomposer():

    def __init__(self):
        pass

    def extract(self, input_file: str, output_folder: str, force: bool = False, quiet: bool = False) -> None:

        cap = cv2.VideoCapture(input_file)
        totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        if not cap.isOpened():
            print("Error opening video stream or file")

        video_name = os.path.splitext(input_file.split('/')[-1])[0]  # extract video name and remove extension

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

        print(f"Extracting video frames to {output_subfolder}\\")
        ctr = 0
        with tqdm(total=totalFrames) as pbar:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                frame_name = str(ctr).zfill(7)
                save_path = os.path.join(output_subfolder, frame_name) + ".jpeg"
                im.save(save_path)
                pbar.update(1)
                ctr += 1

            cap.release()

    def merge(self, input_folder: str, output_file: str) -> bool:
        pass
