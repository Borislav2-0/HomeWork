import asyncio


async def start_strongman(name, power):
    print(f'Strongman {name} started the competition')
    for n in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'The strongman {name} picked up the {n} ball.' )
    print(f'Strongman {name} has finished the competition.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Zimogor', 3))
    task2 = asyncio.create_task(start_strongman('The Grey Dog', 4))
    task3 = asyncio.create_task(start_strongman('Aptakhar', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())