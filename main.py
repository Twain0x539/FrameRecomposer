import argparse
from frame_recomposer import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input video file/folder with frames path", default=None, type=str)
    parser.add_argument("output", help="output folder path", default=None, type=str)
    parser.add_argument("--fps", help="enable overwriting", default=30)
    parser.add_argument("--extract", "-e", help="extract frames mode", action="store_true", default=False)
    parser.add_argument("--merge", "-m", help="merge frames mode", action="store_true", default=False)
    parser.add_argument("--quiet", "-q", help="disable logs", action="store_true", default=False)
    parser.add_argument("--force", "-f", help="enable overwriting", action="store_true", default=False)
    args = parser.parse_args()

    if args.extract and args.merge:
        print("Only one of --merge or --extract should be used!")
    elif not args.extract and not args.merge:
        print("One of --merge or --extract should be passed!")


    if args.merge:
        merge(input_folder=args.input, output_file=args.output, force=args.force, fps=args.fps, quiet=args.quiet)
    else:
        extract(input_file=args.input, output_folder=args.output, force=args.force, quiet=args.quiet)
