import hashlib

device_id = input("请输入设备ID：")
hash_md5 = hashlib.md5()
hash_md5.update(device_id.encode('utf-8'))
encrypted_str = hash_md5.hexdigest()
print(f"序列号为：{encrypted_str}")
