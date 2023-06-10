from __future__ import annotations

from homeassistant.components.input_boolean import DOMAIN as INPUT_BOOLEAN_DOMAIN
from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import SERVICE_TURN_ON, SERVICE_TURN_OFF, ATTR_ENTITY_ID, STATE_ON
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry

from ..coordinator import DeviceState, SatDataUpdateCoordinator


class SatSwitchCoordinator(SatDataUpdateCoordinator):
    """Class to manage the Switch."""

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, entity_id: str) -> None:
        """Initialize."""
        super().__init__(hass, config_entry)

        self._entity = entity_registry.async_get(hass).async_get(entity_id)

    @property
    def setpoint(self) -> float:
        return self.minimum_setpoint

    @property
    def maximum_setpoint(self) -> float:
        return self.minimum_setpoint

    @property
    def device_active(self) -> bool:
        if (state := self.hass.states.get(self._entity.id)) is None:
            return False

        return state.state == STATE_ON

    async def async_set_heater_state(self, state: DeviceState) -> None:
        if not self._simulation:
            service = SERVICE_TURN_ON if state == DeviceState.ON else SERVICE_TURN_OFF

            if self._entity.domain == SWITCH_DOMAIN:
                await self.hass.services.async_call(SWITCH_DOMAIN, service, {ATTR_ENTITY_ID: self._entity.entity_id}, blocking=True)

            if self._entity.domain == INPUT_BOOLEAN_DOMAIN:
                await self.hass.services.async_call(INPUT_BOOLEAN_DOMAIN, service, {ATTR_ENTITY_ID: self._entity.entity_id}, blocking=True)

        await super().async_set_heater_state(state)
