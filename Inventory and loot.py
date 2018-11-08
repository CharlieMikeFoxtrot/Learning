
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 

def printinventory(inventory):
    print('Inventory'.center(24,'='))
    total = 0
    for k,v in inventory.items():
        print (str(v).ljust( 12 ,'.'), k)
        total+= v
    print('Total number of items: ' + str(total))
    

def addtoinv(inventory, addedItem):
    for i in addedItem:
        if i in inventory:
            inventory[i] += 1
            print('Looted %s. You now have %s  %s\'s' % (str(i),str(inventory[i]),str(i)))
        else:
            inventory[i] = 1
            print(('You found a new item, you now have A %s') % (str(i)))

    
    
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addtoinv(inventory , dragonLoot)
printinventory(inventory)
