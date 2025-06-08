from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "mycustomapi"

class MyCustomAPIConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for My Custom API."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            # Save config and create the integration entry
            return self.async_create_entry(title="My Custom API", data=user_input)

        # Show form for input (optional, can be empty if no config needed)
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({})
        )
