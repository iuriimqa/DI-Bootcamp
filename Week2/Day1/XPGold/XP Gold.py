print('Hello world '*4+'I love python '*4)

season = input('Please input your month ')
season = int(season)

if season >= 6 and season <=8:
    print("This is Summer")
elif season >= 3 and season <=5:

    print("This is Spring")
elif season >= 9 and season <=11:
    print("This is Autumn")

else:
    print("This is Winter")
