def make_file(amount_of_files, names_of_files, result_filename):
    files = []
    readlines_files = []
    for i in range(amount_of_files):
        readlines_files.append(
            {'filename': names_of_files[i], 'file': open(names_of_files[i], 'r', encoding='utf-8').readlines()})
        files.append(open(names_of_files[i], 'r', encoding='utf-8'))
    readlines_files.sort(key=lambda x: len(x['file']))
    with open(result_filename, 'w', encoding='utf-8') as result_file:
        for file in readlines_files:
            result_file.write(file['filename'] + '\n')
            result_file.write(str(len(file['file'])) + '\n')
            result_file.writelines(file['file'])
            result_file.write('\n')

    for file in files:
        file.close()


if __name__ == '__main__':
    make_file(3, ['1.txt', '2.txt', '3.txt'], 'result_file')
