# ----------------------------------------------------------------
# HOMEWORK
# ----------------------------------------------------------------
# A machine sells bottles of Coca-Cola for 50 cents and only
# accepts coins in these denominations:
#     25 cents, 10 cents, and 5 cents.

# Write a program that prompts the user to insert a coin, one at a
# time, each time telling the user the amount still due.

# Once the user has inserted at least 50 cents, output how many
# cents in change the user is owed.

# UPGRADED RULES (new in this version):
#   - If the user enters a coin that is NOT 5, 10, or 25, the
#     machine REJECTS it and RETURNS it, printing a message. The
#     amount due does not change.
#   - The user's input must be a whole number (integer). If they
#     type letters or a decimal (like "abc" or "2.5"), print an
#     error and ask again — the program must NOT crash.

# Messages used:
#   - Prompt:           "Insert Coin: "
#   - Not an integer:   "Please insert a valid integer coin"
#   - Rejected coin:    "Coin not accepted. Returning <n> cents"
#   - Still owed:        "Amount Due: <n>"
#   - End:              "Change Owed: <n>"


# ----------------------------------------------------------------
# ABOUT `continue`
# ----------------------------------------------------------------
# `continue` is like `break`'s cousin:
#   - break    -> EXIT the loop completely.
#   - continue -> SKIP to the next round of the loop.

# Here we use continue to ignore invalid input cleanly, without
# wrapping the whole rest of the loop in a big if-block.


# ----------------------------------------------------------------
# EXAMPLE RUNS
# ----------------------------------------------------------------

# Run 1 — non-integer, then a rejected coin, then valid coins:
#     Insert Coin: abc
#     Please insert a valid integer coin
#     Insert Coin: 30
#     Coin not accepted. Returning 30 cents
#     Amount Due: 50
#     Insert Coin: 25
#     Amount Due: 25
#     Insert Coin: 25
#     Change Owed: 0

# Run 2 — exact payment with two quarters:
#     Insert Coin: 25
#     Amount Due: 25
#     Insert Coin: 25
#     Change Owed: 0

# Run 3 — decimal rejected, then overpay by 10:
#     Insert Coin: 2.5
#     Please insert a valid integer coin
#     Insert Coin: 25
#     Amount Due: 25
#     Insert Coin: 10
#     Amount Due: 15
#     Insert Coin: 25
#     Change Owed: 10

# Run 4 — dimes then a quarter (overpay by 5):
#     Insert Coin: 10
#     Amount Due: 40
#     Insert Coin: 10
#     Amount Due: 30
#     Insert Coin: 10
#     Amount Due: 20
#     Insert Coin: 25
#     Change Owed: 5



# Solution: 
amount_due = 50

while amount_due > 0:
    coin = input("Insert Coin: ")

    if not coin.isdigit():
        print("Please insert a valid integer coin")
        continue

    coin = int(coin)

    if coin not in [5, 10, 25]:
        print(f"Coin not accepted. Returning {coin} cents")
        print(f"Amount Due: {amount_due}")
        continue

    amount_due -= coin

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

print(f"Change Owed: {abs(amount_due)}")