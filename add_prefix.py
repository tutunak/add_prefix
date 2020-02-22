#!/usr/bin/env python3
import argparse


def add_prefix(file_name: str, prefix: str, dest: str = None) -> None:
    if not dest:
        dest = f"out_{file_name}"

    with open(file_name, 'r') as source:
        with open(dest, 'w') as destination:
            while True:
                line = source.readline()
                if not line:
                    break
                destination.write(f"{prefix}{line}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str)
    parser.add_argument("prefix", type=str)
    parser.add_argument("--dest", type=str, required=False, help="Destination for out file, default is out_+file_name")
    args = parser.parse_args()
    add_prefix(file_name=args.file_name, prefix=args.prefix, dest=args.dest)


if __name__ == '__main__':
    main()
