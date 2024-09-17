"""
Problem Statement:
1. *Create a function* that takes an array, an index, and a value as parameters.
    Inside the function, use the insert method to insert the value at the specified index in the array.
    Return the modified array.
2. *Implement a simple shopping cart program* using an array.
    Create functions to add items, remove items, and update quantities using array methods.
    Print the cart's contents after each operation.
3. *Write a program* that uses a while loop to print the first 25 integers.
4. *Write a program* that uses a while loop to print the first 10 even numbers.
5. *Create a function* that takes a positive integer as a parameter and
    uses a while loop to calculate and return the factorial of that number.
6. *Write a program* that has an array of numbers; if the number is negative,
    it should remove the negative number from the array.
7. *Create a function* that takes an array of numbers as a parameter.
    Use a while loop to calculate and return the sum of all the numbers in the array.
8. *Implement a program* that takes a list of temperatures in Celsius as input from the user.
    Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store
    the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.
9. *Write a program* to remove all the odd numbers from an array.
"""

while True:
    print("\n1: Take array, index, and a value as parameter.")
    print("2: Shopping cart using an array.")
    print("3: while loop to print first 25 integers.")
    print("4: while loop to print first 10 even numbers.")
    print("5: Use while loop and return factorial.")
    print("6: Remove the -ve numbers from array.")
    print("7: while loop to calculate sum of numbers in array.")
    print("8: Convert Celsius to Fahrenheit.")
    print("9: Remove odd numbers from array.")
    print("   Enter '0' to exit.")

    choose = (input("\nEnter your choice : "))
    match choose:
        case "1":
            """
                1. *Create a function* that takes an array, an index, and a value as parameters.
                    Inside the function, use the insert method to insert the value at the specified index in the array.
                    Return the modified array.
            """
            num:list= [1, 2, 3, 4, 6, 7, 8, 9, 10]
            print(f"By default List items : \n{num}")
            def funs( num ):
                num.insert(4, 5)
                return num
            print(f"\nList items after adding at specific index: \n{funs(num)}")

        case "2":
            """
                2. *Implement a simple shopping cart program* using an array.
                    Create functions to add items, remove items, and update quantities using array methods.
                    Print the cart's contents after each operation.
            """
            cart_ar : list = []
            def carts_items(cart_ar):
                while True:
                    print("\nEnter 1 to see the cart : ")
                    print("Enter 2 to add items in the cart : ")
                    print("Enter 3 to remove items from the cart : ")
                    print("Enter 'q' to exit.")

                    choice = input("Enter your choice : ")
                    if choice == "q":
                        break

                    elif choice == '1':
                        if cart_ar:
                            print(f"\nYour cart items are : {cart_ar}")
                            print(f"Total number of items is cart : {len(cart_ar)}")

                        else:
                                print("\nCart is empty.")

                    elif choice == '2':
                        items = input("Enter items in cart : ")
                        cart_ar.append(items)
                        

                    elif choice == '3':
                        items = input("\nEnter name of items you want to remove : ")
                        cart_ar.remove(items)
                        print(cart_ar)

            carts_items(cart_ar)

        case "3":
            """
                3. *Write a program* that uses a while loop to print the first 25 integers.
            """
            digit : int = 1
            while digit <= 25:
                for i in range(1, 26):
                    print(f"Integer No. {i} ==> : {digit}")
                    digit += 1

        case "4":
            """
                4. *Write a program* that uses a while loop to print the first 10 even numbers.
            """
            # ever_num : int = 0
            # for i in range(1, 21):
            #     while i % 2 == 0:
            #         print(i)
            #         i += 1

            print("Using while loop : \n")
            num = 2
            while num <= 21:
                for i in range(1, 11):
                    print(f"Even No : {i} ===> {num}")
                    num += 2

        case "5":
            """    
                5. *Create a function* that takes a positive integer as a parameter and
                    uses a while loop to calculate and return the factorial of that number.
            """
            def factorial( ):
                factorial : int = 1

                n : int = int(input("\nEnter a number to finf factorial : "))

                if n < 0 :
                    print("Factorial of -ve nums is not available.")

                elif n == 0 :
                    print("Factorial of '0' is 1.")

                else:
                    for i in range(1, n + 1):
                        factorial = factorial * i
                    
                    print(f"\nFactorial of {n} is : {factorial}")

            # Calling the function
            factorial()

        case "6":
            """
                6. *Write a program* that has an array of numbers; if the number is negative,
                    it should remove the negative number from the array.
            """

            def remov_nums(nums_arr):

                num_arr = []
                for num in nums_arr:
                    if num >= 0:
                        num_arr.append(num)
                return num_arr

            num_arr = [1, -2, -3, -4, 5, -6, 7, -8, 9]
            print(f"Mixed Numbers    : {num_arr}")
            new_nums = remov_nums(num_arr)
            print(f"Positive Numbers : {new_nums}")


            # num_arr : list = [1, 2, -3, -4, -5, 6, 7, -8, 9, 10, -11, 12, -13, 14, -15]
            # print(f"\nArray of both +ve and -ve numbers : \n{num_arr}")

            # num = 0
            # while num < len(num_arr):
            #     for num in num_arr:
            #         if num < 0:
            #             num_arr.remove(num)
            #         else:
            #             num += 1
            # print(f"\nUpdated array of +ve numbers : \n{num_arr}")

        case "7":
            """
            7. *Create a function* that takes an array of numbers as a parameter.
                Use a while loop to calculate and return the sum of all the numbers in the array.
            """

            num_arr : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            def sumArr(num_arr):
                sum = 0
                while sum <= len(num_arr):
                    for i in num_arr:
                        sum = sum + i
                print(f"\nSum of given array : {sum}")

            # Calling the function
            sumArr(num_arr)

        case "8":
            """
            8. *Implement a program* that takes a list of temperatures in Celsius as input from the user.
                Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store
                the converted temperatures in an array. Use a while loop to perform the conversion for 
                each temperature.
            """
            def temp_conv():
                while True:
                    tempArr : list = [ ]
                    temp_c = input("Enter temperature in Celcius or 'q' to quit : ")
                    if str(temp_c) == str('q'):
                        break
                    else:
                        tempArr.append(float(temp_c))
                        print(f"\nTemperature in celcius    : {tempArr}")
                        temp_f = 0
                        # print(len(num_arr))
                        while temp_f <= len(tempArr):
                            for temp_celc in tempArr:
                                temp_f = ((float(temp_celc) * 9/5) + 32)
                                tempF : list = []
                                tempF.append(temp_f)
                                print(f"Temperature in fahrenhiet : {tempF}\n")

            # Calling the function
            temp_conv()

        case "9":
            """
                9. *Write a program* to remove all the odd numbers from an array.
            """
            num_arr : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            print(f"Array of mixed numbers : \n{num_arr}")

            num = 0
            for num in num_arr:
                if num % 2 == 1:
                    num_arr.remove(num)
            print(f"\nOdd numbers are removed from array : \n{num_arr}")

        case "0":
            break

        case Default:
            print("\nSelect 1 to 9 numbers, or '0' to quit.\n")
