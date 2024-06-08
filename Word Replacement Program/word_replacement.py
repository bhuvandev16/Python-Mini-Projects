def replace_word_in_file(file_path, word_to_replace, replacement_word):
    try:
        with open(file_path, 'r+') as file:
            content = file.read()
            if word_to_replace not in content:
                print('Word does not exist in the file')
            else:
                file.seek(0)
                file.write(content.replace(word_to_replace, replacement_word))
                file.truncate()
                print('Word replacement was successfull')
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'An error occurred {e}')

def main():
    file_path = 'Word Replacement Program/file.txt'
    word_to_replace = input('Enter the word to replace: ')
    replacement_word = input('Enter the replacement word: ')

    replace_word_in_file(file_path, word_to_replace, replacement_word)

if __name__ == '__main__':
    main()