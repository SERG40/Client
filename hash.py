import hashlib
import hmac


mail = "some-email.com"
key = "some_key"


byte_key = bytes(key, 'UTF-8')
message = bytes(mail, 'UTF-8')

h =  bytes(mail + ":", 'UTF-8') + hmac.new(byte_key, message, hashlib.sha256).digest()


print(h)
