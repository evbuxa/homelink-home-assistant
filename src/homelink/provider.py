from auth import AbstractAuth
from model.button import Button
from model.device import Device


class Provider:
    def __init__(self, host_url):
        self.host_url = host_url

    async def discover(self, auth_session: AbstractAuth):
        device_data = await auth_session.request(
            "POST",
            self.host_url,
            body={{"command": "DISCOVER"}},
        ).json()

        devices = []

        for raw_device in device_data["data"]["devices"]:
            d = Device(raw_device["id"], raw_device["name"])
            for raw_button in raw_device["buttons"]:
                d.buttons.append(Button(raw_button["id"], raw_button["name"], d))

        return devices

    async def enable(self, auth_session: AbstractAuth):
        return await auth_session.request(
            "POST",
            self.host_url,
            body={{"command": "DISCOVER"}},
        ).json()
