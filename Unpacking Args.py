def Healt_calc(age, apples, cig):
    health = (100-age) + apples*2 - (cig*2.8)
    print(health)


Healt_calc(22,5,7)
venkat_data = [22,5,7]
Healt_calc(venkat_data[0],venkat_data[1],venkat_data[2])


Healt_calc(*venkat_data)  # UNPACKING ARGUMENT