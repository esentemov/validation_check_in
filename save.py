import os
import random

def saveme(data_file):
    os.getcwd()
    save_data = "database_"+str(random.randint(1, 99999))+".txt"
    s = open(save_data, 'w')
    s.write(str(data_file) + '\n')
    s.close()
    print("Файл '" + save_data + "' успешно сохранен")
