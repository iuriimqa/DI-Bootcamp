alpha = 'אבגדה'
# 1
heb_dict = {}
for i, char in enumerate(alpha):
    heb_dict[i] = char

# 2
heb_dict = dict(enumerate(alpha))   

print(heb_dict[4])