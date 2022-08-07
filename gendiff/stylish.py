def stylish(diff):

    result = '{' + '\n'
    for i in diff:
        if i['diff'] == 'both_no_changes':
            result = result + '    ' + i['key'] + ': ' + str(i['value']) + '\n'
        elif i['diff'] == 'both_have_changes':
            result = result + '  - ' + i['key'] + ': ' + str(i['changes']['-']) + '\n'
            result = result + '  + ' + i['key'] + ': ' + str(i['changes']['+']) + '\n'
        elif i['diff'] == 'first_only':
            result = result + '  - ' + i['key'] + ': ' + str(i['value']) + '\n'
        elif i['diff'] == 'second_only':
            result = result + '  + ' + i['key'] + ': ' + str(i['value']) + '\n'
    result = result + '}'
    return result.lower()
