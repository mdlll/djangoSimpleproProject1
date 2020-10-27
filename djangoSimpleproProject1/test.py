import json
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoSimpleproProject1.settings'
django.setup()

from django.contrib.auth.models import User
from ap1.hooks import generate_token, certify_token

#
# user = User.objects.filter(is_superuser=True)
# print(user)
#
# ret = generate_token('3a3', 36)
# print(ret)
#
# print(certify_token('3a3', 'MTYwMDg0Mzc3Mi42OTk4NTE4Ojg0ZGNmZGU1ODg1MjRkOGQyMDhjYjkzM2IxMWY2OWRlNmI5ZTlhYjI='))


# AES-demo
#
# import base64
# from Crypto.Cipher import AES
# from urllib import parse
#
# '''
# 采用AES对称加密算法
# '''
#
#
# # str不是16的倍数那就补足为16的倍数
# def add_to_16(value):
#     while len(value) % 16 != 0:
#         value += '\0'
#     return str.encode(value)  # 返回bytes
#
#
# # 加密方法
# def encrypt_oracle():
#     # 秘钥
#     key = '123456'
#     # 待加密文本
#     text = 'abc123def456'
#     # 偏移值
#     Iv = b'1234567890111111'
#     # 初始化加密器
#     aes = AES.new(add_to_16(key), AES.MODE_CBC, Iv)
#     # 先进行aes加密
#     encrypt_aes = aes.encrypt(add_to_16(text))
#     # 用base64转成字符串形式
#     encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').replace('\n', '')  # 执行加密并转码返回bytes
#     # 然后进行url加密
#     encrypt_aes_url = parse.quote(encrypted_text)
#     # pVnMY/aOznt6xwFbblmVHw==
#     print(encrypted_text)
#     print(encrypt_aes_url)
#
#
# # 解密方法
# def decrypt_oralce():
#     # 密文
#     pwd = "RcHB24wYLt%2BytE2rNtMZo6rEg4pyX7QI%2B2WBDn77zJreKE7lGDm7sfL2mQKqzDyG4dAYjlPTdMQsqoB8bEAYgx53KDzp1sFvaNI1DsWilXKRiHEdHq3das8mIXP6u1Gj"
#     text = parse.unquote(pwd)
#     print(text)
#     # 秘钥
#     key = '1q2w3e4r5t6y7u8i'
#     # 偏移值
#     Iv = b'1234567812345678'
#     # 初始化加密器
#     aes = AES.new(add_to_16(key), AES.MODE_CBC, iv=Iv)
#     # 优先逆向解密base64成bytes
#     base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
#     # 执行解密密并转码返回str
#     decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('', '')
#     print(decrypted_text)
#     ss = json.loads(decrypted_text)  # 转为dict
#     print(ss)


# if __name__ == '__main__':
    # encrypt_oracle()
    # decrypt_oralce()


