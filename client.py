import websockets
import asyncio

import hashlib
import hmac

mail = "some-email.com"
key = "some_key"

byte_key = bytes(key, 'UTF-8')
message = bytes(mail, 'UTF-8')
h =  bytes(mail + ":", 'UTF-8') + hmac.new(byte_key, message, hashlib.sha256).digest()


async def client():
    url = 'some_ws'
    async with websockets.connect(url) as ws:
        try:
            await ws.send(h)
            while True:
                print(await ws.recv())
                ws.close()
        except websockets.ConnectionClosed as e:
            print(f'Terminated', e)


asyncio.get_event_loop().run_until_complete(client())
