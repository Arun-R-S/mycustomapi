import aiohttp
#from homeassistant.components.http import HomeAssistantView
from aiohttp import web

class MyCustomAPI:
#class MyCustomAPI(HomeAssistantView):
    #url = "/customapi/tasmota"
    #name = "customapi:tasmota"
    #requires_auth = False  # Set to True if you want authentication

    async def get(self, request):
        ip = request.query.get("ip")
        pulsetime = request.query.get("pulsetime")
        power = request.query.get("power")
        admin = request.query.get("admin")
        username = request.query.get("username")

        if not ip or (not pulsetime and not power):
            return web.json_response({
                "success": False,
                "error": "Missing 'ip' and either 'pulsetime' or 'power' query parameter"
            }, status_code=400)

        try:
            if pulsetime:
                cmd = f"PulseTime{pulsetime}"
            elif power:
                cmd = f"Power{power}"

            url = f"http://{ip}/cm?cmnd={cmd}"

            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=5) as resp:
                    data = await resp.json()

            return web.json_response({
                "success": True,
                "cmd": cmd,
                "data": data
            })

        except Exception as e:
            return web.json_response({
                "success": False,
                "url":url,
                "info":"Check the script!!",
                "error": str(e)
            }, status=500)
