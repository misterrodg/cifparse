def _check_empty_string(string: str) -> bool:
    return True if string.strip() == "" else False


def _string_or_none(string: str) -> str | None:
    return None if _check_empty_string(string) else string


def _check_int_value(check_string: str) -> int:
    return int(check_string) if check_string.isnumeric() else 0


def _get_altitude_fl(string: str) -> tuple[bool, int] | tuple[None, None]:
    if string[:2] == "FL":
        if string[2:].isnumeric():
            return (True, int(string[2:]))
    else:
        if string.isnumeric():
            return (False, int(string))
    return (None, None)


def _get_bool(string: str) -> bool | None:
    if string == "Y":
        return True
    if string == "N":
        return False
    return None


def _get_int(string: str) -> int | None:
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return int(string)


def _get_course(string: str) -> float | None:
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def _get_lat(string: str, high_precision: bool = False) -> float:
    scalar = -4 if high_precision else -2
    north_south = string[0:1]
    lat_d = _check_int_value(string[1:3])
    lat_m = _check_int_value(string[3:5])
    lat_s = _get_scaled_int(_check_int_value(string[5:]), scalar)
    result = lat_d + (lat_m / 60) + (lat_s / (60 * 60))
    if north_south == "S":
        result = -result
    return result


def _get_lon(string: str, high_precision: bool = False) -> float:
    scalar = -4 if high_precision else -2
    east_west = string[0:1]
    lon_d = _check_int_value(string[1:4])
    lon_m = _check_int_value(string[4:6])
    lon_s = _get_scaled_int(_check_int_value(string[6:]), scalar)
    result = lon_d + (lon_m / 60) + (lon_s / (60 * 60))
    if east_west == "W":
        result = -result
    return result


def _get_magnetic_bearing_with_true(
    string: str,
) -> tuple[bool, float] | tuple[None, None]:
    if _check_empty_string(string):
        return (None, None)
    if string[-1] == "T":
        if string[:-1].isnumeric():
            return (True, int(string[:-1]))
    else:
        if string.isnumeric():
            return (False, _get_scaled_int(int(string), -1))
    return (None, None)


def _get_scaled_int(int: int, scalar: int) -> float:
    return round(int * (10**scalar), abs(scalar))


def _get_scaled_magnitude(string: str, scalar: int) -> float | None:
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_int(int(string), scalar)


def _get_signed_value(string: str, scalar: int = -1) -> float | None:
    sign = string[:1]
    value = string
    if sign in ["+", "-"]:
        value = string[1:]
    result = _get_scaled_magnitude(value, scalar)
    if sign == "-" and result:
        return -result
    return result


def field_52(string: str) -> str | None:
    "Record Type (S/T)"
    return _string_or_none(string)


def field_53(string: str) -> str | None:
    "Customer/Area"
    return _string_or_none(string)


def field_54(string: str) -> str | None:
    "Section Code"
    return _string_or_none(string)


def field_55(string: str) -> str | None:
    "Subsection Code"
    return _string_or_none(string)


def field_56(string: str) -> str | None:
    "Airport/Heliport ID"
    return _string_or_none(string.strip())


def field_57(string: str) -> str | None:
    "Route Type"
    return _string_or_none(string)


def field_58(string: str) -> str | None:
    "Route ID"
    return _string_or_none(string.strip())


def field_59(string: str) -> str | None:
    "SID/STAR Route ID"
    return _string_or_none(string.strip())


def field_510(string: str) -> str | None:
    "IAP Route ID"
    return _string_or_none(string.strip())


def field_511(string: str) -> str | None:
    "Transition ID"
    return _string_or_none(string.strip())


def field_512(string: str) -> int | None:
    "Sequence Number"
    return _get_int(string)


def field_513(string: str) -> str | None:
    "Fix Identifier"
    return _string_or_none(string.strip())


def field_514(string: str) -> str | None:
    "ICAO Code/Region"
    return _string_or_none(string.strip())


# 515 Reserved


def field_516(string: str) -> int:
    "Continuation Record Number"
    if string.isnumeric():
        return int(string)
    result = string.upper()
    if "A" <= result <= "Z":
        return ord(result) - ord("A")
    return 0


