import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# url = "https://jsonplaceholder.typicode.com/posts"
# params = {
#     "userId": 1
# }
# response = requests.post(url, params=params)

if response.status_code == 200:
    data = response.json()
    # print(data)
    # df = pd.DataFrame(data=data)
    # print(df.head)
    df = pd.json_normalize(data=data)
    df.to_csv('users.csv',index=False)
    print(df[['id', 'name', 'username', 'email','address.city', 'address.geo.lat']])
else:
    print('Status Code Failed: ', response.status_code)


