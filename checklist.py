print("Hello World")

checklist = list()
#checklist.append('Blue')
print(checklist)
#checklist.append('Orange')
print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    item = checklist[index]
    return item
#checklist = ['Blue', 'Orange']
#checklist[1] = 'Cats'
print(checklist)

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

#for list_items in checklist:

def list_all_items():
    index = 0 
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1 

def select (function_code):
    if function_code == "C":
        input_item = user_input("input item:")
        create(input_item)

    elif function_code == "R":
        item_idex = user_input("index number?")

    elif function_code == "P":
        list_all_items()

    else:
        print("unknown option")

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    
    destroy(1)

    print(read(0))
    #print(read(1))
    
    list_all_items()

test()