def field_517(string: str) -> str | None:
    "Waypoint Description Code"
    return _string_or_none(string)


def field_518(string: str) -> str | None:
    "Boundary Code"
    return _string_or_none(string)


def field_519(string: str) -> str | None:
    "Level"
    return _string_or_none(string)


def field_520(string: str) -> str | None:
    "Turn Direction"
    return _string_or_none(string)


def field_521(string: str) -> str | None:
    "Path and Termination"
    return _string_or_none(string)


def field_522(string: str) -> str | None:
    "Turn Direction Valid"
    return _string_or_none(string)


def field_523(string: str) -> str | None:
    "Recommended NAVAID"
    return _string_or_none(string.strip())


def field_524(string: str) -> float | None:
    "Theta"
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def field_525(string: str) -> float | None:
    "Rho"
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def field_526(string: str) -> tuple[bool, float] | tuple[None, None]:
    "Outbound Magnetic Course"
    return _get_magnetic_bearing_with_true(string)


def field_527(string: str) -> tuple[bool, float] | tuple[None, None]:
    "Route Distance From, Holding Distance/Time"
    if string[:1] == "T":
        if string[1:].isnumeric():
            return (True, _get_scaled_int(int(string[1:]), -1))
    else:
        if string.isnumeric():
            return (False, _get_scaled_int(int(string), -1))
    return (None, None)


def field_528(string: str) -> tuple[bool, float] | tuple[None, None]:
    "Inbound Magnetic Course"
    return _get_magnetic_bearing_with_true(string)


def field_529(string: str) -> str | None:
    "Altitude Description"
    return _string_or_none(string)


def field_530(string: str) -> tuple[bool, int] | tuple[None, None]:
    "Altitude / Minimum Altitude"
    if string in ["UNKNN", "NESTB"]:
        return (None, None)
    if string[:2] == "FL":
        if string[2:].isnumeric():
            return (True, int(string[2:]))
    else:
        if string.isnumeric():
            return (False, int(string))
    return (None, None)


def field_531(string: str) -> int | None:
    "File Record Number"
    return _get_int(string)


def field_532(string: str) -> str | None:
    "Cycle Date"
    return _string_or_none(string)


def field_533(string: str) -> str | None:
    "VOR/NDB Identifier"
    return _string_or_none(string.strip())


def field_534(string: str, type: str) -> float | None:
    """
    VOR/NDB Frequency

    REQUIRES TYPE
    """
    if _check_empty_string(string) or not string.isnumeric():
        return None
    if type == "VOR":
        return _get_scaled_magnitude(string, -2)
    if type == "NDB":
        return _get_scaled_magnitude(string, -1)
    return None


def field_535(string: str) -> str | None:
    "NAVAID Class"
    return _string_or_none(string)


def field_536(string: str) -> float | None:
    "Latitude"
    if _check_empty_string(string):
        return None
    return _get_lat(string)


def field_537(string: str) -> float | None:
    "Longitude"
    if _check_empty_string(string):
        return None
    return _get_lon(string)


def field_538(string: str) -> str | None:
    "DME Identifier"
    return _string_or_none(string.strip())


def field_539(string: str) -> float | None:
    "Magnetic Variation"
    if _check_empty_string(string) or not string[1:].isnumeric():
        return None
    if string[:1] == "T":
        return 0
    result = _get_scaled_magnitude(string[1:], -1)
    if string[:1] == "W" and result != None:
        result = -result
    return result


def field_540(string: str) -> int | None:
    "DME Elevation"
    return _get_int(string)


def field_541(string: str) -> str | None:
    "Region Code"
    return _string_or_none(string.strip())


def field_542(string: str) -> str | None:
    "Waypoint Type"
    return _string_or_none(string)


def field_543(string: str) -> str | None:
    "Waypoint Name/Description"
    return _string_or_none(string.strip())


def field_544(string: str) -> str | None:
    "Localizer/MLS/GLS Identifier"
    return _string_or_none(string.strip())


def field_545(string: str) -> float | None:
    "Localizer Frequency"
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -2)


def field_546(string: str) -> str | None:
    "Runway Identifier"
    return _string_or_none(string.strip())


