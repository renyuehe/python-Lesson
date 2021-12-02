
ll = {i: i**2 for i in range(10)}


from tabulate import tabulate
print(tabulate([*ll.items()]))

