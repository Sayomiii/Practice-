'''
run python asynchronous.py
This file basically demonstrates the use of asynchronous programming in Python using the asyncio library. The code defines an asynchronous function called greet() that prints "Starting...", waits for 3 seconds using await asyncio.sleep(3), and then prints "Finished!". The asyncio.run(greet()) line is used to run the greet() function.

'''
import asyncio
async def greet():
    print("Starting...")
    await asyncio.sleep(3)
    print("Finished!")

asyncio.run(greet())




#You don't need multiple statements inside one function to benefit from async. You need asynchronous work that can yield control while waiting, allowing other tasks to make progress.

#sayo is a gile that lives in a busy city and wants to learn how to use asynchronous programming to improve the performance of her applications. She is particularly interested in how it can help her handle multiple tasks concurrently, such as making API calls, reading files, or processing data without blocking the main thread.

