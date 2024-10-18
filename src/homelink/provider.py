from homelink.auth import AbstractAuth
from homelink.model.button import Button
from homelink.model.device import Device
import json
import logging


class Provider:
    def __init__(self, host_url):
        self.host_url = host_url

    async def discover(self, auth_session: AbstractAuth):
        resp = await auth_session.request(
            "POST",
            self.host_url,
            json={"command": "DISCOVER"},
        )
        device_data = await resp.json()
        logging.info(device_data)
        devices = []

        for raw_device in device_data["data"]["devices"]:
            d = Device(raw_device["id"], raw_device["name"])
            for raw_button in raw_device["buttons"]:
                d.buttons.append(Button(raw_button["id"], raw_button["name"], d))
            devices.append(d)

        return devices

    async def enable(self, auth_session: AbstractAuth):
        return auth_session.request(
            "POST",
            self.host_url,
            json={"command": "ENABLE"},
        )
