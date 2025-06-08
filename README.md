
## Installation

### Custom-Components

mycustomapi is available in [Custom-Component Repository](https://github.com/Arun-R-S/home-assistant-custom-components).

Use this link to directly go to the release in Github

[Releases](https://github.com/Arun-R-S/home-assistant-custom-components/releases)


### Manual

1. Download `project` from the [latest release](https://github.com/Arun-R-S/home-assistant-custom-components/releases).
2. Put the files and folders into your `config/custom_components` folder.
3. Now Restart the Home Assistant. The way to do that:
	- **Update YAML:** Add following code to `configuration.yaml` section.
        ```yaml
        mycustomapi:
        ```
    - **Then Restart:** _Settings_ → _Developer Tools_ → _YAML_ → _Restart_. Now the configuration will check for errors and if everything is ok then a Popup will open. Select `Restart Home Assistant` option from there.
      **Note:** If you see any config error please check the configuration.yaml properly and then try restart again.
    

## Usage

With this custom component you can be able call an api from the front end UI to avoid CORS.

1. In Cards if you have a functionality to call an api(eg: `http://192.168.0.54/cm?cmnd=power1`) then it will cause CORS issue since the domain is different from the `homeassistant.local:8123` host.
2. Instead of calling the api directly just call the home assistant script first `http://homeassistant.local:8123/customapi/tasmota?ip=192.168.0.54&power=1` , then in the home assistant script handle the logic to call the exact api and return the response.
3. This api is created exactly to handle the tasmota pulsetime scenerio. You can change the logic as per your requirement.
4. Happy Coding!!!!!.




## Credits

The design is inspired by [Arun’s work][Arun-R-S].

<!-- References -->

[home-assistant]: https://www.home-assistant.io/
[home-assitant-theme-docs]: https://www.home-assistant.io/integrations/frontend/#defining-themes
[hacs]: https://hacs.xyz
[ui-lovelace-minimalist]: https://ui-lovelace-minimalist.github.io/UI/
[button-card]: https://github.com/custom-cards/button-card
[Arun-R-S]: https://arunrs.com
[release-url]: https://github.com/Arun-R-S/home-assistant-custom-components/releases
