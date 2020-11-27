import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    # for _ in range(3):
    #     await asyncio.gather(count())
    await asyncio.gather(count(),count(),count())


if __name__ == "__main__":
    import time
    start = time.time()
    asyncio.run(main())
    end = time.time()
    file_name = str(__file__).split("/")
    print(f"{file_name[-1]} executed in {end-start:0.2f} seconds.")