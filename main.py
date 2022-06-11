def make_cook_book_from_file(filename):
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as recipes_file:
        name = recipes_file.readline()[:-1]
        while name:
            amount_of_ingredients = int(recipes_file.readline()[:-1])
            list_of_ingredients = []
            for i in range(amount_of_ingredients):
                temp = recipes_file.readline()[:-1]
                ingredient = {'ingredient_name': temp[:temp.find('|')]}
                temp = temp[temp.find('|') + 2:]
                ingredient['quantity'] = int(temp[:temp.find('|')])
                temp = temp[temp.find('|') + 2:]
                ingredient['measure'] = temp
                list_of_ingredients.append(ingredient)
            cook_book[name] = list_of_ingredients
            temp = recipes_file.readline()
            name = recipes_file.readline()[:-1]
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = make_cook_book_from_file('recipes.txt')
    ingredients = {}
    for key, value in cook_book.items():
        if key in dishes:
            for ingredient in value:
                if ingredient['ingredient_name'] in ingredients.keys():
                    ingredients[ingredient['ingredient_name']]['quantity'] += person_count * ingredient['quantity']
                else:
                    ingredients[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'], 'quantity': person_count * ingredient['quantity']}
    return dict(sorted(ingredients.items(), key=lambda x: x[0]))


if __name__ == '__main__':
    list_of_dishes = input("Введите блюда через запятую: ").title().split(', ')
    ingredients = get_shop_list_by_dishes(list_of_dishes, int(input("Введите количество человек: ")))
    for name, amount in ingredients.items():
        print(name, end=": ")
        print(amount)

