import asyncio


async def add(start,end,wait):
    sum = 0

    for n in range(start,end):
        sum+=n

    await asyncio.sleep(wait)
    print(f"Sum from {start} to {end} is {sum}")

async def main():
    task1 = loop.create_task(add(5,500000,3))
    task2 = loop.create_task(add(2,300000,2))
    task3 = loop.create_task(add(10,1000,1))
    # task4 = loop.create_task(add(1,101,1))
    #Run the task asynchonously
    await asyncio.wait([task1,task2,task3])

if __name__ == "__main__":
    #Declare event loop
    loop = asyncio.get_event_loop()
    # Run the code untile complete all task
    loop.run_until_complete(main())
    # close the loop
    loop.close()

# output:
# Sum from 10 to 1000 is 499455
# Sum from 2 to 300000 is 44999849999
# Sum from 5 to 500000 is 124999749990
#
# That means less time excute first
# other will execute next
