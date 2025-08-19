import requests
from client import api_key
from db_connector import get_connection

connection = get_connection()
cursor = connection.cursor()

def electric_car():
    user_id, uddi, serviceKey = api_key()
    url = f"http://api.odcloud.kr/api/{user_id}/v1/uddi:{uddi}"

    params = {
        'serviceKey': serviceKey,
        'page': 1,
        'perPage': 600
    }

    response = requests.get(url, params=params)
    datas = response.json()

    relationship = {}
    for data in datas['data']:
        city, town = data['시군구별'].split()[:2]
        type_list = '승용_승합_화물_특수'
        for t in type_list.split('_'):
            key = city + '_' + town + '_' + t
            try:
                relationship[key] += data[t]
            except:
                relationship[key] = data[t]
        
    for key in relationship.keys():
        query_value = "'" + key.replace("_", "', '") + "', " + str(relationship[key])
        query = f"insert registed_car (city, town, type, total, local_regist) values ({query_value}, 'N')"
        cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()
electric_car()