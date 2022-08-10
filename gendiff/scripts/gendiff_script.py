from gendiff import generate_diff
import argparse


def main():
    gendiff = argparse.ArgumentParser(prog='gendiff', description='Compares\
        two configuration files and shows a difference.')
    gendiff.add_argument('first_file')
    gendiff.add_argument('second_file')
    gendiff.add_argument('-f', '--format', help='set format of output')
    args = gendiff.parse_args()
    formatter = args.format
    if formatter:
        diff = generate_diff(args.first_file, args.second_file, formatter=formatter)
    else:
        diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
