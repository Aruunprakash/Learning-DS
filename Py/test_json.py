book={}
book["tom"]={"name":"Tom",
             "age":25,
             "phone":89876554
             }
book["bob"]={"name":"Bob",
             "age":31,
             "phone":987654321}

import json
s=json.dumps(book)
print(s)
print(type(s))
with open('/Users/arunmp/git/Learning-DS/Py/book.txt', 'w') as f:
    f.write(s)