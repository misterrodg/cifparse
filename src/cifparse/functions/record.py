def _check_int_value(check_string: str) -> int:
    return int(check_string) if check_string.isnumeric() else 0


def _get_scaled_magnitude(value: int, scalar: int) -> float:
    return value * (10**scalar)


def clean_value(value: any) -> any:
    if isinstance(value, str) and value == "":
        return None
    return value


def convert_altitude(altitude_string: str) -> int:
    if altitude_string == "" or not altitude_string.isnumeric():
        return None
    return int(altitude_string)


def convert_altitude_fl(altitude_fl_string: str) -> tuple[int, int]:
    if altitude_fl_string[:2] == "FL":
        if altitude_fl_string[2:].isnumeric():
            return (1, int(altitude_fl_string[2:]))
    else:
        if altitude_fl_string.isnumeric():
            return (0, int(altitude_fl_string))
    return (None, None)


def convert_angle(angle_string: str) -> float:
    if angle_string == "" or not angle_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(angle_string), -2)


def convert_arc_bearing(arc_bearing_string: str) -> float:
    if arc_bearing_string == "" or not arc_bearing_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(arc_bearing_string), -1)


def convert_bearing(bearing_string: str) -> tuple[int, float]:
    if bearing_string == "":
        return (None, None)
    if bearing_string[-1] == "T":
        if bearing_string[:-1].isnumeric():
            return (1, int(bearing_string[:-1]))
    else:
        if bearing_string.isnumeric():
            return (0, int(bearing_string) / 10)
    return (None, None)


def convert_course(course_string: str) -> float:
    if course_string == "" or not course_string.isnumeric():
        return None
    return int(course_string) / 10


def convert_distance(distance_string: str, scalar: int = 1) -> float:
    if distance_string == "" or not distance_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(distance_string), scalar)


def convert_distance_time(
    distance_time_string: str, scalar: int = 1
) -> tuple[float, int]:
    if distance_time_string[:1] == "T":
        if distance_time_string[1:].isnumeric():
            return (1, int(distance_time_string[1:]))
    else:
        if distance_time_string.isnumeric():
            return (0, _get_scaled_magnitude(int(distance_time_string), scalar))
    return (None, None)


def convert_el_angle(angle_string: str) -> int:
    if angle_string == "" or not angle_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(angle_string), -1)


def convert_elevation(elevation_string: str) -> int:
    if elevation_string == "" or not elevation_string.isnumeric():
        return None
    return int(elevation_string)


def convert_elevation_wgs84(wgs84_elevation_string: str) -> int:
    if wgs84_elevation_string == "":
        return None
    is_negative = False
    value = None
    if wgs84_elevation_string[:1] == "-":
        is_negative = True
        if wgs84_elevation_string[1:].isnumeric():
            value = int(wgs84_elevation_string[1:])
    else:
        if wgs84_elevation_string.isnumeric():
            value = int(wgs84_elevation_string)
    return value if not is_negative else -value


def convert_ellipsoidal_height(ellipsoidal_height_string: str) -> float:
    if ellipsoidal_height_string == "" or not ellipsoidal_height_string[1:].isnumeric():
        return None
    result = _get_scaled_magnitude(int(ellipsoidal_height_string[1:]), -1)
    if ellipsoidal_height_string[:1] == "-":
        result = -result
    return result


def convert_frequency(frequency_string: str) -> float:
    if frequency_string == "" or not frequency_string.isnumeric():
        return None
    return int(frequency_string) / 100


def convert_gradient(gradient_string: str) -> float:
    if gradient_string == "" or not gradient_string[1:].isnumeric():
        return None
    result = _get_scaled_magnitude(int(gradient_string[1:]), -2)
    if gradient_string[:1] == "-":
        result = -result
    return result


def convert_int(int_string: str) -> int:
    if int_string == "" or not int_string.isnumeric():
        return None
    return int(int_string)


def convert_length(length_string: str, scalar: int = 1) -> int:
    if length_string == "" or not length_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(length_string), scalar)


def convert_lat_dms(lat_string: str) -> float:
    if lat_string == "":
        return None
    north_south = lat_string[0:1]
    lat_d = _check_int_value(lat_string[1:3])
    lat_m = _check_int_value(lat_string[3:5])
    lat_s = _check_int_value(lat_string[5:]) / 100
    result = lat_d + (lat_m / 60) + (lat_s / (60 * 60))
    if north_south == "S":
        result = -result
    return result


def convert_lon_dms(lon_string: str) -> float:
    if lon_string == "":
        return None
    east_west = lon_string[0:1]
    lon_d = _check_int_value(lon_string[1:4])
    lon_m = _check_int_value(lon_string[4:6])
    lon_s = _check_int_value(lon_string[6:]) / 100
    result = lon_d + (lon_m / 60) + (lon_s / (60 * 60))
    if east_west == "W":
        result = -result
    return result


def convert_mag_hdg(mag_hdg_string: str) -> float:
    if mag_hdg_string == "" or not mag_hdg_string.isnumeric():
        return None
    return int(mag_hdg_string)


def convert_mag_var(mag_var_string: str) -> float:
    if mag_var_string == "" or not mag_var_string[1:].isnumeric():
        return None
    if mag_var_string[:1] in ["G", "T"]:
        return 0
    mag_var_value = int(mag_var_string[1:]) / 10
    if mag_var_string[:1] == "W":
        mag_var_value = -mag_var_value
    return mag_var_value


def convert_radius(radius_string: str, scalar: int = -1) -> float:
    if radius_string == "" or not radius_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(radius_string), scalar)


def convert_rho(rho_string: str) -> float:
    if rho_string == "" or not rho_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(rho_string), -1)


def convert_rnp(rnp_string: str) -> float:
    if rnp_string == "" or not rnp_string.isnumeric():
        return None
    if rnp_string[0:1] == "0":
        value = int(rnp_string[1:2])
        exponent = -int(rnp_string[2:3])
        result = round(value * (10**exponent), 1)
        return result
    return int(rnp_string) / 10


def convert_record_number(record_number_string: str) -> int:
    if record_number_string == "" or not record_number_string.isnumeric():
        return None
    return int(record_number_string)


def convert_seq_no(seq_no_string: str) -> int:
    if seq_no_string == "" or not seq_no_string.isnumeric():
        return None
    return int(seq_no_string)


def convert_speed(speed_string: str) -> int:
    if speed_string == "" or not speed_string.isnumeric():
        return None
    return int(speed_string)


def convert_theta(theta_string: str) -> float:
    if theta_string == "" or not theta_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(theta_string), -1)


def convert_time(time_string: str) -> float:
    if time_string == "" or not time_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(time_string), -1)


def convert_true_bearing(true_bearing_string: str) -> float:
    if true_bearing_string == "" or not true_bearing_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(true_bearing_string), -2)


def convert_width(width_string: str, scalar: int = 1) -> int:
    if width_string == "" or not width_string.isnumeric():
        return None
    return _get_scaled_magnitude(int(width_string), scalar)


def convert_yn(text_val: str) -> bool:
    result = False
    if text_val.upper() == "Y":
        result = True
    return result


def extract_field(line: str, field_indices: tuple) -> str:
    start, end = field_indices
    return line[start:end].strip()


def translate_cont_rec_no(cont_rec_no_val: str) -> int:
    if cont_rec_no_val.isnumeric():
        return int(cont_rec_no_val)
    result = cont_rec_no_val.upper()
    if "A" <= result <= "Z":
        return ord(result) - ord("A")
    return 0
