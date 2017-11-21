while True:
    try:
        number = int(input("Whats you fav number??\n"))
        print(12/number)
        break
    except ValueError:
        print("Make sure you enter a number")
    except ZeroDivisionError:
        print("Dont pick 0")
    except:
        break
    finally:
        print("Byeeeee!")

