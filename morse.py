import sys

codes = {
        'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-'
    }
    


def main():
    
    
    print("welcome to morse code converter, select from below:")
    choice=input("1.Encryp \n2.Decrypt\n")
    if choice == "1":
        sen = input("Enter the sentence: ").upper()
        print(morse_code_encrypt(sen))
    elif choice == "2":
        try:
            code = input("Enter the code: ")
        except:
            sys.exit("Invalid!")
        
        print(morse_code_decrypt(code))
    else:
        sys.exit("Invalid option!")
    
    

def morse_code_encrypt(s):
    send = ''
    for i in s:
        if i in codes.keys():
            send += codes.get(i) + " "
        if i == " ":
            send += "    " 
    return send
    
    
def morse_code_decrypt(s):
    reverse_dict = {value: key for key, value in codes.items()}
    words = s.split("    ")
    
    decrypted_message = ''
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            decrypted_message += reverse_dict.get(letter, '')
        decrypted_message += " "
    return decrypted_message
        
    
if __name__ == "__main__":
    main()