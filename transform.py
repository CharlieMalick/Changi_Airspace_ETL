def classify_flight_phase(on_ground: bool, baro_altitude, vertical_rate) -> str:
    if on_ground:
        return "Grounded"
    else:
        if vertical_rate is None:
            return "Insufficient Data"
        else:
            if vertical_rate < -1:
                return "Approach"
            elif vertical_rate > 1:
                return "Climb"
            elif -1 <= vertical_rate <= 1:
                return "Cruise"

def clean_callsign(raw_callsign) -> str:
    if raw_callsign is None:
        return "Insufficient Data"
    
    cleaned = raw_callsign.strip()
    
    if cleaned == "":
        return "Insufficient Data"
    
    return cleaned

def transform_state(state: list) -> dict:
    # state is one row from OpenSky's "states" array, e.g.:
    # ["76cd06","SIA967  ","Singapore",1789742730,1789742730,103.9269,1.2294,754.38,false,98.89,22.96,-5.2,...]
    #    [0]      [1]                                            [5]      [6]     [7]    [8]           [11]
    #  icao24   callsign                                          lon      lat  altitude on_ground   vert_rate
    icao24 = state[0]
    callsign = clean_callsign(state[1])
    longitude = state[5]
    latitude = state[6]
    altitude = state[7]
    phase = classify_flight_phase(state[8], state[7], state[11])
    final_dict = {"icao24":icao24, "callsign":callsign, "longitude":longitude, 
                  "latitude":latitude, "altitude":altitude, "phase":phase}
    return final_dict