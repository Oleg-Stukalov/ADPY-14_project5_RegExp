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
  #   1. поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
  #   2. привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
  #   3. объединить все дублирующиеся записи о человеке в одну.
    print('self.contacts_list: ', self.contacts_list)
    print('self.contacts_list: ', self.contacts_list[1])
    pattern1 = '\w+'
    result = re.findall(pattern1, self.contacts_list[1][0])
    # print('+++', self.contacts_list[1][0])
    print('***', result)





  # TODO 2: сохраните получившиеся данные в другой файл
  # код для записи файла в формате CSV
  # with open("phonebook.csv", "w") as f:
  #   datawriter = csv.writer(f, delimiter=',')
  #   # Вместо contacts_list подставьте свой список
  #   datawriter.writerows(contacts_list)