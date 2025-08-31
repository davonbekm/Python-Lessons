# 1) Oddiy sinxron kutish: 1 soniyadan oshsa TimeoutError ko'taramiz.
#    Simple synchronous wait: raise TimeoutError after 1 second.

import time

start = time.time()
while True:
    if time.time() - start > 1.0:
        raise TimeoutError("1 soniya kutdik, natija yo‘q | Waited 1s, no result")


# 2) asyncio.wait_for bilan korutina vaqtidan oshsa asyncio.TimeoutError ko'tariladi
#       (uni odatiy TimeoutError sifatida ham tuta olasiz).
#    asyncio.wait_for raises asyncio.TimeoutError on timeout
#       (you can catch it as regular TimeoutError).

import asyncio

async def work():
    await asyncio.sleep(2)  # uzoqroq ish

async def main():
    await asyncio.wait_for(work(), timeout=0.5)

asyncio.run(main())


# 3) (Unix) signal.alarm bilan muddat o'rnatib, handler ichida TimeoutError ko'taramiz.
#    (Unix) Use signal.alarm and raise TimeoutError in the handler.

import signal
import time

def handler(signum, frame):
    raise TimeoutError("Vaqt tugadi | Time limit exceeded")

signal.signal(signal.SIGALRM, handler)
signal.alarm(1)  # 1 soniya
time.sleep(2)    # ko'proq kutamiz -> handler ishga tushadi va TimeoutError