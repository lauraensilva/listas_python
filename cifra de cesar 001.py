def encrypt(text, s):
    result = "";
    for i in range(len(text)):
        char = text[i]
        if char.isupper() :
                result += chr(ord(char) + s-65) ;
        else:
             result += chr(ord(char) + s - 97 );
    return result;
print(encrypt("ABCDEF", 1));