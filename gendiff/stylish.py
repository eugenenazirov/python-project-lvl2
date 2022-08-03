def stylish(diff):
    result = '{' + '\n'
    for i in diff.keys():
        if i['diff'] == 'both':
            if file1[i] == file2[i]:
                result = result + '    ' + i + ': ' + str(file1[i]) + '\n'
            else:
                result = result + '  - ' + i + ': ' + str(file1[i]) + '\n'
                result = result + '  + ' + i + ': ' + str(file2[i]) + '\n'
        elif i['diff'] == 'only_first':
            result = result + '  - ' + i + ': ' + str(file1[i]) + '\n'
        elif i['diff'] == 'only_second':
            result = result + '  + ' + i + ': ' + str(file2[i]) + '\n'
    result = result + '}'
    return result.lower()


    # result = '{' + '\n'
    # for i in sorted_files:
    #     if i in file1.keys() & file2.keys():
    #         if file1[i] == file2[i]:
    #             result = result + '    ' + i + ': ' + str(file1[i]) + '\n'
    #         else:
    #             result = result + '  - ' + i + ': ' + str(file1[i]) + '\n'
    #             result = result + '  + ' + i + ': ' + str(file2[i]) + '\n'
    #     elif i in file1.keys() - file2.keys():
    #         result = result + '  - ' + i + ': ' + str(file1[i]) + '\n'
    #     elif i in file2.keys() - file1.keys():
    #         result = result + '  + ' + i + ': ' + str(file2[i]) + '\n'
    # result = result + '}'
    # return result.lower()