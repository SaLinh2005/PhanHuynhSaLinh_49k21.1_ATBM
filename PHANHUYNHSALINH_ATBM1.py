# -*- coding: utf-8 -*-

def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # chỉ mã hóa chữ cái
            shift = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - shift + k) % 26 + shift)
        else:
            ciphertext += char  # giữ nguyên nếu không phải chữ
    return ciphertext


if __name__ == "__main__":
    try:
        k = int(input("Nhập số thứ tự (STT): "))
        plaintext = "Phan Huynh Sa Linh"
        ciphertext = caesar_encrypt(plaintext, k)

        print("Bản rõ :", plaintext)
        print("Bản mã :", ciphertext)

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên cho STT.")
