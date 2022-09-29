"""entendiendo que es asyc sin utilizar asyc que es un generados en python"""
from typing import List
import asyncio

async def estudiar():
    print("estudiar")
    await asyncio.sleep(0)
    print("relizar resumen")
    await asyncio.sleep(0)
    print("Memorizar")
    

async def facebook():
    print("ver videos")
    await asyncio.sleep(0)
    print("descanzar")
    await asyncio.sleep(0)
    print("chatear")

async def main():
    await asyncio.gather(estudiar(),facebook())

asyncio.run(main())