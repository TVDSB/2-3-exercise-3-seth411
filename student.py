def main():
    #your code goes here
    
    number = int(input("enter a number:"))

    if (number%3) == 0 and (number%5) == 0:
      print("fizzbuzz")

    elif (number%5) == 0:
      print("buzz")

    elif (number%3) == 0:
      print("fizz")

    else:
      print(number)
if __name__ =='__main__':
    main()
