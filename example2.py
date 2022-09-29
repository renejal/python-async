import asyncio

async def fecht_data():
    print("init fetch")
    asyncio.sleep(0)
    print("end fetch")
    
async def print_number():
    for i in range(10):
        print(i)

async def main():
    task1 = asyncio.create_task(fecht_data())
    task2 = asyncio.create_task(print_number)
    

asyncio.run(main())