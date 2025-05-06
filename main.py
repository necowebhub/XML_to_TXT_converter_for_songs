import os
import xml.etree.cElementTree as ET

def create_txt(title, lyrics):
    try:
        with open(f'./to/{title}.txt', 'w', encoding='utf-8') as file:
            file.write(f'Заголовок: {title}\n\n')
            file.write(f'{lyrics}')
    except IOError:
        print("Ошибка ввода-вывода.")

def xml_to_txt():
    try:
        for filename in sorted(os.listdir('./from/')):
            file_path = os.path.join('./from/', filename)
            
            root = ET.parse(f'{file_path}').getroot()

            # Чтение элементов
            for child in root.iter('song'):
                try:
                    title = child.find('title').text
                    lyrics = child.find('lyrics').text

                    if title is not None and lyrics is not None:
                        create_txt(title, lyrics)
                    else: 
                        print('Ошибка в прочтении файла')
                except Exception as e:
                    print(f"Произошла ошибка: {e}")

            print(f'{filename} был успешно преобразован')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    # Чтение XML
    print('--- Чтение XML ---')

    try:
        xml_to_txt()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
