import re
def compress(text):
    lower_text=text.upper()
    # Remove all spaces 
    lower_text= re.sub(r"\s+", "", lower_text, flags=re.UNICODE)
    # print (lower_text)
    return lower_text
def expandedKey(key,p_text_len):
    len_key=len(key)
    if p_text_len>=len_key:
        repeat_index=int(p_text_len /len_key)
        remainder=p_text_len %len_key
        key=key*repeat_index
        if remainder>0:
            remain_key=key[:remainder]
            key=key+remain_key
    else:
        key=key[:p_text_len]
    return key
    # print(repeat_index)
    # print(remainder)
def removepunc(msg):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # Removing punctuations in string
    # Using loop + punctuation string
    for ele in msg:
        if ele in punc:
            msg = msg.replace(ele, "")
    return msg
def encode(msg,key):
    msg=compress(msg)
    msg=removepunc(msg)
    # Expand Key
    print("\tCompressed plaintext :\t "+msg)
    key=expandedKey(key,len(msg))
    print("\t\tExpnded Key : \t "+key)
    cipher_text = []
    for i in range(len(msg)):
        x = (ord(msg[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    cipher=("" . join(cipher_text))
    n = 5
    chunks = [cipher[i:i+n] for i in range(0, len(cipher), n)]
    cipher_text=""
    for x in chunks:
        cipher_text+=x+" "
    return cipher_text

def decode(cipher_text,key):
    cipher_text=compress(cipher_text)
    cipher_text=removepunc(cipher_text)
    key=expandedKey(key,len(cipher_text))
    print("\tCompressed ciphertext :\t "+cipher_text)
    print("\t\tExpnded Key : \t "+key)
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))