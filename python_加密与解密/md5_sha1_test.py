import hashlib
test_string = '123456'
md5 = hashlib.md5()
md5.update(test_string.encode('utf-8'))
md5_encode = md5.hexdigest()
print(md5_encode)


sha1 = hashlib.sha1()
sha1.update(test_string.encode('utf-8'))
sha1_encode =sha1.hexdigest()
print(sha1_encode)