def field_547(string: str) -> tuple[bool, float] | tuple[None, None]:
    "Localizer Bearing"
    return _get_magnetic_bearing_with_true(string)


def field_548(string: str) -> int | None:
    "Localizer Position"
    return _get_int(string)


def field_549(string: str) -> str | None:
    "Localizer/Azimuth Position Reference"
    return _string_or_none(string)


def field_550(string: str) -> int | None:
    "Glide Slope Position / Elevation Position"
    return _get_int(string)


def field_551(string: str) -> float | None:
    "Localizer Width"
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -2)


def field_552(string: str) -> float | None:
    "Glide Slope Angle / Minimum Elevation Angle"
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -2)


def field_553(string: str) -> int | None:
    "Transition Altitude/Level"
    return _get_int(string)


def field_554(string: str) -> int | None:
    "Longest Runway"
    result = _get_scaled_magnitude(string, 2)
    if result != None:
        result = int(result)
    return result


def field_555(string: str) -> int | None:
    "Airport/Heliport Elevation"
    return _get_int(string)


def field_556(string: str) -> str | None:
    "Gate Identifier"
    return _string_or_none(string.strip())


def field_557(string: str) -> int | None:
    "Runway Length"
    return _get_int(string)


def field_558(string: str) -> tuple[bool, float] | tuple[None, None]:
    "Runway Magnetic Bearing"
    return _get_magnetic_bearing_with_true(string)


def field_559(string: str) -> str | None:
    "Runway Description"
    return _string_or_none(string.strip())


def field_560(string: str) -> str | None:
    "Name"
    return _string_or_none(string.strip())


def field_561(string: str) -> str | None:
    "Notes"
    return _string_or_none(string.strip())


def field_562(string: str) -> tuple[bool, float] | tuple[None, None]:
    "Inbound Holding Course"
    return _get_magnetic_bearing_with_true(string)


def field_563(string: str) -> str | None:
    "Turn"
    return _string_or_none(string)


def field_564(string: str) -> float | None:
    "Leg Length"
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def field_565(string: str) -> float | None:
    "Leg Time"
    if _check_empty_string(string) or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def field_566(string: str) -> float | None:
    "Station Declination"
    if _check_empty_string(string) or not string[1:].isnumeric():
        return None
    if string[:1] in ["G", "T"]:
        return 0
    result = _get_scaled_magnitude(string[1:], -1)
    if string[:1] == "W" and result != None:
        result = -result
    return result


def field_567(string: str) -> int | None:
    "Threshold Crossing Height"
    return _get_int(string)


def field_568(string: str) -> int | None:
    "Landing Threshold Elevation"
    return _get_int(string)


def field_569(string: str) -> int | None:
    "Threshold Displacement Distance"
    return _get_int(string)


def field_570(string: str) -> float | None:
    "Vertical Angle"
    return _get_signed_value(string, -2)


def field_571(string: str) -> str | None:
    "Name Field"
    return _string_or_none(string.strip())


def field_572(string: str) -> int | None:
    "Speed Limit"
    return _get_int(string)


def field_573(string: str) -> tuple[bool, int] | tuple[None, None]:
    "Speed Limit Altitude"
    return _get_altitude_fl(string)


def field_574(string: str) -> int | None:
    "Component Elevation"
    return _get_int(string)


def field_575(string: str) -> str | None:
    "From/To - Airport/Fix"
    return _string_or_none(string.strip())


def field_576(string: str) -> str | None:
    "Company Route Identifier"
    return _string_or_none(string.strip())


def field_577(string: str) -> str | None:
    "Via Code"
    return _string_or_none(string)


def field_578(string: str) -> str | None:
    "SID/STAR/IAP/Airway"
    return _string_or_none(string.strip())


def field_579(string: str) -> int | None:
    "Stopway"
    return _get_int(string)


def field_580(string: str) -> str | None:
    "ILS/MLS/GLS Category"
    return _string_or_none(string)


def field_581(string: str) -> str | None:
    "ATC Indicator"
    return _string_or_none(string)


def field_582(string: str) -> str | None:
    "Waypoint Usage"
    return _string_or_none(string)


def field_583(string: str) -> str | None:
    "To Fix"
    return _string_or_none(string.strip())


