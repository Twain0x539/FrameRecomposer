# FrameRecomposer

Using this module you can:
* Save video frames as separate images to folder
* Merge separate images to one video

## Installing
### 0. Requirements
This module was developed using Python 3.9, but must work on lower versions

### Clone repository and install pip requirements:
```
git clone https://github.com/Twain0x539/FrameRecomposer.git
pip install -r requirements.txt
```
## Using
### Extraction
```
python main.py <input_video> <output_folder> --extract
```
Separate <input_video> to frames and save them under <output_folder>/<input_video>/
#### Optional flags
```
-f or --force # Enables overwriting in output folder
-q or --quiet # Disables intermediate module output
```

### Merging
```
python main.py <input_folder> <output_video> --merge
```
Merge all frames from input_folder as <output_video>.mp4
#### Optional flags
```
-f or --force # Enables overwriting output_video
-q or --quiet # Disables intermediate module output
--fps # Set output video FPS, Default=30
```
