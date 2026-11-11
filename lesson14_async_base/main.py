import asyncio
import time


async def fetch_data(seconds):
    print(f"Начинаем запрос {seconds}")
    await asyncio.sleep(seconds)
    # await asyncio.to_thread(time.sleep, seconds) # bad
    print(f"Запрос прошел успешно {seconds}")

    return 42


async def main():
    print(fetch_data)
    start = time.perf_counter()

    await asyncio.gather(fetch_data(2), fetch_data(4))

    # task1 = asyncio.create_task(fetch_data(2))
    # task2 = asyncio.create_task(fetch_data(4))
    # task3 = asyncio.create_task(fetch_data(3))

    # await asyncio.gather(task1, task2, task3)

    # await task1
    # await task2
    # await task3

    print(time.perf_counter() - start)


asyncio.run(main())


# async def alternative():
#     tasks = [
#         asyncio.create_task(fetch_data(5)),
#         asyncio.create_task(fetch_data(2)),
#     ]

#     # wait:
#     done, pending = await asyncio.wait(tasks)
#     print(f"Завершена {len(done)}, осталось: {len(pending)}")

#     # as_completed:
#     for finished_task in asyncio.as_completed(tasks):
#         result = await finished_task
#         print(f"Готов результат {result}")

#     # TaskGroup:
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(fetch_data(5))
#         tg.create_task(fetch_data(2))


# asyncio.run(alternative())
