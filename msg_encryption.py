import cv2
import os

def encrypt_image(image_path, secret_message, password):
    img = cv2.imread(image_path)
    encrypted_img = img.copy()

    key = 0
    for char in password:
        key += ord(char)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                encrypted_img[i, j, k] = (img[i, j, k] + key) % 256

    cv2.imwrite("Encryptedmsg.jpg", encrypted_img)

def decrypt_image(encrypted_path, password):
    encrypted_img = cv2.imread(encrypted_path)
    decrypted_img = encrypted_img.copy()

    key = 0
    for char in password:
        key += ord(char)

    for i in range(encrypted_img.shape[0]):
        for j in range(encrypted_img.shape[1]):
            for k in range(encrypted_img.shape[2]):
                decrypted_img[i, j, k] = (encrypted_img[i, j, k] - key) % 256

    cv2.imwrite("Decryptedmsg.jpg", decrypted_img)

    os.system("start Decryptedmsg.jpg")

# Example Usage:
image_path = "mypic.jpg"
secret_message = input("Enter secret message: ")
password = input("Enter password: ")

# Encryption
encrypt_image(image_path, secret_message, password)

# Decryption
entered_password = input("Enter password for Decryption: ")
if password == entered_password:
    decrypt_image("Encryptedmsg.jpg", password)
    print("Decryption successful!")
else:
    print("Invalid password.")
