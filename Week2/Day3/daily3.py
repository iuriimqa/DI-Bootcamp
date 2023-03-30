# # Daily1
# # Challenge 1
# # Ask a user for a word
# # Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# #
# # Make sure the letters are the keys.
# # Make sure the letters are strings.
# # Make sure the indexes are stored in a list and those lists are values.
#
# sample_dict = {}
# word = input("Please input word ")
# for i, letter in enumerate(word):
#
#     if letter in sample_dict:
#         sample_dict[letter].append(i)
#     else:
#         sample_dict[letter] = []
#         sample_dict[letter].append(i)
# print(sample_dict)

# # Daily2
# # Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# # Sort the list in alphabetical order.
# # Return “Nothing” if you can’t afford anything from the store.
#
#
# def calculate_purchases(items_prices: dict[str, str], wallet: str) -> list | str:
#
#     wallet_updated = wallet.strip("$")
#     wallet_updated = wallet_updated.replace(",", "")
#     wallet = int(wallet_updated)
#
#     can_purchase = []
#
#     for item, price in items_prices.items():
#         price_updated = price.strip("$")
#         price_updated = price_updated.replace(",", "")
#         items_prices[item] = int(price_updated)
#
#         if items_prices[item] <= wallet:
#             can_purchase.append(item)
#             wallet -= items_prices[item]
#
#     return sorted(can_purchase) if can_purchase else "Nothing"
#
# # 1
# items_purchase1 = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
#
# # 2
# items_purchase2 = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }
#
# # 3
# items_purchase3 = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }
#
# wallet1 = "$300"
# wallet2 = "$100"
# wallet3 = "$1"
#
# print(calculate_purchases(items_purchase1, wallet2))
# print(calculate_purchases(items_purchase2, wallet2))
# print(calculate_purchases(items_purchase3, wallet1))