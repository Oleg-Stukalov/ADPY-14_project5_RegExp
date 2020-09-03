from pprint import pprint
import requests
import csv
import re
from collections import OrderedDict

#CONSTANTS
CSV_RAW = 'https://github.com/netology-code/py-homeworks-advanced/raw/master/5.Regexp/phonebook_raw.csv'
NL = '\n'

class Phonebook:
  """
  Phonebook is a class that gets raw date from CSV file (https://github.com/netology-code/py-homeworks-advanced/raw/master/5.Regexp/phonebook_raw.csv) and
  update it, saves it in local CSV file
  """

  def __init__(self, url=CSV_RAW):
    self.contacts_list = []
    self.contacts_list_edited = []
    response = requests.get(url)
    print('Исходные данные будем брать отсюда:', url)
    # сохраняю локальную копию файла
    with open('phonebook_raw.csv', 'wb') as f:
      f.write(response.content)

    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      self.contacts_list = list(rows)
    # print('contacts_list: ', type( self.contacts_list), len( self.contacts_list))
    # print( self.contacts_list)
    #print('+++',  self.contacts_list[1][0])
    #pprint( self.contacts_list)

  def Reg_exp(self):

    common_list = [''] * len(self.contacts_list)
    doubles_list = [[]] * len(self.contacts_list)
    for index in range(len(self.contacts_list)):
      for element in self.contacts_list[index]:
        #print(type(element), element)
        #print('index: ', index)
        #print(len(temp_list))
        common_list[index] += f'{element} '
    #print('***', common_list )
    print()

    #1. names correct placement
    # name RegExp: [А-ЯЁ][а-яё]+
    for contact in range(1, len(self.contacts_list)):
      splitted_names = '[А-ЯЁ][а-яё]+'
      name_result = re.findall(splitted_names, common_list[contact])
      #print('result: ', len(result), result)
      for names in range(3):
        #print(result[index])
        try:
          self.contacts_list[contact][0] = name_result[0]
          self.contacts_list[contact][1] = name_result[1]
          self.contacts_list[contact][2] = name_result[2]
        except:
          IndexError

      #print('self.contacts_list[contact]: ', self.contacts_list[contact])

      # 2. telephone correction +7(999)999-99-99 доб.9999
      # tel RegExp: (\+7|8)\s*\(*(\d+)\)*(\s|-)*(\d+)\-*(\d+)\-*(\d+)(\s\(*доб\.\s\d+\)*)?
      tel_regex = re.compile(r'(\+7|8)\s*\(?(\d+)\)?(\s|-)*(\d+)\-*(\d+)\-*(\d+)(\s\(?доб.\s*\d+\)?)?')
      tel_result = tel_regex.sub(r'+7(\2)\4-\5-\6\7', self.contacts_list[contact][5])
      #print('***', tel_result)
      self.contacts_list[contact][5] = tel_result

      # 3. doubles correction
      for contact in range(1, len(self.contacts_list)):
        for contact2 in range(contact+1, len(self.contacts_list)):
          if self.contacts_list[contact][0] == self.contacts_list[contact2][0] and self.contacts_list[contact][1] == self.contacts_list[contact2][1]:
            # print(self.contacts_list[contact][0], self.contacts_list[contact2][0])
            # print(self.contacts_list[contact][1], self.contacts_list[contact2][1])
            print(f'Внимание! Найдены дубли:{NL} {self.contacts_list[contact]} и {NL} {self.contacts_list[contact2]} {NL}Ждите окончания процесса спаривания!{NL}')
            for element in range(len(self.contacts_list[contact])):
              if len(self.contacts_list[contact][element]) <= len(self.contacts_list[contact2][element]):
                self.contacts_list[contact][element] = self.contacts_list[contact2][element]
                self.contacts_list[contact2][element] = ''
                self.contacts_list[contact2][0] = ''
                self.contacts_list[contact2][1] = ''
            print('Пожалуйста, проверьте корректность результатов спаривания:', NL, self.contacts_list[contact], NL)

      double_indexes = [] #номера строк для удаления
      for contact in range(len(self.contacts_list)):
        if self.contacts_list[contact][0] == '':
          double_indexes.append(contact)

    iter_ratio = 0 #коэф учитывающий уменьшение длины списка
    for index in double_indexes:
      self.contacts_list.pop(index - iter_ratio)
      iter_ratio +=1


    # for contact in range(len(self.contacts_list)):
    #   print('*****', len(self.contacts_list[contact]), self.contacts_list[contact])


    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf-8') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(self.contacts_list)
    print('Обработанная телефонная книга успешно сохранена в файл: phonebook.csv')