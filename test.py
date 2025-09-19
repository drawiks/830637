
from translator import translate
import asyncio

async def test():
    while True:
        print(await translate(input("word: ")))
        
if __name__ == "__main__":
    asyncio.run(test())