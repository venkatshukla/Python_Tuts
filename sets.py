shopping = {'Milk', 'Cheese','Butter'}
shopping.add('Milk')
shopping.add('Milk')

if 'Bread' not in shopping:
    shopping.add('Bread')

print(shopping)

for i in shopping:
    print(i)