# Simple Asynchronous Programming Example

import asyncio

async def task(name):
    print(name, "started")

    # Wait without blocking other tasks
    await asyncio.sleep(2)

    print(name, "finished")

async def main():
    # Run both tasks concurrently
    await asyncio.gather(
        task("Task 1"),
        task("Task 2")
    )

    print("All tasks completed.")

# Start the program
asyncio.run(main())