if __name__ == '__main__':
    s = input()
    for func in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(map(getattr(str, func), list(s))))