from cryptography.fernet import Fernet
from pyodide import create_proxy
import sys

from js import alert, document

def p(*s: str):
    for i in s:
        sys.stdout.write(i)

# EPB-y60D3qJaBI1n0cShTNy2-CwwzMdb69lhuf8Dm0I=
def generate_key():
    key = Fernet.generate_key()
    return key.decode('utf-8')

def encrypt(key: str, message: str):
    f = Fernet(key.encode('utf-8'))
    encrypted = f.encrypt(message.encode('utf-8'))
    return encrypted

input_message = Element("str")
input_key = Element("key")

enc_mode = document.getElementById("enc_mode")
dec_mode = document.getElementById("dec_mode")
out = document.getElementById("out")

inp_out = document.getElementById("str")
inp_out_key = document.getElementById("key")

def set_mode_enc(mode):
    sys.stdout.write("Encrypting")

def set_mode_dec(mode):
    sys.stdout.write("Decrypting")

def payload(ao):
    global out
    p('Sending payload')
    key = input_key.value
    message = input_message.value
    if key == "":
        alert("Please enter an encryption key")
        return
    if message == "":
        alert("Please enter a string to encrypt")
        return
    try:
        encrypted = encrypt(key, message)
        out.readonly = False
        out.innerHTML = encrypted.decode('utf-8')
        out.readonly = True
        p(out.innerHTML)
    except ValueError as e:
        alert("Invalid encryption key: " + str(e))
    except Exception as e:
        alert("Error: " + str(e))
    p('Payload sent')
    # p(*out.__dir__())
function_proxy = create_proxy(payload)

document.getElementById("submit_btn").addEventListener("click", function_proxy)

enc_mode_proxy = create_proxy(set_mode_enc)
enc_mode.addEventListener("click", enc_mode_proxy)

dec_mode_proxy = create_proxy(set_mode_dec)
dec_mode.addEventListener("click", dec_mode_proxy)
