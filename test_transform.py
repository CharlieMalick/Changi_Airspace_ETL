import json
from transform import classify_flight_phase

with open("sample_changi_states.json") as f:
    data = json.load(f)

for state in data["states"]:
    on_ground = state[8]
    baro_altitude = state[7]
    vertical_rate = state[11]
    print(classify_flight_phase(on_ground, baro_altitude, vertical_rate))