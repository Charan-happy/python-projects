#a Gui application to enscrypt and decrypt a message using python
#if user chooses encrypt a message the user's message must be tranformed into secret code
#if user chooses decrypt a message then it converts secret code into a meaningful message

#the basic idea of achieving this is reversing the letters according to user input

#a/c to user input we need to write an event program because the operation of the program depends on the user input.
#here we can use the dialogue box to get user input and the info box to show the encrypted and decrypted message to the user.
# the program will continue to run until when the user gives other than "encrypt" and "decrypt"

#main code
from collections import Counter
from tkinter import messagebox, simpledialog, Tk
import tkinter
def is_even(number):
    return number %2 == 0
def get_even_letters(message):
    even_letters= []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters=[]
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list=[]
    if not is_even(len(message)):
        message=message+'x'
    even_letters=get_even_letters(message)
    odd_letters=get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[Counter])
    new_message=' '.join(letter_list)
    return new_message

def get_task():
    task=simpledialog.askstring('Task','Do you want to encrypt or decrypt?')
    return task

def get_message():
    message=simpledialog.askstring('Message','Enter the secret message:')
    return message
root = Tk()
while True:
    task=get_task()
    if task=='encrypt':
        message=get_message()
        encrypted=swap_letters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    elif task == 'decrypt':
        message=get_message()
        decrypted=swap_letters(message)
        messagebox.showinfo('plaintext of the secret message is : ',decrypted)
    else:
        break
root.mainloop()