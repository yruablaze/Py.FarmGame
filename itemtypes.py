import random

##when new items are added need to update:
##items.all_items,
##item(object),
##search.item_gather_lists,


class item(object):
    #Star value will alter buy and sell price later
    #edible will affect eating food and cooking later
    def __init__(self, name, sellable, edible, star, buy, sell):
        self.name = name
        self.sellable = sellable
        self.edible = edible
        self.star = star
        self.buy = buy
        self.sell = sell

        
#is this used anywhere?
    def get_name(self):
        return self.name

#required for new buysell page
    def get_price(self):
        return (self.price)

#should work
    def buy_query(self):
        print ("Do you want to buy a " + str(self.name) \
               + " for " + str(self.buy) + " silver?")
        price = self.buy
        return (price)

    #prints list of sellable items and sell price,
    #called by items.sell_query

    #fix this
    def sell_query(self, sellables):
        if self.sellable == True:
            print("You can sell these items:")
            print (str(self.name) + " - " + \
                   str(player.pc.inv_quantity(self.name)))
            sellables.append(1)
            return sellables

        
default_star = 0
##(self, name, sellable, edible, star, buy, sell)        
#raw food  = item("", True, True, default_star, 4.0, 2.0)
blue_berry = item("blueberry", True, True, default_star, 2.0, 1.0)
shijemi = item("shijemi", True, True, default_star, 3.0, 2.0)
apple = item("apple", True, True, default_star, 4.0, 2.0)

#crafted food = item("", True, True, default_star, 4.0, 2.0)
fruit_dish = item("fruit_dish", True, True, default_star, 16.0, 12.0)

#base  = item("", False, False, default_star, 1.0, 0)
twig = item("twig", False, False, default_star, 1.0, 0)
branch = item("branch", False, False, default_star, 3.0, 0)
bark = item("bark", False, False, default_star, 1.0, 0)
stone = item("stone", False, False, default_star, 2.0, 0)
pebbles = item("pebbles", False, False, default_star, 1.0, 0)
dirt = item("dirt", False, False, default_star, 1.0, 0)

#craft = item("", False, False, default_star, 5.0, 0)
string = item("string", False, False, default_star, 5.0, 0)
cloth = item("cloth", True, False, default_star, 15.0, 11.0)
brick = item("brick", True, False, default_star, 4.0, 2.0)
