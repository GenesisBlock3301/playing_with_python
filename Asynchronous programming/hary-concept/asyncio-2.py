import asyncio


async def show_message(number, wait):
    # print the message
    print(f"Task {number} is running")
    # Wait assign second
    await asyncio.sleep(wait)
    print(f"Task {number} is completed")


# async def stop_after(when):
#     await asyncio.sleep(when)
#     loop.stop()

async def main():
    task1 = asyncio.ensure_future(show_message(1,2))
    print("Schedule-1")
    task2 = asyncio.ensure_future(show_message(2,1))
    print("Schedule-2")
    # Run the task asynchronously
    await asyncio.wait([task1,task2])

if __name__ == '__main__':
    # Declare event loop
    loop = asyncio.get_event_loop()
    # Run the code of main method until completing all task.
    loop.run_until_complete(main())
    loop.close()



# output
    # Schedule - 1
    # Schedule - 2
    # Task 1 is running
    # Task 2 is running
    # Task 2 is completed
    # Task 1 is completed
