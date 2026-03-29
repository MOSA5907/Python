import asyncio

async def download_file(name, seconds):
    print(f"Starting {name}")
    await asyncio.sleep(seconds)
    print(f"Finished {name}")

async def main():
    task1 = asyncio.create_task(download_file("report.pdf",2))
    task2 = asyncio.create_task(download_file("photo.png",1))

    await task1
    await task2

asyncio.run(main())
