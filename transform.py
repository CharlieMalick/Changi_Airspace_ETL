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