def field_584(string: str) -> str | None:
    "Runway Transition"
    return _string_or_none(string.strip())


def field_585(string: str) -> str | None:
    "Enroute Transition"
    return _string_or_none(string.strip())


def field_586(string: str) -> tuple[bool, int] | tuple[None, None]:
    "Cruise Altitude"
    return _get_altitude_fl(string)


def field_587(string: str) -> str | None:
    "Terminal/Alternate Airport"
    return _string_or_none(string.strip())


def field_588(string: str) -> int | None:
    "Alternate Distance"
    return _get_int(string)


def field_589(string: str) -> int | None:
    "Cost Index"
    return _get_int(string)


def field_590(string: str) -> float | None:
    "ILS/DME Bias"
    return _get_scaled_magnitude(string, -1)


def field_591(string: str) -> str | None:
    "Continuation Record Application Type"
    return _string_or_none(string)


def field_592(string: str) -> int | None:
    "Facility Elevation"
    return _get_int(string)


def field_593(string: str) -> str | None:
    "Facility Characteristics"
    return _string_or_none(string)


def field_594(string: str) -> float | None:
    "True Bearing"
    return _get_scaled_magnitude(string, -2)


def field_595(string: str) -> bool | None:
    "Government Source"
    return _get_bool(string)


def field_596(string: str) -> float | None:
    "Glide Slope Beam Width"
    return _get_scaled_magnitude(string, -2)


def field_597(string: str) -> int | None:
    "Touchdown Zone Elevation"
    return _get_int(string)


def field_598(string: str) -> str | None:
    "Touchdown Zone Elevation Location"
    return _string_or_none(string)


def field_599(string: str) -> str | None:
    "Marker Type"
    return _string_or_none(string)


def field_5100(string: str) -> float | None:
    "Minor Axis Bearing"
    return _get_scaled_magnitude(string, -1)


def field_5101(string: str) -> str | None:
    "Communication Type"
    return _string_or_none(string)


def field_5102(string: str) -> str | None:
    "Radar"
    return _string_or_none(string)


def field_5103(string: str, type: str) -> float | None:
    """
    Communication Frequency

    REQUIRES TYPE
    """
    if type in ["H", "U"]:
        return _get_scaled_magnitude(string, -2)
    if type == ["V", "C"]:
        return _get_scaled_magnitude(string, -3)
    return None


def field_5104(string: str) -> str | None:
    "Frequency Unit"
    return _string_or_none(string)


def field_5105(string: str) -> str | None:
    "Call Sign"
    return _string_or_none(string.strip())


def field_5106(string: str) -> str | None:
    "Service Indicator"
    return _string_or_none(string)


def field_5107(string: str) -> str | None:
    "ATA/IATA Designator"
    return _string_or_none(string.strip())


def field_5108(string: str) -> bool | None:
    "IFR Capability"
    return _get_bool(string)


def field_5109(string: str) -> int | None:
    "Runway Width"
    return _get_int(string)


def field_5110(string: str) -> str | None:
    "Marker Identifier"
    return _string_or_none(string)


def field_5111(string: str) -> str | None:
    "Marker Code"
    return _string_or_none(string)


def field_5112(string: str) -> str | None:
    "Marker Shape"
    return _string_or_none(string)


def field_5113(string: str) -> str | None:
    "High/Low"
    return _string_or_none(string)


def field_5114(string: str) -> str | None:
    "Duplicate Indicator"
    return _string_or_none(string)


def field_5115(string: str) -> str | None:
    "Directional Restriction"
    return _string_or_none(string)


def field_5116(string: str) -> str | None:
    "FIR/UIR Identifier"
    return _string_or_none(string)


def field_5117(string: str) -> str | None:
    "FIR/UIR Indicator"
    return _string_or_none(string)


def field_5118(string: str) -> str | None:
    "Boundary Via"
    return _string_or_none(string)


def field_5119(string: str) -> float | None:
    "Arc Distance"
    return _get_scaled_magnitude(string, -1)


def field_5120(string: str) -> float | None:
    "Arc Bearing"
    return _get_scaled_magnitude(string, -1)


def field_5121(string: str) -> str | None:
    "Lower/Upper Limit"
    return _string_or_none(string)


