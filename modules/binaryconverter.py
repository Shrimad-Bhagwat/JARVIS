print("\n\t\t\t\t\tWelcome")
decision='y'
while decision=='y':
    
    print("__"*50,"\n")


    print("\t1:Encode\n\t2:Decode\n")

    choice=int(input("Enter your choice: "))
    if choice == 1:

        #Encoded
        a=input("\tEnter : ")
        x=(' '.join(format(ord(x), 'b') for x in a))
        print("\tEncoded : ",x)
        print( "\n" )
    elif choice == 2:


        #Decoded
        q=input("\tEnter : ")
        z=str(q)
        binary_values = z.split()
        ascii_string = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character
        print('\tDecoded : ',ascii_string)
    decision=input("Do you want to continue?y/n  ").lower()