import database_utils.get_data

res = database_utils.get_data.get_r2_data()
data = []
for i in res:
    data.append([i[0],i[1]])
print(data)