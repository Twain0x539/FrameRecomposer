import cv2
from PIL import Image
import os
from tqdm import tqdm


def extract(input_file: str, output_folder: str, force: bool = False, quiet: bool = False) -> None:
    cap = cv2.VideoCapture(input_file)
    if not cap.isOpened():
        print(f"Error opening video stream or file {input_file}")
        return
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if not quiet:
            print(f"Video stream {input_file} successfully opened ({fps} FPS)")

    video_name = os.path.splitext(input_file.split('/')[-1])[0]  # extract video name and remove extension
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    output_subfolder = os.path.join(output_folder, video_name)
    if not os.path.exists(output_subfolder):
        os.mkdir(output_subfolder)

    if len(os.listdir(output_subfolder)) > 0:
        if not force:
            print("Error! Output directory is not empty. Operation cancelled.")
            return
        else:
            print("Warning! Output directory is not empty")

    if not quiet:
        print(f"Extracting video frames to {output_subfolder}\\")
        pbar = tqdm(total=total_frames)
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


def merge(input_folder: str, output_file: str, fps: int = 30, force: bool = False, quiet: bool = False) -> None:
    input_frames = [f for f in os.listdir(input_folder) if
                    f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png")]
    input_frames = sorted(input_frames)

    if len(input_frames) < 1:
        print("Error! Input directory is empty or not containing images.")
        return

    frame = cv2.imread(os.path.join(input_folder, input_frames[0]))
    H, W = frame.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    if os.path.exists(output_file):
        if not force:
            print(f"Error! Output path {output_file} already exists.")
            return

    out = cv2.VideoWriter(output_file, fourcc, float(fps), (W, H))

    if not quiet:
        print(f"Merging {input_folder} to {output_file}")
    for filepath in tqdm(input_frames):
        frame = cv2.imread(os.path.join(input_folder, filepath))
        H_cur, W_cur = frame.shape[:2]
        if H_cur != H or W_cur != W:
            print("Warning! Image of different shape! Skipping...")
        else:
            out.write(frame)

    out.release()