def field_5122(string: str) -> str | None:
    "FIR/UIR ATC Reporting Unit Speed"
    return _string_or_none(string)


def field_5123(string: str) -> str | None:
    "FIR/UIR ATC Reporting Unit Altitude"
    return _string_or_none(string)


def field_5124(string: str) -> bool | None:
    "FIR/UIR Entry Report"
    return _get_bool(string)


def field_5125(string: str) -> str | None:
    "FIR/UIR Name"
    return _string_or_none(string.strip())


def field_5126(string: str) -> str | None:
    "Restrictive Airspace Name"
    return _string_or_none(string.strip())


def field_5127(string: str) -> tuple[bool, int] | tuple[None, None]:
    "Maximum Altitude"
    return _get_altitude_fl(string)


def field_5128(string: str) -> str | None:
    "Restrictive Airspace Type"
    return _string_or_none(string)


def field_5129(string: str) -> str | None:
    "Restrictive Airspace Designation"
    return _string_or_none(string.strip())


def field_5130(string: str) -> str | None:
    "Multiple Code"
    return _string_or_none(string)


def field_5131(string: str) -> str | None:
    "Time Code"
    return _string_or_none(string)


def field_5132(string: str) -> str | None:
    "NOTAM"
    return _string_or_none(string)


def field_5133(string: str) -> str | None:
    "Unit Indicator"
    return _string_or_none(string)


def field_5134(string: str) -> str | None:
    "Cruise Table Indicator"
    return _string_or_none(string)


def field_5135(string: str) -> float | None:
    "Course From/To"
    return _get_course(string)


def field_5136(string: str) -> str | None:
    "Cruise Level From/To"
    return _string_or_none(string)


def field_5137(string: str) -> str | None:
    "Vertical Separation"
    return _string_or_none(string)


def field_5138(string: str) -> str | None:
    "Time Indicator"
    return _string_or_none(string)


# 5139 Reserved


def field_5140(string: str) -> str | None:
    "Controlling Agency"
    return _string_or_none(string.strip())


def field_5141(string: str) -> str | None:
    "Starting Latitude"
    return _string_or_none(string)


def field_5142(string: str) -> str | None:
    "Starting Longitude"
    return _string_or_none(string)


def field_5143(string: str) -> int | None:
    "Grid MORA"
    result = _get_scaled_magnitude(string, 2)
    if result != None:
        result = int(result)
    return result


def field_5144(string: str) -> str | None:
    "Center Fix"
    return _string_or_none(string.strip())


def field_5145(string: str) -> int | None:
    "Radius Limit"
    return _get_int(string)


def field_5146(string: str) -> str | None:
    "Sector Bearing"
    return _string_or_none(string)


def field_5147(string: str) -> int | None:
    "Sector Altitude"
    result = _get_scaled_magnitude(string, 2)
    if result != None:
        result = int(result)
    return result


def field_5148(string: str) -> str | None:
    "Enroute Alternate Airport"
    return _string_or_none(string.strip())


def field_5149(string: str) -> str | None:
    "Figure of Merit"
    return _string_or_none(string)


def field_5150(string: str) -> int | None:
    "Frequency Protection Distance"
    return _get_int(string)


def field_5151(string: str) -> str | None:
    "FIR/UIR Address"
    return _string_or_none(string.strip())


def field_5152(string: str) -> str | None:
    "Start/End Identifier"
    return _string_or_none(string)


def field_5153(string: str) -> str | None:
    "Start/End Date"
    return _string_or_none(string)


def field_5154(string: str) -> int | None:
    "Restriction Identifier"
    return _get_int(string)


# 5155 Reserved
# 5156 Reserved


def field_5157(string: str) -> str | None:
    "Airway Restriction Start/End Date"
    return _string_or_none(string)


# 5158 Reserved
# 5159 Reserved


def field_5160(string: str) -> str | None:
    "Units of Altitude"
    return _string_or_none(string)


def field_5161(string: str) -> int | None:
    "Restriction Altitude"
    return _get_int(string)


def field_5162(string: str) -> str | None:
    "Step Climb Indicator"
    return _string_or_none(string)


