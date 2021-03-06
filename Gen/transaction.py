import random

from random import choice

types = [{"banks": ["ATB", "VTB", "Alpha-Bank", "Sberbank", "Tinkoff", "Alpha-bank", "Western-Union", "Bank of America",
                    "Gazprom-bank"],
          "stores": ["24/7", "K&B", "Foods", "X5", "Zara", "Apple", "DNS", "Adidas", "Reebok",
                     "Samsung"],
          "humans": [["Alex", "Tom", "Petr", "Rick", "Robert", "Pavel", "Oleg", "Carl", "Paul",
                      "Vadim", "Timur", "Roman", "Michael", "Archibald", "Tim", "Dmitriy",
                      "Sean", "Nikolay", "Ares", "Denis", "Colt", "julio", "Demon", "Bob", "Yan",
                      "Yakov", "John", "James", "Vasiliy", "Vladimir", "Rob", "Ilia", "Ilya", "Gunnar"],
                     ["Ivanov", "Smirnov", "Sobolev", "Jones", "Johnson", "Peres", "Milos",
                      "Warner", "Sid", "Black", "White", "Stalin", "Rus", "Vegan", "Nelson", "Gaits"]],
          "type": ["bank", "store", "client"],
          "direction": ["to", "from"]
          }]


def trans_creation(how_many: int):
    bank_trans = []
    while how_many >= 1:
        for item in types:
            name = item.get("humans")[0]
            surname = item.get("humans")[1]
            bank = item.get("banks")
            stores = item.get("stores")
            type = item.get("type")
            via = item.get("direction")
            trans_type = choice(type)
            via_type = choice(via)
            if trans_type == "bank":
                bank_choice = choice(bank)
                bank_sum = random.randint(100, 10000)
                str_sum = str(bank_sum)+"$"
                if bank_choice not in bank_trans:
                    bank_trans.append(str_sum)
                    bank_trans.append(via_type)
                    bank_trans.append(trans_type)
                    bank_trans.append(bank_choice)
                    how_many -= 1

            elif trans_type == "store":
                store_choice = choice(stores)
                store_sum = random.randint(1, 100)
                str_s = str(store_sum)+"$"
                if store_choice not in bank_trans:
                    bank_trans.append(str_s)
                    bank_trans.append(via[0])
                    bank_trans.append(trans_type)
                    bank_trans.append(store_choice)
                    how_many -= 1
            else:
                human_choice = choice(name) + " " + choice(surname)
                human_sum = random.randint(100, 1000)
                human_str = str(human_sum)+"$"
                if human_choice not in bank_trans:
                    bank_trans.append(human_str)
                    bank_trans.append(via_type)
                    bank_trans.append(trans_type)
                    bank_trans.append(human_choice)
                    how_many -= 1
        return bank_trans
    