# подключение модулей
import json
from datetime import datetime

# функция popularCategories() получает на вход файл формата json
# и возвращает категории с наибольшим количеством покупок в
# предновогодний период
def popularCategories(jsonFile):
    categoriesNum = {}
    
    with open(jsonFile, encoding='utf-8') as file:
        data = json.load(file)

        # отбираем покупки, сделанные в предновогодний период, и подсчитываем их
        # количество по категориям
        for elem in data:
            ordered_at = datetime.strptime(elem['ordered_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if ordered_at.month == 12 and ordered_at.day >= 1 and ordered_at.day <= 31:
                for item in elem['items']:
                    category = item['category']['name']
                    if category in categoriesNum:
                        categoriesNum[category] += 1
                    else:
                        categoriesNum[category] = 1
                        
    # находим категории с максимальным количеством покупок                    
    maxCount = max(categoriesNum.values())
    popularCategories = []
    for category, count in categoriesNum.items():
        if count == maxCount:
            popularCategories.append(category)

    popularCategories.sort() # сортируем категории в алфавитном порядке   
    
    result = {"categories": popularCategories}
    return json.dumps(result, ensure_ascii=False) # возвращаем результат

# основная часть
jsonFile = 'input.json' # определям файл с входными данными
result = popularCategories(jsonFile) # проводим обработку файла
print(result) # выводим результат
