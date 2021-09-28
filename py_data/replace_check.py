def dataReplace(string):
    replace_check = {'[HEADER]': 'Test python server',
                     '[CONTENT_PAGE]': 'Welcome to this test page! This text replaced via server utils and special tags!'}
    for key, value in replace_check.items():
        string = string.replace(key.encode('utf-8'), value.encode('utf-8'))
    return string
