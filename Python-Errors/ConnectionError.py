# 1) socket.connect() — yopiq portga ulanishga urinish
# 127.0.0.1 dagi yopiq (1) portga ulanish -> ConnectionRefusedError (ConnectionError ost turi).
# Connect to a closed port on 127.0.0.1 -> ConnectionRefusedError (a subclass of ConnectionError).
import socket

s = socket.socket()
s.settimeout(0.5)
s.connect(("127.0.0.1", 1))  # odatda tezda rad etiladi


# 2) asyncio.open_connection() — yopiq port
# Async ulanish ham yopiq portda xuddi shu xatoni ko‘taradi.
# Async connect to a closed port raises the same error.
import asyncio

async def main():
    # Bu satr ConnectionRefusedError ko‘taradi (ConnectionError ost turi)
    await asyncio.open_connection("127.0.0.1", 1)

asyncio.run(main())


# 3) requests.get() — xizmat ishlamayapti
# requests kutubxonasida xato turi requests.exceptions.ConnectionError bo‘ladi.
# In requests, you'll get requests.exceptions.ConnectionError.
import requests

requests.get("http://127.0.0.1:1", timeout=1)  # NewConnectionError/ConnectionError ko‘taradi