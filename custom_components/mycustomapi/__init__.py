from .api import MyCustomAPI
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    _LOGGER.info("Setting up MyCustomAPI")
    hass.http.register_view(MyCustomAPI())
    return True