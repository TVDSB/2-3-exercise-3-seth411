def main():
    #your code goes here
    print("0")
    number = int(input("enter a number:\n"))

    if (number%3) == 0 and (number%5) == 0:
      print("fizzbuzz")

    elif (number%5) == 0:
      print("buzz")

    elif (number%3) == 0:
      print("fizzbuzz")

    else:
      print(number)
if __name__ =='__main__':
    main()
