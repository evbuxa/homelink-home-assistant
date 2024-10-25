async def fetch_data(host_url, authorized_session):
    """Fetch data from"""
    resp = await authorized_session.request("GET", host_url)
    resp_data = await resp.json()
    return resp_data["data"]
