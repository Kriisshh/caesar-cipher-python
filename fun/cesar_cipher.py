"""ceasar cipher technique"""
def welcome():
    '''
    prints the welcome message of this program.
    '''
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    '''

    This function continuously prompts the user for the mode until valid input is entered.
    and it checks if the input is an integer between 0 and 25. If the input is not an integer,
    it prints an error message and prompts again.

    Raises:
        ValueError: If the shift number input is not an integer.

    '''
    while True:
        mode=input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode not in ['e','d']:
            print("invalid mode")
            continue
        message=input(f"What message to {'encrypt' if mode=='e' else 'decrypt'}: ").upper()
        #{} acts as a placeholder
        while True:
            try:
                shift=int(input("What is the shift number: "))
                if 0<=shift<=25:
                    break
                else:
                    print("Invalid Shift")
            except ValueError:
                print ("It Should't be string")
        print(f"('{mode}','{message}',{shift})")
        if mode=='e':
            encrypted_message=encrypt(message,shift)
            print(f'encrypted_message: {encrypted_message}' )
        else:
            decrypted_message=decrypt(message,shift)
            print(f'decrypted_message: {decrypted_message}' )

        break


def encrypt(message,shift):
    '''
    Encrypts a plain text message using the Caesar Cipher technique.
    
    Parameters:
    - message (str): The plain text message to be encrypted.
    - shift (int): The number of positions to shift each letter in the message.
    
    Returns:
    - str: The encrypted message.
    '''

    res_en=""
    for i in message:
        if i.isalpha():
            if i.isupper():
                newchar=chr((ord(i)-65+shift)%26+65)
            else:
                newchar=(chr((ord(i)-97+shift)%26+97))
            res_en+=newchar
        else:
            res_en+=i
    return res_en

def decrypt(message,shift):
    '''    
    Parameters:
    - text (str): The encrypted message to be decrypted.
    - shift (int): The number of positions each letter in the message was shifted.
    
    Returns:
    - str: The decrypted plain text message.
    '''
    res_dec=""
    for i in message:
        if i.isalpha(): #check if it is alphabet letter.
            if i.isupper():
                newchar=chr((ord(i)-65-shift)%26+65)
            else:
                newchar=(chr((ord(i)-97-shift)%26+97))
            #executes first condition if i is uppercase else executes second condition.
            res_dec+=newchar
        else:
            res_dec+=i
    return res_dec



def is_file(fname):
    '''
    checks if file exists
    
    returns:
        true:if file exist.
        false:if file doesn't exist.
    '''
    try:
        with open (fname,'r',encoding='utf-8') as f:
            f.read()
        return True
    except FileNotFoundError:
        return False

def process_file(fname,mode): #fname=filename, mode=encrypt/decrypt.
    '''
    Reads messages from a file, 
    encrypts or decrypts them based on user input, 
    and returns a list of the resulting messages.
  
    Args:
    fname (str): The name of the file to read messages from.
    mode (str): The mode of operation, either 'e' for encryption or 'd' for decryption.

    Returns:
    list: A list containing the encrypted or decrypted messages.

    Raises:
    FileNotFoundError: If the specified file (fname) does not exist.
    ValueError: If the mode is not 'e' or 'd', or 
                if the shift number provided by the user is not an integer.
    '''
    messages=[]
    with open(fname,'r',encoding='utf-8') as p:
        for line in p:
            message=line.strip() #remove white space
            shift = int(input("What is the shift number: "))
            if mode=='e':
                encrypted_message=encrypt(message,shift)
                print(f'encrypted_message: {encrypted_message}' )
                messages.append(encrypted_message)
            else:
                decrypted_message=decrypt(message,shift)
                print(f'decrypted_message: {decrypted_message}' )
                messages.append(decrypted_message)
    return messages


def write_messages(messages):
    '''
    writes message in a file.
    '''
    with open('results.txt','w',encoding='utf-8') as f:
        for message in messages:
            f.write(message +'\n')

# #example:
# write_messages(["david laid", "arnold","zyzz"])



def message_or_file():
    """
    Prompts the user to choose between encrypt or decrypt mode 
    and whether to read input from a file or the console.

    Returns the mode of operation, 
    the message to be encrypted or decrypted (or None if reading from a file), 
    and the filename (or None if reading from the console).

    Returns:
        tuple: A tuple containing the mode, message, and filename.
            - mode (str): The mode of operation, 
              either 'e' for encryption or 'd' for decryption.
            - message (str or None): The message to be encrypted or decrypted,
              or None if reading from a file.
            - filename (str or None): The filename to read from,
              or None if reading from the console.
    """
    while True:
        mode=input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode not in ['e','d']:
            print('invalid mode')
            continue
        while True:
            in_type=input("Would you like to read from a file (f) or the console (c)? ").lower()
            if in_type not in ['f','c']:
                print("Invalid input type")
                continue
            if in_type=="f":
                fname=input("enter the filename: ")
                if not is_file(fname):
                    print("invalid filename")
                    continue
                return mode,None,fname
            else:
                message=input("What message would you like to encrypt or decrypt: ").upper()
                return mode,message,None

def main():
    """
    The main function orchestrates the program's workflow, 
    starting with the `welcome` function to guide the user through the initial setup. 
    It then enters a loop where the user can either process a file containing messages or
    manually input a message to be encrypted or decrypted.

    The program allows for multiple operations without requiring a restart.
    For each operation, the user can specify whether they want to encrypt or decrypt a message,
    and optionally provide a filename for processing.
    The processed messages are written to a file named "result.txt".

    After each operation, the user is prompted 
    to decide whether they wish to perform another operation. 
    If the user chooses 'n', the program terminates; 
    otherwise, it continues to the next operation.

    This function is the central control flow mechanism of the program, 
    ensuring that the user can seamlessly switch between different modes of operation
    and exit the program gracefully when desired.
    """
    welcome()
    while True:
        mode, message, fname= message_or_file()
        if fname:
            messages=process_file(fname,mode)
            write_messages(messages)
            print("i have written output to the file result.txt")
        else:
            shift = int(input("What is the shift number: "))
            if mode=='e':
                encrypted_message=encrypt(message,shift)
                print(encrypted_message)
            else:
                decrypted_message=decrypt(message,shift)
                print(decrypted_message)
        while True:
            choice=input("Would you like to encrypt or decrypt another message? (y/n):").lower()
            if choice not in ['y','n']:
                print("Invalid Choice")
                continue
            if choice=='n':
                print("Thanks for using the program, goodbye!")
                return False
            else:
                break
main()
