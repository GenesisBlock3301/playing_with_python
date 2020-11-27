import asyncio


async def findDivisible(inrange, div_by):
    print(f"Finding num in range {inrange} divisible by {div_by}")
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 500000 == 0:
            await asyncio.sleep(0.0001)
    print(f"Done w/ nums in range {inrange} divisible by {div_by}")
    return located


async def main():
    divs1 = loop.create_task(findDivisible(508000, 34113))
    divs2 = loop.create_task(findDivisible(100052, 3210))
    divs3 = loop.create_task(findDivisible(500, 3))
    await asyncio.wait(divs1,divs2,divs3)

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        # loop.set_debug(1)
        loop.run_until_complete(main())
        loop.close()
    except Exception as e:
        pass
    finally:
        loop.close()
