import aiohttp
import asyncio


async def main():
    url = "http://localhost:8000/start_interview"

    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            if response.status == 200:
                result = response.json
                print("Inteview finished")
                print("Interview result:", result)
            else:
                print("Inteview had an issue")
                print("Error:", response.status)
                print("Error:", response.text)

if __name__ == "__main__":
    asyncio.run(main())
