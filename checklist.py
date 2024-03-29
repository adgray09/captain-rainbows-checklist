checklist = list ()

#Create
def create(item):
    checklist.append(item)

#Read
def read(index):
    return checklist[index]

#Update
def update(index, item):
    checklist[index] = item

#Destroy
def destroy(index):
    checklist.pop(index)

#for list_items in checklist:

def list_all_items():
    index = 0 
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1 

def marked_completed():
    for list_item in checklist:
        print ("√ {}".format(list_item))

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index number?")
        
        read(int(item_index))

    elif function_code == "P":
        list_all_items()
        
    elif function_code == "Q":
        return False   

    elif function_code == "U":
        update_index = user_input("Index number?")
        update_name = user_input("New name")
        update(int(update_index), update_name)

    elif function_code == "D":
        index = int(user_input("index:"))
        destroy(index)

    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

#Test
#def test():
    #list_all_items()

   # create("purple sox")
   #create("red cloak")

   # print(read(0))
    #print(read(1))

   # update(0, "purple socks")
    #destroy(1)
    
    #print(read(0))
    #print(read(1))
    #list_all_items()
    #select("C")
    #list_all_items()
    #select("R")
    #list_all_items()

    #user_value = user_input("Please Enter a Value:")
    #print(user_value)

#test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, U to update, R to Read from list, P to display list, D to destroy, and Q to quit")
    running = select(selection)
    marked_completed()



