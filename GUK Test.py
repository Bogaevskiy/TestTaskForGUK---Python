import re
def file_search(file, key):
    f = open(file, 'r')
    re.split('\x0A|\t', f)
    dict = {f[i]: f[i+1] for i in range(0, len(f), 2)}
    return dict[key]
    
