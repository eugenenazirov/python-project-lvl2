def sort_files(file1, file2):
    merged_files = file1 | file2
    sorted_list = sorted(merged_files.items(), key=lambda x: x[0])
    sorted_files = dict(sorted_list)
    return sorted_files
