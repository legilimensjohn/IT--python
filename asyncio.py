import asyncio

async def hello():
    print("Hello, ")
    await asyncio.sleep(1)
    print("World!")

# Create an event loop and run the coroutine
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())