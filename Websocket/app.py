import asyncio
import websockets

connected = set()


async def echo(websocket, path):
    connected.add(websocket)
    try:
        # Implement logic here.
        async for message in websocket:
            for conn in connected:
                if conn != websocket:
                    await conn.send(f"Got a new messgae {message}")
    finally:
        # Unregister.
        connected.remove(websocket)


start_server = websockets.serve(echo, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
