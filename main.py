import argparse
from frame_recomposer import FrameRecomposer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input video file/folder with frames path", default=None, type=str)
    parser.add_argument("output", help="output folder path", default=None, type=str)
    parser.add_argument("--extract", "-e", help="extract frames mode", action="store_true", default=False)
    parser.add_argument("--merge", "-m", help="merge frames mode", action="store_true", default=False)
    args = parser.parse_args()

    if args.extract and args.merge:
        print("Only one of --merge or --extract should be used!")
    elif not args.extract and not args.merge:
        print("One of --merge or --extract should be passed!")



    frame_recomposer = FrameRecomposer()

    if args.merge:
        frame_recomposer.merge(args.input, args.output)
    else:
        frame_recomposer.extract(args.input, args.output)