def field_5163(string: str) -> str | None:
    "Restriction Notes"
    return _string_or_none(string.strip())


def field_5164(string: str) -> str | None:
    "EU Indicator"
    return _string_or_none(string)


def field_5165(string: str) -> str | None:
    "Magnetic/True Indicator"
    return _string_or_none(string)


def field_5166(string: str) -> str | None:
    "Channel"
    return _string_or_none(string)


def field_5167(string: str) -> tuple[bool, float] | tuple[None, None]:
    "MLS Azimuth Bearing"
    return _get_magnetic_bearing_with_true(string)


def field_5168(string: str) -> int | None:
    "Azimuth Proportional Angle"
    return _get_int(string)


def field_5169(string: str) -> float | None:
    "Elevation Angle Span"
    return _get_scaled_magnitude(string, -1)


def field_5170(string: str) -> int | None:
    "Decision Height"
    return _get_int(string)


def field_5171(string: str) -> int | None:
    "Minimum Descent Height"
    return _get_int(string)


def field_5172(string: str) -> int | None:
    "Azimuth Coverage Sector Right/Left"
    return _get_int(string)


def field_5173(string: str) -> float | None:
    "Nominal Elevation Angle"
    return _get_scaled_magnitude(string, -2)


def field_5174(string: str) -> str | None:
    "Restrictive Airspace Link Continuation"
    return _string_or_none(string)


def field_5175(string: str) -> int | None:
    "Holding Speed"
    return _get_int(string)


def field_5176(string: str) -> str | None:
    "Pad Dimensions"
    return _string_or_none(string)


def field_5177(string: str) -> str | None:
    "Public/Military Indicator"
    return _string_or_none(string)


def field_5178(string: str) -> str | None:
    "Time Zone"
    return _string_or_none(string)


def field_5179(string: str) -> bool | None:
    "Daylight Time Indicator"
    return _get_bool(string)


def field_5180(string: str) -> str | None:
    "Pad Identifier"
    return _string_or_none(string.strip())


def field_5181(string: str) -> bool | None:
    "H24 Indicator"
    return _get_bool(string)


def field_5182(string: str) -> str | None:
    "Guard/Transmit"
    return _string_or_none(string)


def field_5183(string: str) -> str | None:
    "Sectorization"
    return _string_or_none(string)


def field_5184(string: str) -> tuple[bool, int] | tuple[None, None]:
    "Communication Altitude"
    return _get_altitude_fl(string)


def field_5185(string: str) -> str | None:
    "Sector Facility"
    return _string_or_none(string.strip())


def field_5186(string: str) -> str | None:
    "Narrative"
    return _string_or_none(string.strip())


def field_5187(string: str) -> str | None:
    "Distance Description"
    return _string_or_none(string)


def field_5188(string: str) -> int | None:
    "Communication Distance"
    return _get_int(string)


def field_5189(string: str) -> str | None:
    "Remote Site Name"
    return _string_or_none(string.strip())


def field_5190(string: str) -> str | None:
    "FIR/RDO Identifier"
    return _string_or_none(string.strip())


# 5191 Reserved
# 5192 Reserved
# 5193 Reserved
def field_5194(string: str) -> str | None:
    "Initial/Terminus Airport/Fix"
    return _string_or_none(string.strip())


def field_5195(string: str) -> str | None:
    "Time of Operation"
    return _string_or_none(string)


def field_5196(string: str) -> str | None:
    "Name Format Indicator"
    return _string_or_none(string)


def field_5197(string: str) -> str | None:
    "Datum Code"
    return _string_or_none(string.strip())


def field_5198(string: str) -> str | None:
    "Modulation"
    return _string_or_none(string)


def field_5199(string: str) -> str | None:
    "Signal Emission"
    return _string_or_none(string)


def field_5200(string: str) -> str | None:
    "Remote Facility"
    return _string_or_none(string.strip())


def field_5201(string: str) -> str | None:
    "Restriction Record Type"
    return _string_or_none(string)


def field_5202(string: str) -> str | None:
    "Exclusion Indicator"
    return _string_or_none(string)


def field_5203(string: str) -> str | None:
    "Block Indicator"
    return _string_or_none(string)


