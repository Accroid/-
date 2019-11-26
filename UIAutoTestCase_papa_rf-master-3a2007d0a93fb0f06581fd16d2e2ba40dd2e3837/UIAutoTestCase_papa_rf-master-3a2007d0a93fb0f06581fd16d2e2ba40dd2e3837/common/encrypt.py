#coding=utf-8


import rsa
import base64
def encrypt(message):
    # message = '18143488220'
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(b"""-----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCl88KDodsoi5be7uSFPt8m5ezx
    DEWz+eP616I44LZRgR5SzE54jeF9Af4QbMFOlBcIb2QjxfV5rO7RWxMbb8QfqFCL
    lcL/0pw5GQVn+RVUQZDh0sg/iPAIRBEcedhYO/d7iC/GmJ/oUV528txkBfg4zTcr
    mH38UczXdN+0m8pqfwIDAQAB
    -----END PUBLIC KEY-----""")
    crypto = rsa.encrypt(message.encode('utf-8'), pubkey)
    return base64.encodestring(crypto)
# print type(crypto)
# print('cry_base64:',base64.encodestring(crypto))


if __name__ == '__main__':
    scm = encrypt('13735865796')
    print (scm)

# import rsa

# # 生成密钥
# (pubkey, privkey) = rsa.newkeys(1024)
# 保存密钥
# with open('rsa_public_key_2.pem', 'w+') as f:
#     f.write(pubkey.save_pkcs1().decode())
# with open('private.pem', 'w+') as f:
#     f.write(privkey.save_pkcs1().decode())
# 导入密钥
# with open('rsa_public_key_2.pem', 'r') as f:
#     pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
# # with open('private.pem', 'r') as f:
# #     privkey = RSA.PrivateKey.load_pkcs1(f.read().encode())
# # 明文
# message = 'hello'
# # 公钥加密
# crypto = rsa.encrypt(message.encode(), pubkey)
# print crypto
# # 私钥解密
# message = RSA.decrypt(crypto, privkey).decode()
# print(message)
# # 私钥签名
# signature = RSA.sign(message.encode(), privkey, 'SHA-1')
# # 公钥验证
# RSA.verify(message.encode(), signature, pubkey)

