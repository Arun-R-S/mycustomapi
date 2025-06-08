from .api import MyCustomAPI

async def async_setup(hass, config):
    hass.http.register_view(MyCustomAPI())
    return True