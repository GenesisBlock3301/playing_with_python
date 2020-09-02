import asyncio,time

start = time.time()

async def add(x,y):
    print(f"Adding {x}+{y}")
    await asyncio.sleep(5.0)
    print(f"Result of addition: {x+y}")

async def sub(x,y):
    print(f"Substructing {x}-{y}")
    await asyncio.sleep(2.0)
    print(f"Result of Substruct: {x - y}")

loop = asyncio.get_event_loop()
tasks = []
tasks.append(loop.create_task(add(1,3)))
tasks.append(loop.create_task(sub(5,4)))
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f"Totall time to spend : {end-start}")
loop.close()