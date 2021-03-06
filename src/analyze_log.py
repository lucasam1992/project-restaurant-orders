import csv


def read_csv(data):
    with open(data) as csv_file:
        reader_datas = csv.reader(csv_file, delimiter=",", quotechar='"')
        return[index for index in reader_datas]


# https://app.betrybe.com/course/computer-science/estrutura-de-dados-i/hashmap-e-dict/aee34d10-0053-49a1-85e3-decc63b90543/conteudo/e0c7c2c3-3ac8-4262-81ce-6d5c43ec2fb1/resumo-do-conteudo-e-resolucao-de-problemas/233931d0-f85e-4389-9994-d7ab1d008c94?use_case=side_bar
def favorite_maria_food(data):
    count = {}
    most_frequent = data[0]
    for food in data:
        if food == "maria":
            if food not in count:
                count[food] = 1
            else:
                count[food] += 1

            if count[food] > count[most_frequent]:
                most_frequent = food

    return most_frequent[1]


def arnaldo_eat_hamburguer(data):
    count = 0
    for food in data:
        if food[0] == "arnaldo" and food[1] == "hamburguer":
            count += 1
    return count


def joao_not_eat(data):
    aux_all_customers = []
    aux_joao = []
    for food in data:
        aux_all_customers.append(food[1])
        if food[0] == "joao":
            aux_joao.append(food[1])

    make_intersection = set(aux_all_customers).difference(set(aux_joao))

    return make_intersection


def joao_not_eat_day(data):
    aux_all_customers = []
    aux_joao = []
    for food in data:
        aux_all_customers.append(food[2])
        if food[0] == "joao":
            aux_joao.append(food[2])

    make_intersection = set(aux_all_customers).difference(set(aux_joao))

    return make_intersection


def analyze_log(path_to_file):
    get_csv = read_csv(path_to_file)
    maria_order_frequent = favorite_maria_food(get_csv)
    arnaldo_ask_hamburguer = arnaldo_eat_hamburguer(get_csv)
    joao_not_ask = joao_not_eat(get_csv)
    day_joao_not_eat = joao_not_eat_day(get_csv)
    with open('data/mkt_campaign.txt', mode='w') as arq:
        arq.write(maria_order_frequent + '\n')
        arq.write(str(arnaldo_ask_hamburguer) + '\n')
        arq.write(str(joao_not_ask) + '\n')
        arq.write(str(day_joao_not_eat) + '\n')
