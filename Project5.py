import pprint

inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
        print("%s %d"%(k,v))
        total += v
    return(total)

def addToInventory(inventory, addedItems):
    newItems = {}
    for i in addedItems:
        if i not in newItems:
            newItems[i] = 1
        else:
            newItems[i] += 1
    for i in newItems:
        if i in inventory:
            inventory[i] += newItems[i]
        else:
            inventory[i] = newItems[i]
    return(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

newInventory = addToInventory(inventory, dragonLoot)
total = displayInventory(newInventory)
print("Total number of items: " + str(total))
