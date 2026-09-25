def validate_state(record: dict) -> bool:
    # record is the output of transform_state() — e.g.:
    # {'icao24': '76cef2', 'callsign': 'SIA636', 'longitude': 104.0733, 
    #  'latitude': 1.4473, 'altitude': 1120.14, 'phase': 'Climb'}
    for value in record.values():
        if value is None:
            return False
    return True