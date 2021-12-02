l1 = [i for i in range(10)]
l2 = [i**2 for i in range(10)]
l3 = [i*2 for i in range(10)]

ll = [("l",i) for i in [l1, l2, l3]]

import pprint
table_header = ["keys", "values"]
exp_table = [
    (str(k), pprint.pformat(v)) for k, v in ll if not k.startswith("_")
]
from tabulate import tabulate
ret = tabulate(exp_table, headers=table_header, tablefmt="fancy_grid")
print(ret)