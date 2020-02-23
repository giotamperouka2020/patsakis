#task3

items = {
  "milk": 1.4,
  "laptop": 500,
  "potatos": 2
}



def foros(item):
    for x in items:
        items[x] =  items[x] * (1+0.24)
    print(items(item))



