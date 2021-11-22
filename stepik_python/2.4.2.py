import os

res_dir_list = []
for cur_dir, dirs, files in os.walk('python/main'):
    print(cur_dir, dirs, files)
    for file in files:
        if os.path.splitext(file)[1] == '.py':
            res_dir_list.append(cur_dir.split('/')[1].replace('\\', '/'))
            continue

res_dir_list = list(set(res_dir_list))
res_dir_list.sort()
with open('python/2.4.2_output.txt', 'w') as f:
    f.write('\n'.join(res_dir_list))
