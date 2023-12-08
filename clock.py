import clock_class

def main():
    print("Welcome to the best clock ever!")
    print('''         .--.
        .-._;.--.;_.-.
       (_.'_..--.._'._)
        /.' . 60 . '.\\
       // .      / . \\\\
      |; .      /   . |;
      ||45    ()    15||
      |; .          . |;
       \\\ .        . //
        \\'._' 30 '_.'/
         '-._'--'_.-'
             `""` ''')
    #getting the basic info
    on = True
    hours, minutes, seconds = input("please enter the info for the clock in the following order:\nhours minutes seconds\nenter only number from 0-24:\n").split(" ")
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    while on:
        for i in hours, minutes, seconds:
            if i > 24:
                print("Please follow instractions! enter only nuber betwwen 0 -24")
                hours, minutes, seconds = input("please enter the info for the clock in the following order:\nhours minutes seconds\nenter only numbers from 0-24:\n").split(" ")
            else:
                on = False

    #creating the clock
    clock = clock_class.Clock(hours, minutes, seconds)
    print('the time is: ', clock.time)

    #creating a menu:
    on = True
    while on:
        order = input('these are the allowed functions:\n-Print time\n-Change value\n-Add to time\n-EXIT\nplease enter a function:')
        if order == "Print time":
            print(clock.get_time())

        elif order == "Change value":
            value_type, value = input("enter what value you would like to change(hours\\minutes\\seconds) and its new value: ").split(" ")
            clock.set_time(value_type, value)
            print(clock.get_time())

        elif order == "Add to time":
            value_type, value = input("enter what value you would like to add to(hours\\minutes\\seconds) and how much to add: ").split(" ")
            clock.add_time(value_type, value)
            print(clock.get_time())

        elif order == "EXIT":
            on = False
            print("Goodbye!")

        else:
            print("please follow instructions!")





if __name__ == '__main__':
    main()
