from gendiff import generate_diff


def main():
    generate_diff()


if __name__ == '__main__':
    main()


generate_diff(r'gendiff/files/file1.json', r'gendiff/files/file2.json')
