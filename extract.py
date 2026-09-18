import requests
import json

with open("/Users/sidharthrao/Downloads/credentials.json") as f:
    creds = json.load(f)

CLIENT_ID = creds["clientId"]
CLIENT_SECRET = creds["clientSecret"]

TOKEN_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
STATES_URL = "https://opensky-network.org/api/states/all"

# Changi airspace bounding box
BBOX = {
    "lamin": 1.15,
    "lamax": 1.55,
    "lomin": 103.60,
    "lomax": 104.20,
}


def get_access_token():
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


def get_flight_states(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(STATES_URL, params=BBOX, headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    token = get_access_token()
    data = get_flight_states(token)
    print(f"Fetched {len(data.get('states', []))} aircraft states")

    # Save the full response for later use in Phase 2
    with open("sample_changi_states.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Saved full response to sample_changi_states.json")