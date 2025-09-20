
from translator import encode, decode
import asyncio

async def test():
    while True:
        encoded = await encode(input(": "))
        decoded = await decode(encoded)
        print(encoded)
        print(decoded)
        
if __name__ == "__main__":
    asyncio.run(test())