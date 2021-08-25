'''create a programa for a paint shop.
the program should ask the size in square meters for the painted area
consider that the coverage of paint is 1 liter for each 3 square meters, and the paint is selled in one can of 18 liters,
that costs R$ 80.00
give me the number of paint cans to be selled and the total price'''

one_liter = 3
one_can = 18
meters = float(input("how many square maters are you going to paint? "))
liters = meters / one_liter
cans = liters / one_can
if cans > 1:
    cans += 1
    print("you'll paint %.2f square meters, using %d cans, total cost: R$%d.00"%(meters, cans, int(cans)*80))
else:
    print("you'll paint %.2f square meters, but using just 1 can, total cost: R$80.00"%meters)

