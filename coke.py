count = 0 

# Loop until sufficient coins
while count < 50:

    # User inputs coin
    coin = input("Insert Coin:")
    count += float(coin)

    # Programme checks how much until 50 + adds input to total
    if count < 50:
        count_difference = 50 - count
        print(f"Amount Due: {count_difference}")
    else:
        break

# Outputs change due
if count > 50:
    print(f"Change Owed: {count - 50}")