def field_5204(string: str) -> float | None:
    "Arc Radius"
    return _get_scaled_magnitude(string, -3)


def field_5205(string: str) -> str | None:
    "NAVAID Limitation Code"
    return _string_or_none(string)


def field_5206(string: str) -> str | None:
    "Component Affected Indicator"
    return _string_or_none(string)


def field_5207(string: str) -> str | None:
    "Sector From/To"
    return _string_or_none(string)


def field_5208(string: str) -> str | None:
    "Distance Limitation"
    return _string_or_none(string)


def field_5209(string: str) -> str | None:
    "Altitude Limitation"
    return _string_or_none(string)


def field_5210(string: str) -> str | None:
    "Sequence End Indicator"
    return _string_or_none(string)


def field_5211(string: str) -> float | None:
    "Required Navigation Performance"
    if string[0:1] == "0":
        value = string[1:2]
        exponent = -int(string[2:3])
        return _get_scaled_magnitude(value, exponent)
    return _get_scaled_magnitude(string, -1)


def field_5212(string: str) -> float | None:
    "Runway Gradient"
    return _get_signed_value(string, -2)


def field_5213(string: str) -> str | None:
    "Controlled Airspace Type"
    return _string_or_none(string)


def field_5214(string: str) -> str | None:
    "Controlled Airspace Center"
    return _string_or_none(string.strip())


def field_5215(string: str) -> str | None:
    "Controlled Airspace Classification"
    return _string_or_none(string)


def field_5216(string: str) -> str | None:
    "Controlled Airspace Name"
    return _string_or_none(string.strip())


def field_5217(string: str) -> str | None:
    "Controlled Airspace Indicator"
    return _string_or_none(string)


def field_5218(string: str) -> str | None:
    "Geographical Reference Table Identifier"
    return _string_or_none(string)


def field_5219(string: str) -> str | None:
    "Geographical Entity"
    return _string_or_none(string.strip())


def field_5220(string: str) -> str | None:
    "Preferred Route Use Indicator"
    return _string_or_none(string)


def field_5221(string: str) -> str | None:
    "Aircraft Use Group"
    return _string_or_none(string)


def field_5222(string: str) -> str | None:
    "GNSS/FMS Indicator"
    return _string_or_none(string)


def field_5223(string: str) -> str | None:
    "Operation Type"
    return _string_or_none(string)


def field_5224(string: str) -> str | None:
    "Route Indicator"
    return _string_or_none(string)


def field_5225(string: str) -> float | None:
    "Ellipsoidal Height"
    return _get_signed_value(string)


def field_5226(string: str) -> float | None:
    "Glide Path Angle"
    return _get_scaled_magnitude(string, -2)


def field_5227(string: str) -> float | None:
    "Orthometric Height"
    return _get_scaled_magnitude(string, -1)


def field_5228(string: str) -> float | None:
    "Course Width At Threshold"
    return _get_scaled_magnitude(string, -2)


def field_5229(string: str) -> str | None:
    "Final Approach Segment data CRC Remainder"
    return _string_or_none(string)


def field_5230(string: str) -> str | None:
    "Procedure Type"
    return _string_or_none(string)


def field_5231(string: str) -> int | None:
    "Along Track Distance"
    return _get_int(string)


def field_5232(string: str) -> str | None:
    "Number of Engines Restriction"
    return _string_or_none(string)


def field_5233(string: str) -> str | None:
    "Turboprop/Jet Indicator"
    return _string_or_none(string)


def field_5234(string: str) -> bool | None:
    "RNAV Flag"
    return _get_bool(string)


def field_5235(string: str) -> str | None:
    "ATC Weight Category"
    return _string_or_none(string)


def field_5236(string: str) -> str | None:
    "ATC Identifier"
    return _string_or_none(string.strip())


def field_5237(string: str) -> str | None:
    "Procedure Description"
    return _string_or_none(string.strip())


def field_5238(string: str) -> str | None:
    "Leg Type Code"
    return _string_or_none(string)


def field_5239(string: str) -> str | None:
    "Reporting Code"
    return _string_or_none(string)


def field_5240(string: str) -> tuple[bool, int] | tuple[None, None]:
    "Altitude"
    return _get_altitude_fl(string)


