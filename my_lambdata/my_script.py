
# my_script.py

import pandas 

from my_lambdata.my_mod import check_nulls


print('HAPPY TUESDAY NIGHT')

df = pandas.DataFrame({'x':[1,2,3], 'y':[4,5,6]})
print(df.head())

x = df
print("number of null values", check_nulls(x))
