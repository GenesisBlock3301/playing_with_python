import asyncio
import time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started time at: {time.strftime('%X')}")
    task1 = asyncio.create_task(say_after(1,'hello'))
    task2 = asyncio.create_task(say_after(2,'Sifat'))
    await task1
    await task2
    print(f"Finished time: {time.strftime('%X')}")

asyncio.run(main())