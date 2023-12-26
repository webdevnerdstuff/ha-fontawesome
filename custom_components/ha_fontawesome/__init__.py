from __future__ import annotations

import asyncio

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "ha_fontawesome"


@asyncio.coroutine
def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:

    return True
