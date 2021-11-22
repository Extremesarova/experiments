with open('python/2.4.1_input.txt') as f, open('python/2.4.1_output.txt', 'w') as w:
    file_content = f.read().splitlines()
    w.write('\n'.join(file_content[::-1]))