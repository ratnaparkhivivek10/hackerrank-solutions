def count_substring(string, sub_string):
    return len(set([string.find(sub_string, i) for i in range(len(string)) if string.find(sub_string, i) != -1]))