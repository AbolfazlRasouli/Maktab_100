import os
import argparse

master_parser = argparse.ArgumentParser(description="Master come on!!!")
master_parser.add_argument("-d", "--directory", type=str, help="Directory ra vared kon ", required=True)
master_parser.add_argument("-f", "--file", type=str, help="Filename ra vared kon ")
master_parser.add_argument("-F", "--file-extension", default=None, help="Filter files by extension when using -d.")

args = master_parser.parse_args()


def directory_size_getter(path):
    size = 0
    for path, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    return size / 1024


def file_size_getter(path, fname):
    for (root, dirs, files) in os.walk(path):
        for file in files:
            if file == fname:
                joiner = os.path.join(root, file)
                size = os.path.getsize(joiner)

    return size / 1024


def format_finder(path, ext):
    size = 0
    for (root, dirs, files) in os.walk(path):
        for file in files:
            if file.endswith("." + ext):
                joiner = os.path.join(root, file)
                size += os.path.getsize(joiner)
                # print(f"File: {joiner} with Size: {size / 1024} KB")

    return size / 1024


if args.directory:
    if args.file_extension:
        print(format_finder(args.directory, args.file_extension))
    elif args.file:
        print(file_size_getter(args.directory, args.file))
    else:
        print(directory_size_getter(args.directory))

    