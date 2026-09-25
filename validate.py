def validate_state(record: dict) -> bool:
    for key, value in record.items():
        if key != "altitude" and value is None:
            return False
    
    if not altitude_is_reasonable(record["altitude"]):
        return False
    
    if not coordinates_in_bounds(record["longitude"], record["latitude"]):
        return False
    
    return True

def altitude_is_reasonable(altitude) -> bool:
    if altitude is None:
        return True  # grounded aircraft, no altitude to check
    if -500 <= altitude <= 18000:
        return True
    return False

def coordinates_in_bounds(longitude, latitude) -> bool:
    if longitude is None or latitude is None:
        return False
    if 103.60 <= longitude <= 104.20 and 1.15 <= latitude <= 1.55:
        return True
    return False