# ################################################################
# #   PROBLEM 2: WAREHOUSE ORDER PROCESSOR
# ################################################################

# ----------------------------------------------------------------
# PROBLEM
# ----------------------------------------------------------------
# A warehouse system ships orders against its inventory.
# inventory = {"laptop": 5, "mouse": 10, "keyboard": 0}
#     orders = [
#         ("laptop", 2),
#         ("mouse", 15),
#         ("keyboard", 1),
#         ("monitor", 3),
#     ]

# Loop through the orders.
# Use MATCH with guarded patterns:
#   - product not in inventory -> "<product>: not in inventory"
#   - enough stock             -> ship it, reduce inventory, print
#                                 "<product>: shipped <qty>, <left> left"
#   - not enough stock         -> "<product>: only <stock> in stock,
        
#                         cannot ship <qty>"

# Expected output:
#     laptop: shipped 2, 3 left
#     mouse: only 10 in stock, cannot ship 15
#     keyboard: only 0 in stock, cannot ship 1
#     monitor: not in inventory

# Solution:

inventory = {"laptop": 5, "mouse": 10, "keyboard": 0}
orders = [
        ("laptop", 2),
        ("mouse", 15),
        ("keyboard", 1),
        ("monitor", 3),
    ]

for product, qty in orders:
    match (product, qty):

        case (product, qty) if product not in inventory:
            print(f"{product}: not in inventory")

        case (product, qty) if inventory[product] >= qty:
            inventory[product] -= qty
            print(
                f"{product}: shipped {qty}, "
                f"{inventory[product]} left"
            )

        case (product, qty):
            print(
                f"{product}: only {inventory[product]} in stock, "
                f"cannot ship {qty}"
            )