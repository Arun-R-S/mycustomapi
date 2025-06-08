from .api import MyCustomAPI

import logging

_LOGGER = logging.getLogger(__name__)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

async def async_setup(hass: HomeAssistant, config: dict):
    # Optional: still needed if you have YAML setup
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    # Called when a user adds your integration via the UI
    _LOGGER.info("Setting up MyCustomAPI")
    hass.http.register_view(MyCustomAPI())
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    # Optional clean-up logic
    return True
