import asyncio

async def get_score(player,seconds):
    await asyncio.sleep(1)
    return f"{player}: {seconds} seconds"

async def main():
    results = await asyncio.gather(
        get_score("Amina", 10),
        get_score("Kai", 15),
        get_score("Noah", 20)
    )
    
    # results is a list of the return values from the get_score function for each player
    print("Scores retrieved:")
    print(results)
    print("\n")  # Just to add a newline for better readability
    print("All scores have been retrieved!")
    # You can also loop through the results if you want to print them one by one
    for result in results:
        print(result)

asyncio.run(main())
