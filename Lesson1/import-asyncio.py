import asyncio

async def get_score(player):
    await asyncio.sleep(1)
    return f"{player}: 100"

async def main():
    results = await asyncio.gather(
        get_score("Amina"),
        get_score("Kai"),
        get_score("Noah")
    )
    print(results)

asyncio.run(main())
