from __future__ import annotations

import asyncio

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType



DOMAIN = "ha_fontawesome"


@asyncio.coroutine
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.states.async_set('ha_fontawesome.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True
