A = {'Alex', 'Maria', 'Ann', 'Iryna', 'Olena'}
B = {'Ann', 'Olena', 'Mark', 'Ivan', 'Viktoriia'}

all_debtors = A.union(B)
oct_debtors = B.difference(A)

print(f'The debtors for both months: {all_debtors};\nthe debtors for October: {oct_debtors}')