def field_5241(string: str) -> str | None:
    "Fix Related Transition Code"
    return _string_or_none(string)


def field_5242(string: str) -> str | None:
    "Procedure Category"
    return _string_or_none(string.strip())


def field_5243(string: str) -> str | None:
    "GLS Station Identifier"
    return _string_or_none(string.strip())


def field_5244(string: str) -> str | None:
    "GLS Channel"
    return _string_or_none(string)


def field_5245(string: str) -> int | None:
    "Service Volume Radius"
    return _get_int(string)


def field_5246(string: str) -> str | None:
    "TDMA Slots"
    return _string_or_none(string)


def field_5247(string: str) -> str | None:
    "Station Type"
    return _string_or_none(string)


def field_5248(string: str) -> int | None:
    "Station Elevation WGS84"
    return _get_int(string)


def field_5249(string: str) -> str | None:
    "Longest Runway Surface Code"
    return _string_or_none(string)


def field_5250(string: str) -> str | None:
    "Alternate Record Type"
    return _string_or_none(string)


def field_5251(string: str) -> int | None:
    "Distance to Alternate"
    return _get_int(string)


def field_5252(string: str) -> str | None:
    "Alternate Type"
    return _string_or_none(string)


def field_5253(string: str) -> str | None:
    "Primary and Additional Alternate Identifier"
    return _string_or_none(string.strip())


def field_5254(string: str) -> float | None:
    "Fix Radius Transition Indicator"
    return _get_scaled_magnitude(string, -1)


def field_5255(string: str) -> str | None:
    "SBAS Service Provider Identifier"
    return _string_or_none(string)


def field_5256(string: str) -> str | None:
    "Reference Path Data Selector"
    return _string_or_none(string)


def field_5257(string: str) -> str | None:
    "Reference Path Identifier"
    return _string_or_none(string)


def field_5258(string: str) -> str | None:
    "Approach Performance Designator"
    return _string_or_none(string)


def field_5259(string: str) -> int | None:
    "Length Offset"
    return _get_int(string)


def field_5260(string: str) -> float | None:
    "Terminal Procedure Flight Planning Leg Distance"
    return _get_scaled_magnitude(string, -1)


def field_5261(string: str) -> str | None:
    "Speed Limit Description"
    return _string_or_none(string)


def field_5262(string: str) -> str | None:
    "Approach Type Identifier"
    return _string_or_none(string.strip())


def field_5263(string: str) -> float | None:
    "HAL"
    return _get_scaled_magnitude(string, -1)


def field_5264(string: str) -> float | None:
    "VAL"
    return _get_scaled_magnitude(string, -1)


def field_5265(string: str, type: str) -> float | None:
    """
    Path Point TCH

    REQUIRES TYPE
    """
    if _check_empty_string(string) or not string.isnumeric():
        return None
    if type == "F":
        return _get_scaled_magnitude(string, -1)
    if type == "M":
        return _get_scaled_magnitude(string, -2)
    return None


def field_5266(string: str) -> str | None:
    "TCH Units Indicator"
    return _string_or_none(string)


def field_5267(string: str) -> float | None:
    "High Precision Latitude"
    return _get_lat(string, True)


def field_5268(string: str) -> float | None:
    "High Precision Longitude"
    return _get_lon(string, True)


def field_5269(string: str) -> int | None:
    "Helicopter Procedure Course"
    return _get_int(string)


def field_5270(string: str) -> str | None:
    "TCH Value Indicator"
    return _string_or_none(string)


def field_5271(string: str) -> str | None:
    "Procedure Turn"
    return _string_or_none(string.strip())


def field_5272(string: str) -> str | None:
    "TAA Sector Identifier"
    return _string_or_none(string)


def field_5273(string: str) -> str | None:
    "TAA IAF Waypoint"
    return _string_or_none(string.strip())


def field_5274(string: str) -> str | None:
    "TAA Sector Radius"
    return _string_or_none(string)


def field_5275(string: str) -> str | None:
    "Level of Service Name"
    return _string_or_none(string.strip())


def field_5276(string: str) -> bool | None:
    "Level of Service Authorized"
    if string == "A":
        return True
    if string == "N":
        return False
    return None
