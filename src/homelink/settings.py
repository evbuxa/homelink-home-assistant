from decouple import config

# TODO: Defaults should be production
HOST_URL = config("HOMELINK_HOST_URL", default="https://d1f2mm2dg61j0w.cloudfront.net")
DISCOVER_URL = config(
    "HOMELINK_DISCOVER_URL",
    default=f"{HOST_URL}/services/v2/home-assistant/fulfillment",
)
ENABLE_URL = config(
    "HOMELINK_ENABLE_URL", default=f"{HOST_URL}/services/v2/home-assistant/fulfillment"
)
STATE_URL = config(
    "HOMELINK_STATE_URL", default=f"{HOST_URL}/services/v2/home-assistant/state"
)
