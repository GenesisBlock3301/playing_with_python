import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print("Hello world")

asyncio.run(main())
