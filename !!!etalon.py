from chardet.universaldetector import UniversalDetector
import re
import csv


# Задание 1 и 2 в одном классе - читаем парсим, записываем

class ContactNormalizer:
    # Наборы паттернов - можно расширять как угодно, ключи помогут не потеряться, что парсим
    patterns = {
        'fio': {
            'regexp': r'^(\w+)( |,)(\w+)( |,)(\w+|),(,+|)(,,,|[А-Яа-я]+)',
            'subst': r'\1,\3,\5,\7'
        },
        'phone': {
            'regexp': r'(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})',
            'subst': r'+7(\3)\4-\5-\6'},
        'add_phone': {
            'regexp': r'\(доб\.\s(\d+)\)*',
            'subst': r'доп.\1'
        }
    }

    def __init__(self, csv_file_path, delimiter=',', is_save_parsed_file=True, parsed_csv_file_path='parsed_file.csv'):
        """
        Инициализация
        :param csv_file_path: пусть к файлу CSV
        :param delimiter: разделитель
        :param is_save_parsed_file: нужно ли сохранять новый файл с обработанными данными
        :param parsed_csv_file_path: путь к новому файлу
        """
        self.file = csv_file_path
        self.parsed_csv_file_path = parsed_csv_file_path
        self.is_save_parsed_file = is_save_parsed_file
        self.delimiter = delimiter
        self.encoding = 'utf-8'
        self.parsed_data = {}

    def detect_encoding(self):
        """
        Метод определения колировки
        :return: кодировка
        """
        detector = UniversalDetector()
        with open(self.file, 'rb') as file:
            for line in file.readlines():
                detector.feed(line)
                if detector.done:
                    break
        detector.close()
        self.encoding = detector.result['encoding']
        return self.encoding

    def get_raw_data_list(self):
        """
        Метод для получения сырых данных
        :return: список списков
        """
        try:
            with open(self.file, encoding=self.detect_encoding()) as f:
                rows = csv.reader(f, delimiter=self.delimiter)
                return list(rows)
        except FileNotFoundError:
            print('Файл не найден')
            return None

    def create_csv(self):
        """
        Создание нового файла
        """
        if self.parsed_data:
            with open(self.parsed_csv_file_path, "w", encoding=self.encoding) as file:
                data_writer = csv.writer(file, delimiter=self.delimiter)
                data_writer.writerows([self.parsed_data[key] for key in self.parsed_data])

    def parse_data(self, row_data):
        """
        Парсинг данных и обработка согласно набору паттернов
        :param row_data: данные для парсинга - список
        :return: список с данными
        """
        row_data = ','.join(row_data)
        for key, patten in self.patterns.items():
            row_data = re.sub(patten['regexp'], patten['subst'], row_data)
        return row_data.split(',')

    def check_data(self, row_data, unique_key_index=0):
        """
        Проверка данных на уникальность
        :param row_data:
        :param unique_key_index: какое поле ключа использцем как уникальный идентификатор
        """
        data_id = row_data[unique_key_index]

        if self.parsed_data.get(data_id):
            old_data = self.parsed_data.get(data_id)
            for index, data in enumerate(old_data):
                for new_index, new_data in enumerate(row_data):
                    if new_index == index and not data and new_data:
                        old_data[index] = new_data
        else:
            self.parsed_data[data_id] = row_data

    def start_parse(self):
        """
        Старт парсиннга
        :return: данные парсинга или ничего
        """
        contacts_list = self.get_raw_data_list()
        if contacts_list:
            for contact in contacts_list:
                self.check_data(self.parse_data(contact))

            if self.is_save_parsed_file:
                self.create_csv()

            return self.parsed_data

        return None


if __name__ == '__main__':
    ContactNormalizer('phonebook_raw.csv').start_parse()