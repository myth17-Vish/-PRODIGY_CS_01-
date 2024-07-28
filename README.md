
# ProdigyInfo-Intern-Task
 
Task No.1:- Implement Casesar Cipar.

     A python program that can encrypt and decrypt text using the Caesar Cipher algorithm.
     Allow users to input a message and a shift value to perform encryption and decryption.

Here's how the program works:

    1.The caesar_encrypt function takes a message and a shift value as input, and returns the encrypted message. It iterates through each character in the message, and if the character is a letter, it shifts it by the specified amount using the ASCII values of the characters.

    2.The caesar_decrypt function is similar, but it shifts the characters in the opposite direction to decrypt the message.

    3.The main function is the entry point of the program. It presents a menu to the user, allowing them to choose between encrypting a message, decrypting a message, or quitting the program.

    4.If the user chooses to encrypt or decrypt a message, they are prompted to enter the message and shift value. The program then calls the appropriate function to perform the encryption or decryption, and prints the result.

You can copy this code to a file (e.g. T1_caesar_cipher.py) and run it using Python (e.g. python T1_caesar_cipher.py). Then, follow the prompts to encrypt or decrypt a message!


Task No.3:- Password Complexity Chacker 

    A Tool that assesses the strength of a password based on criteria such as lengh,presence of uppercase and lowercase letters,numbers, and special characters. Provide feedback to users on the passwords's strength.

Here's how the program works:

    1.The assess_password_strength function takes a password as input, and returns a string indicating the password's strength. It calculates a score for each of the criteria mentioned above, and then determines the overall strength based on the total score.

    2.The main function is the entry point of the program. It presents a menu to the user, allowing them to choose between assessing a password or quitting the program.
    
    3.If the user chooses to assess a password, they are prompted to enter the password. The program then calls the assess_password_strength function to determine the password's strength, and prints the result.

You can save this code to a file (e.g. T3_password-strength.py) and run it using Python (e.g. python T3_password-strength.py). Then, follow the prompts to assess a password's strength!
