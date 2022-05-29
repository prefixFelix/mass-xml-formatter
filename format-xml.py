#!/usr/bin/env python3
import argparse
import os
import pathlib
import sys
import xml.etree.ElementTree as ET


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        required=True,
                        type=str,
                        action='store',
                        metavar='PATH',
                        help="Path to the input directory.")
    parser.add_argument('-o', '--output',
                        type=str,
                        action='store',
                        metavar='PATH',
                        help="Path to the output directory")
    parser.add_argument('-is', '--ignore-subdirs',
                        action='store_true',
                        help="Set if you only want to format files from the specified directory and not from subdirectories.")
    args = parser.parse_args()

    if not os.path.isdir(args.input):
        sys.exit("The input directory does not exist!")
    input_dir = pathlib.Path(args.input).resolve()

    if args.output is None:
        args.output = '{}-formatted'.format(input_dir.stem)
    output_dir = pathlib.Path(args.output).resolve()

    search_pattern = '**/*'  # Query subdirs
    if args.ignore_subdirs:
        search_pattern = '*'  # Query only the current dir

    paths = []

    # Only XML files and ignore hidden files / dirs
    for path in input_dir.glob(search_pattern):
        if path.suffix.lower() == '.xml' and not path.name.startswith('.') and not os.path.isdir(path):
            paths.append(path)

    for path in paths:
        # Extract the dirs of the input folder
        striped_path = path.parts[len(path.parts) - path.parts[::-1].index(input_dir.stem):-1]
        # Build the path for the output file
        output_path = pathlib.Path(output_dir, *striped_path, path.name)

        # Create dir in the output dir
        pathlib.Path(output_dir, *striped_path).mkdir(parents=True, exist_ok=True)

        # Read file and pretty XML
        root = ET.parse(path).getroot()
        tree = ET.ElementTree(root)
        ET.indent(tree)

        with open(output_path, 'w') as output_xml:
            tree.write(output_xml, encoding='unicode', xml_declaration=True)

        print("{}\n"
              "--->\n"
              "{}\n".format(path, output_path))

    print("+-----------------------+\n"
          "Formatted files: {}\n"
          "+-----------------------+".format(len(paths)))


if __name__ == '__main__':
    main()
