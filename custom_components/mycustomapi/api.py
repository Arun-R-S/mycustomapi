import aiohttp
from homeassistant.components.http import HomeAssistantView

class MyCustomAPI(HomeAssistantView):
    url = "/mycustomapi/tasmota"
    name = "mycustomapi:tasmota"
    requires_auth = False  # Set to True if you want authentication

    async def get(self, request):
        ip = request.query.get("ip")
        pulsetime = request.query.get("pulsetime")
        power = request.query.get("power")
        thisUser = request.query.get("user")
        thisPassword = request.query.get("password")

        if not ip or (not pulsetime and not power):
            return self.json({
                "success": False,
                "error": "Missing 'ip' and either 'pulsetime' or 'power' query parameter"
            }, status_code=400)

        try:
            if pulsetime:
                cmd = f"PulseTime{pulsetime}"
            elif power:
                cmd = f"Power{power}"
            # Build base URL
            base_url = f"http://{ip}/cm?cmnd={cmd}"

            # Append auth params if provided
            if thisUser and thisPassword:
                url = base_url + f"&user={thisUser}&password={thisPassword}"

            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=5) as resp:
                    data = await resp.json()

            return self.json({
                "success": True,
                "ip": ip,
                "cmd": cmd,
                "data": data
            })

        except Exception as e:
            return self.json({
                "success": False,
                "info":"Check the script!!",
                "error": str(e)
            }, status_code=500)
