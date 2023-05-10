
def addToInventory(inventory, addedItems):
    print("Inventory: ")
    total_items = 0
    for k, v in inventory.items(addedItems):
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total)) 

inv = {'gold coin':42, 'rope':1}

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
