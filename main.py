from execjs import compile as js_compile
import re
import json
import requests

class Encryptor:
    def __init__(self):
        self._cipher = js_compile(open("cipher_value.js").read())

    def encrypt_value(self, password, num, key) -> str:
        return self._cipher.call("encrypt", password, num, key)
    
class OutlookCipher:
    def __init__(self) -> None:
        pass

    def __values__(self) -> None:
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'es',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }

        r = requests.get("https://signup.live.com/signup?lic=1", headers=headers)
        matches = re.findall(r'Key="(.*?)"; var randomNum="(.*?)"', r.text)
        for match in matches:
            key, number = match
            print(f"Key: {key}\n\nNumber: {number}\n")
            return key, number

if __name__ == "__main__":
    i = OutlookCipher()
    key, number = i.__values__()

    encryptor = Encryptor()
    encrypted_value = encryptor.encrypt_value("H4cK3dR4Du", number, key)
    print("Cipher Value:", encrypted_value)