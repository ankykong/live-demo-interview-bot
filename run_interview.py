import aiohttp
import asyncio


async def main():
    url = "http://127.0.0.1:8000/start_interview"

    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            if response.status == 200:
                result = response.json
                print("Interview started successfully.")
                print("Interview result:", result)
            else:
                print("Failed to start interview.")
                print("Response status code:", response.status)
                print("Error Text:", await response.text())

if __name__ == "__main__":
    asyncio.run(main())
