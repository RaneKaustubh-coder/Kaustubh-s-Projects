contact_book = {} # Empty Dictionary
while True: # Forever Loop
    try: # Error Handling
        menu = int(input('[1] - New Contact | [2] - Get Contact | [3] - Exit\n')) # Ask what user want to do.
        if menu == 1: # if this is true 
            ask_user_name = input('Type name: ') # Ask user about Contact Name.
            ask_user_number = input('Type number: ') # Ask user about Contact Number
            if len(ask_user_number) != 10: # Check their are total 10 digits in contact number.
                print('Number must be exactly 10 digits.') # print this message.
            else: # else
                try: # Error Handling
                    contact_book[ask_user_name] = int(ask_user_number) # Add contact to Empty Dictionary.
                    print('Successfully added New Contact Number.') # And print this message.
                except ValueError: # If error occurs
                    print('Type only numbers!!') # Print this message.
        elif menu == 2: # if this condition is true
            get_contact = input('Type Name: ') # Ask user about Contact Name
            if get_contact in contact_book: # check if it is in our dictionary.
                print(get_contact, contact_book[get_contact]) # Print Contact Name and Number.
            else: # else
                # Print these messages
                print('This contact Does not Exists!')
                print('To add new contact press 1.')
        else: # if everything is done then 
            break # use break to get out of that loop.
    except ValueError: # if error occues
        print('Enter Valid Input! Only number between (1 - 3).') # print this message
print('Thankyou!') # At the ent print this message.
