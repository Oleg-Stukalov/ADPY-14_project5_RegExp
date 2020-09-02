from pprint import pprint
import requests
import csv
import re

#CONSTANTS
CSV_RAW = 'https://github.com/netology-code/py-homeworks-advanced/raw/master/5.Regexp/phonebook_raw.csv'


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
      # TODO 1: выполните пункты 1-3 ДЗ
  #   3. объединить все дублирующиеся записи о человеке в одну.
    print('self.contacts_list: ', self.contacts_list)
    #print('self.contacts_list[1]: ', self.contacts_list[1])

    #find and join doubles
    for index in range(len(self.contacts_list)):
      for element in self.contacts_list[index]:
        pass

    pattern1 = '\w+'
    # result = re.findall(pattern1, self.contacts_list[1][0])
    # print('***', result)

    common_list = [''] * len(self.contacts_list)
    #print(temp_list)
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

      print('self.contacts_list[contact]: ', self.contacts_list[contact])

      # 2. telephone correction
      # tel RegExp: (\+7|8)\s*\(*\d+\)*(\s|-)*\d+\-*\d+\-*\d+(\s|\()*\w+.\s*\d+
      # tel_regex = re.compile(r'(\+7|8)\s*\(*\d+\)*(\s|-)*\d+\-*\d+\-*\d+(\s|\()*\w+.\s*\d+')
      # tel_result = tel_regex.sub(r'+7 (\2) \3-\5-\7', self.contacts_list[contact][5])
      # print('***', tel_result)
      # self.contacts_list[contact][5] = tel_result

      # 3. doubles correction








  # TODO 2: сохраните получившиеся данные в другой файл
  # код для записи файла в формате CSV
  # with open("phonebook.csv", "w") as f:
  #   datawriter = csv.writer(f, delimiter=',')
  #   # Вместо contacts_list подставьте свой список
  #   datawriter.writerows(contacts_list)