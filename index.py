from pprint import pprint
from unicodedata import name
from dataset import users, countries
users_wrong_password = []
girls_drivers = []
max_salary = 0
dict_job ={}
big_salary = 0
best_occupation = {}
car_owner_counter = 0
flights_counter = 0
avg_flights = 0
vip_user = None
list_el = []


#Point 1. Плохие пароли
for user in users:
    try:
        check = int(user['password'])
    except ValueError:
        # print('Error chooesen correct password')
        pass
    else:
        dict_el = dict(name = user['name'], mail = user['mail'])
        users_wrong_password.append(dict_el)


#Point 2. Женщины водители
for user in users:
    if user.get('friends', '') != '':
        for friend in user['friends']:
            if friend['sex'] == 'F' and friend.get('cars', '') != '' :
                friend_name = friend['name']
                girls_drivers.append(friend_name)   


#Point 3. Лучшая профессия
for user in users:
    if user.get('friends', '') != '':
        for friend in user['friends']:
            if friend.get('job', '') != '':
                salary  = friend['job']['salary']
                if salary > max_salary:
                    max_salary = salary  
                    best_occupation = friend['job'].copy()



#Point 4. Самый влиятельный пользователь           
for user in users:
    salary_1 = 0
    if user.get('friends', '') != '':
        for friend in user['friends']:
            if friend.get('job', '') != '':
                salary_1 += friend['job']['salary']
        if salary_1 > big_salary:
            big_salary = salary_1
            vip_user = user['name']


#Point 5. Путешественники
for user in users:
    if user.get('friends', '') != '':
        for friend in user['friends']:
            if friend.get('cars','') != '':
                car_owner_counter += 1
                if friend.get('flights','') != '':
                    for fly_atr in friend['flights']:
                        if fly_atr.get('airport'):
                            flights_counter += 1
avg_flights = round((flights_counter/car_owner_counter),5)


#Point 6. Чистка списка users               
for user in users:
    if user.get('friends', '') == '':
        list_el.append(user)
    elif user.get('friends', '') != '':
        for friend in user['friends']:
            if friend.get('flights', '') == '':
                list_el.append(user)
            elif friend.get('flights', '') != '':  
                for fly_atr in friend['flights']:
                    if fly_atr['country'] not in countries:
                        list_el.append(user)

users = list_el

# print(users_wrong_password)
# print(girls_drivers)
# print(best_occupation)
# print(vip_user)
# print(avg_flights)
# print(users)
