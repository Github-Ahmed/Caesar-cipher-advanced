from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(user_text, user_shifts, user_direction):
    answer = ""
    if user_direction == 'decode':
        user_shifts *= -1
    for char in user_text:
        if char not in alphabet:
            answer += char
            continue
        index = alphabet.index(char)
        new_index = index + user_shifts
        answer += alphabet[new_index]

    print(f"The {user_direction}d text is: {answer}.")

repeat = "yes"
while repeat == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26
    caesar(text, shift, direction)
    
    ask_repeat = input("\nType 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if ask_repeat == 'no':
        print("\nGoodbye!")
        repeat = "no"

#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
