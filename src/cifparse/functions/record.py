def _check_int_value(check_string: str) -> int:
    return int(check_string) if check_string.isnumeric() else 0


def _get_altitude_fl(string: str) -> tuple[bool, int]:
    if string[:2] == "FL":
        if string[2:].isnumeric():
            return (True, int(string[2:]))
    else:
        if string.isnumeric():
            return (False, int(string))
    return (None, None)


def _get_bool(string: str) -> bool:
    if string == "Y":
        return True
    if string == "N":
        return False
    return None


def _get_int(string: str) -> int:
    if string == "" or not string.isnumeric():
        return None
    return int(string)


def _get_course(string: str) -> float:
    if string == "" or not string.isnumeric():
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


def _get_magnetic_bearing_with_true(string: str) -> tuple[bool, float]:
    if string == "":
        return (None, None)
    if string[-1] == "T":
        if string[:-1].isnumeric():
            return (True, int(string[:-1]))
    else:
        if string.isnumeric():
            return (False, _get_scaled_magnitude(string, -1))
    return (None, None)


def _get_scaled_int(int: int, scalar: int) -> float:
    return round(int * (10**scalar), abs(scalar))


def _get_scaled_magnitude(string: str, scalar: int) -> float:
    if string == "" or not string.isnumeric():
        return None
    return _get_scaled_int(int(string), scalar)


def _get_signed_value(string: str, scalar: int = -1) -> int:
    sign = string[:1]
    value = string
    if sign in ["+", "-"]:
        value = string[1:]
    result = _get_scaled_magnitude(value, scalar)
    if sign == "-" and result:
        return -result
    return result


def field_52(string: str) -> str:
    "Record Type (S/T)"
    return string


def field_53(string: str) -> str:
    "Customer/Area"
    return string


def field_54(string: str) -> str:
    "Section Code"
    return string


def field_55(string: str) -> str:
    "Subsection Code"
    return string


def field_56(string: str) -> str:
    "Airport/Heliport ID"
    return string.strip()


def field_57(string: str) -> str:
    "Route Type"
    return string


def field_58(string: str) -> str:
    "Route ID"
    return string.strip()


def field_59(string: str) -> str:
    "SID/STAR Route ID"
    return string.strip()


def field_510(string: str) -> str:
    "IAP Route ID"
    return string.strip()


def field_511(string: str) -> str:
    "Transition ID"
    return string.strip()


def field_512(string: str) -> int:
    "Sequence Number"
    return _get_int(string)


def field_513(string: str) -> str:
    "Fix Identifier"
    return string.strip()


def field_514(string: str) -> str:
    "ICAO Code/Region"
    return string.strip()


# 515 Reserved


def field_516(string: str) -> str:
    "Continuation Record Number"
    if string.isnumeric():
        return int(string)
    result = string.upper()
    if "A" <= result <= "Z":
        return ord(result) - ord("A")
    return 0


def field_517(string: str) -> str:
    "Waypoint Description Code"
    return string


def field_518(string: str) -> str:
    "Boundary Code"
    return string


def field_519(string: str) -> str:
    "Level"
    return string


def field_520(string: str) -> str:
    "Turn Direction"
    return string


def field_521(string: str) -> str:
    "Path and Termination"
    return string


def field_522(string: str) -> str:
    "Turn Direction Valid"
    return string


def field_523(string: str) -> str:
    "Recommended NAVAID"
    return string.strip()


def field_524(string: str) -> float:
    "Theta"
    if string == "" or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def field_525(string: str) -> float:
    "Rho"
    if string == "" or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def field_526(string: str) -> tuple[bool, float]:
    "Outbound Magnetic Course"
    return _get_magnetic_bearing_with_true(string)


def field_527(string: str) -> tuple[bool, float]:
    "Route Distance From, Holding Distance/Time"
    if string[:1] == "T":
        if string[1:].isnumeric():
            return (1, int(string[1:]))
    else:
        if string.isnumeric():
            return (0, _get_scaled_magnitude(string, -1))
    return (None, None)


def field_528(string: str) -> tuple[bool, float]:
    "Inbound Magnetic Course"
    return _get_magnetic_bearing_with_true(string)


def field_529(string: str) -> str:
    "Altitude Description"
    return string


def field_530(string: str) -> tuple[bool, int]:
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


def field_531(string: str) -> int:
    "File Record Number"
    return _get_int(string)


def field_532(string: str) -> str:
    "Cycle Date"
    return string


def field_533(string: str) -> str:
    "VOR/NDB Identifier"
    return string.strip()


def field_534(string: str, type: str) -> float:
    """
    VOR/NDB Frequency

    REQUIRES TYPE
    """
    if string == "" or not string.isnumeric():
        return None
    if type == "VOR":
        return _get_scaled_magnitude(string, -2)
    if type == "NDB":
        return _get_scaled_magnitude(string, -1)
    return None


def field_535(string: str) -> str:
    "NAVAID Class"
    return string


def field_536(string: str) -> float:
    "Latitude"
    if string == "":
        return None
    return _get_lat(string)


def field_537(string: str) -> float:
    "Longitude"
    if string == "":
        return None
    return _get_lon(string)


def field_538(string: str) -> str:
    "DME Identifier"
    return string.strip()


def field_539(string: str) -> float:
    "Magnetic Variation"
    if string == "" or not string[1:].isnumeric():
        return None
    if string[:1] == "T":
        return 0
    result = _get_scaled_magnitude(string[1:], -1)
    if string[:1] == "W":
        result = -result
    return result


def field_540(string: str) -> int:
    "DME Elevation"
    return _get_int(string)


def field_541(string: str) -> str:
    "Region Code"
    return string.strip()


def field_542(string: str) -> str:
    "Waypoint Type"
    return string


def field_543(string: str) -> str:
    "Waypoint Name/Description"
    return string.strip()


def field_544(string: str) -> str:
    "Localizer/MLS/GLS Identifier"
    return string.strip()


def field_545(string: str) -> float:
    "Localizer Frequency"
    if string == "" or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -2)


def field_546(string: str) -> str:
    "Runway Identifier"
    return string.strip()


def field_547(string: str) -> tuple[bool, float]:
    "Localizer Bearing"
    return _get_magnetic_bearing_with_true(string)


def field_548(string: str) -> int:
    "Localizer Position"
    return _get_int(string)


def field_549(string: str) -> str:
    "Localizer/Azimuth Position Reference"
    return string


def field_550(string: str) -> int:
    "Glide Slope Position / Elevation Position"
    return _get_int(string)


def field_551(string: str) -> float:
    "Localizer Width"
    if string == "" or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -2)


def field_552(string: str) -> float:
    "Glide Slope Angle / Minimum Elevation Angle"
    if string == "" or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -2)


def field_553(string: str) -> int:
    "Transition Altitude/Level"
    return _get_int(string)


def field_554(string: str) -> int:
    "Longest Runway"
    return _get_scaled_magnitude(string, 2)


def field_555(string: str) -> int:
    "Airport/Heliport Elevation"
    return _get_int(string)


def field_556(string: str) -> str:
    "Gate Identifier"
    return string.strip()


def field_557(string: str) -> int:
    "Runway Length"
    return _get_int(string)


def field_558(string: str) -> tuple[bool, float]:
    "Runway Magnetic Bearing"
    return _get_magnetic_bearing_with_true(string)


def field_559(string: str) -> str:
    "Runway Description"
    return string.strip()


def field_560(string: str) -> str:
    "Name"
    return string.strip()


def field_561(string: str) -> str:
    "Notes"
    return string.strip()


def field_562(string: str) -> tuple[bool, float]:
    "Inbound Holding Course"
    return _get_magnetic_bearing_with_true(string)


def field_563(string: str) -> str:
    "Turn"
    return string


def field_564(string: str) -> float:
    "Leg Length"
    if string == "" or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def field_565(string: str) -> float:
    "Leg Time"
    if string == "" or not string.isnumeric():
        return None
    return _get_scaled_magnitude(string, -1)


def field_566(string: str) -> float:
    "Station Declination"
    if string == "" or not string[1:].isnumeric():
        return None
    if string[:1] in ["G", "T"]:
        return 0
    result = _get_scaled_magnitude(string[1:], -1)
    if string[:1] == "W":
        result = -result
    return result


def field_567(string: str) -> int:
    "Threshold Crossing Height"
    return _get_int(string)


def field_568(string: str) -> int:
    "Landing Threshold Elevation"
    return _get_int(string)


def field_569(string: str) -> int:
    "Threshold Displacement Distance"
    return _get_int(string)


def field_570(string: str) -> float:
    "Vertical Angle"
    return _get_scaled_magnitude(string, -2)


def field_571(string: str) -> str:
    "Name Field"
    return string.strip()


def field_572(string: str) -> int:
    "Speed Limit"
    return _get_int(string)


def field_573(string: str) -> tuple[bool, int]:
    "Speed Limit Altitude"
    return _get_altitude_fl(string)


def field_574(string: str) -> int:
    "Component Elevation"
    return _get_int(string)


def field_575(string: str) -> str:
    "From/To - Airport/Fix"
    return string.strip()


def field_576(string: str) -> str:
    "Company Route Identifier"
    return string.strip()


def field_577(string: str) -> str:
    "Via Code"
    return string


def field_578(string: str) -> str:
    "SID/STAR/IAP/Airway"
    return string.strip()


def field_579(string: str) -> int:
    "Stopway"
    return _get_int(string)


def field_580(string: str) -> str:
    "ILS/MLS/GLS Category"
    return string


def field_581(string: str) -> str:
    "ATC Indicator"
    return string


def field_582(string: str) -> str:
    "Waypoint Usage"
    return string


def field_583(string: str) -> str:
    "To Fix"
    return string.strip()


def field_584(string: str) -> str:
    "Runway Transition"
    return string.strip()


def field_585(string: str) -> str:
    "Enroute Transition"
    return string.strip()


def field_586(string: str) -> tuple[bool, int]:
    "Cruise Altitude"
    return _get_altitude_fl(string)


def field_587(string: str) -> str:
    "Terminal/Alternate Airport"
    return string.strip()


def field_588(string: str) -> int:
    "Alternate Distance"
    return _get_int(string)


def field_589(string: str) -> int:
    "Cost Index"
    return _get_int(string)


def field_590(string: str) -> float:
    "ILS/DME Bias"
    return _get_scaled_magnitude(string, -1)


def field_591(string: str) -> str:
    "Continuation Record Application Type"
    return string


def field_592(string: str) -> int:
    "Facility Elevation"
    return _get_int(string)


def field_593(string: str) -> str:
    "Facility Characteristics"
    return string


def field_594(string: str) -> float:
    "True Bearing"
    return _get_scaled_magnitude(string, -2)


def field_595(string: str) -> bool:
    "Government Source"
    return _get_bool(string)


def field_596(string: str) -> float:
    "Glide Slope Beam Width"
    return _get_scaled_magnitude(string, -2)


def field_597(string: str) -> int:
    "Touchdown Zone Elevation"
    return _get_int(string)


def field_598(string: str) -> str:
    "Touchdown Zone Elevation Location"
    return string


def field_599(string: str) -> str:
    "Marker Type"
    return string


def field_5100(string: str) -> float:
    "Minor Axis Bearing"
    return _get_scaled_magnitude(string, -1)


def field_5101(string: str) -> str:
    "Communication Type"
    return string


def field_5102(string: str) -> str:
    "Radar"
    return string


def field_5103(string: str, type: str) -> float:
    """
    Communication Frequency

    REQUIRES TYPE
    """
    if type in ["H", "U"]:
        return _get_scaled_magnitude(string, -2)
    if type == ["V", "C"]:
        return _get_scaled_magnitude(string, -3)
    return None


def field_5104(string: str) -> str:
    "Frequency Unit"
    return string


def field_5105(string: str) -> str:
    "Call Sign"
    return string.strip()


def field_5106(string: str) -> str:
    "Service Indicator"
    return string


def field_5107(string: str) -> str:
    "ATA/IATA Designator"
    return string.strip()


def field_5108(string: str) -> bool:
    "IFR Capability"
    return _get_bool(string)


def field_5109(string: str) -> int:
    "Runway Width"
    return _get_int(string)


def field_5110(string: str) -> str:
    "Marker Identifier"
    return string


def field_5111(string: str) -> str:
    "Marker Code"
    return string


def field_5112(string: str) -> str:
    "Marker Shape"
    return string


def field_5113(string: str) -> str:
    "High/Low"
    return string


def field_5114(string: str) -> str:
    "Duplicate Indicator"
    return string


def field_5115(string: str) -> str:
    "Directional Restriction"
    return string


def field_5116(string: str) -> str:
    "FIR/UIR Identifier"
    return string


def field_5117(string: str) -> str:
    "FIR/UIR Indicator"
    return string


def field_5118(string: str) -> str:
    "Boundary Via"
    return string


def field_5119(string: str) -> float:
    "Arc Distance"
    return _get_scaled_magnitude(string, -1)


def field_5120(string: str) -> float:
    "Arc Bearing"
    return _get_scaled_magnitude(string, -1)


def field_5121(string: str) -> str:
    "Lower/Upper Limit"
    return string


def field_5122(string: str) -> str:
    "FIR/UIR ATC Reporting Unit Speed"
    return string


def field_5123(string: str) -> str:
    "FIR/UIR ATC Reporting Unit Altitude"
    return string


def field_5124(string: str) -> bool:
    "FIR/UIR Entry Report"
    return _get_bool(string)


def field_5125(string: str) -> str:
    "FIR/UIR Name"
    return string.strip()


def field_5126(string: str) -> str:
    "Restrictive Airspace Name"
    return string.strip()


def field_5127(string: str) -> tuple[bool, int]:
    "Maximum Altitude"
    return _get_altitude_fl(string)


def field_5128(string: str) -> str:
    "Restrictive Airspace Type"
    return string


def field_5129(string: str) -> str:
    "Restrictive Airspace Designation"
    return string.strip()


def field_5130(string: str) -> str:
    "Multiple Code"
    return string


def field_5131(string: str) -> str:
    "Time Code"
    return string


def field_5132(string: str) -> str:
    "NOTAM"
    return string


def field_5133(string: str) -> str:
    "Unit Indicator"
    return string


def field_5134(string: str) -> str:
    "Cruise Table Indicator"
    return string


def field_5135(string: str) -> float:
    "Course From/To"
    return _get_course(string)


def field_5136(string: str) -> str:
    "Cruise Level From/To"
    return string


def field_5137(string: str) -> str:
    "Vertical Separation"
    return string


def field_5138(string: str) -> str:
    "Time Indicator"
    return string


# 5139 Reserved


def field_5140(string: str) -> str:
    "Controlling Agency"
    return string.strip()


def field_5141(string: str) -> str:
    "Starting Latitude"
    return string


def field_5142(string: str) -> str:
    "Starting Longitude"
    return string


def field_5143(string: str) -> int:
    "Grid MORA"
    return _get_scaled_magnitude(string, 2)


def field_5144(string: str) -> str:
    "Center Fix"
    return string.strip()


def field_5145(string: str) -> int:
    "Radius Limit"
    return _get_int(string)


def field_5146(string: str) -> str:
    "Sector Bearing"
    return string


def field_5147(string: str) -> int:
    "Sector Altitude"
    return _get_scaled_magnitude(string, 2)


def field_5148(string: str) -> str:
    "Enroute Alternate Airport"
    return string.strip()


def field_5149(string: str) -> str:
    "Figure of Merit"
    return string


def field_5150(string: str) -> int:
    "Frequency Protection Distance"
    return _get_int(string)


def field_5151(string: str) -> str:
    "FIR/UIR Address"
    return string.strip()


def field_5152(string: str) -> str:
    "Start/End Identifier"
    return string


def field_5153(string: str) -> str:
    "Start/End Date"
    return string


def field_5154(string: str) -> int:
    "Restriction Identifier"
    return _get_int(string)


# 5155 Reserved
# 5156 Reserved


def field_5157(string: str) -> str:
    "Airway Restriction Start/End Date"
    return string


# 5158 Reserved
# 5159 Reserved


def field_5160(string: str) -> str:
    "Units of Altitude"
    return string


def field_5161(string: str) -> int:
    "Restriction Altitude"
    return _get_int(string)


def field_5162(string: str) -> str:
    "Step Climb Indicator"
    return string


def field_5163(string: str) -> str:
    "Restriction Notes"
    return string.strip()


def field_5164(string: str) -> str:
    "EU Indicator"
    return string


def field_5165(string: str) -> str:
    "Magnetic/True Indicator"
    return string


def field_5166(string: str) -> str:
    "Channel"
    return string


def field_5167(string: str) -> tuple[bool, float]:
    "MLS Azimuth Bearing"
    return _get_magnetic_bearing_with_true(string)


def field_5168(string: str) -> int:
    "Azimuth Proportional Angle"
    return _get_int(string)


def field_5169(string: str) -> float:
    "Elevation Angle Span"
    return _get_scaled_magnitude(string, -1)


def field_5170(string: str) -> int:
    "Decision Height"
    return _get_int(string)


def field_5171(string: str) -> int:
    "Minimum Descent Height"
    return _get_int(string)


def field_5172(string: str) -> int:
    "Azimuth Coverage Sector Right/Left"
    return _get_int(string)


def field_5173(string: str) -> float:
    "Nominal Elevation Angle"
    return _get_scaled_magnitude(string, -2)


def field_5174(string: str) -> str:
    "Restrictive Airspace Link Continuation"
    return string


def field_5175(string: str) -> int:
    "Holding Speed"
    return _get_int(string)


def field_5176(string: str) -> str:
    "Pad Dimensions"
    return string


def field_5177(string: str) -> str:
    "Public/Military Indicator"
    return string


def field_5178(string: str) -> str:
    "Time Zone"
    return string


def field_5179(string: str) -> bool:
    "Daylight Time Indicator"
    return _get_bool(string)


def field_5180(string: str) -> str:
    "Pad Identifier"
    return string.strip()


def field_5181(string: str) -> bool:
    "H24 Indicator"
    return _get_bool(string)


def field_5182(string: str) -> str:
    "Guard/Transmit"
    return string


def field_5183(string: str) -> str:
    "Sectorization"
    return string


def field_5184(string: str) -> tuple[bool, int]:
    "Communication Altitude"
    return _get_altitude_fl(string)


def field_5185(string: str) -> str:
    "Sector Facility"
    return string.strip()


def field_5186(string: str) -> str:
    "Narrative"
    return string.strip()


def field_5187(string: str) -> str:
    "Distance Description"
    return string


def field_5188(string: str) -> int:
    "Communication Distance"
    return _get_int(string)


def field_5189(string: str) -> str:
    "Remote Site Name"
    return string.strip()


def field_5190(string: str) -> str:
    "FIR/RDO Identifier"
    return string.strip()


# 5191 Reserved
# 5192 Reserved
# 5193 Reserved
def field_5194(string: str) -> str:
    "Initial/Terminus Airport/Fix"
    return string.strip()


def field_5195(string: str) -> str:
    "Time of Operation"
    return string


def field_5196(string: str) -> str:
    "Name Format Indicator"
    return string


def field_5197(string: str) -> str:
    "Datum Code"
    return string.strip()


def field_5198(string: str) -> str:
    "Modulation"
    return string


def field_5199(string: str) -> str:
    "Signal Emission"
    return string


def field_5200(string: str) -> str:
    "Remote Facility"
    return string.strip()


def field_5201(string: str) -> str:
    "Restriction Record Type"
    return string


def field_5202(string: str) -> str:
    "Exclusion Indicator"
    return string


def field_5203(string: str) -> str:
    "Block Indicator"
    return string


def field_5204(string: str) -> float:
    "Arc Radius"
    return _get_scaled_magnitude(string, -3)


def field_5205(string: str) -> str:
    "NAVAID Limitation Code"
    return string


def field_5206(string: str) -> str:
    "Component Affected Indicator"
    return string


def field_5207(string: str) -> str:
    "Sector From/To"
    return string


def field_5208(string: str) -> str:
    "Distance Limitation"
    return string


def field_5209(string: str) -> str:
    "Altitude Limitation"
    return string


def field_5210(string: str) -> str:
    "Sequence End Indicator"
    return string


def field_5211(string: str) -> float:
    "Required Navigation Performance"
    if string[0:1] == "0":
        value = string[1:2]
        exponent = -int(string[2:3])
        return _get_scaled_magnitude(value, exponent)
    return _get_scaled_magnitude(string, -1)


def field_5212(string: str) -> float:
    "Runway Gradient"
    return _get_signed_value(string, -2)


def field_5213(string: str) -> str:
    "Controlled Airspace Type"
    return string


def field_5214(string: str) -> str:
    "Controlled Airspace Center"
    return string.strip()


def field_5215(string: str) -> str:
    "Controlled Airspace Classification"
    return string


def field_5216(string: str) -> str:
    "Controlled Airspace Name"
    return string.strip()


def field_5217(string: str) -> str:
    "Controlled Airspace Indicator"
    return string


def field_5218(string: str) -> str:
    "Geographical Reference Table Identifier"
    return string


def field_5219(string: str) -> str:
    "Geographical Entity"
    return string.strip()


def field_5220(string: str) -> str:
    "Preferred Route Use Indicator"
    return string


def field_5221(string: str) -> str:
    "Aircraft Use Group"
    return string


def field_5222(string: str) -> str:
    "GNSS/FMS Indicator"
    return string


def field_5223(string: str) -> str:
    "Operation Type"
    return string


def field_5224(string: str) -> str:
    "Route Indicator"
    return string


def field_5225(string: str) -> float:
    "Ellipsoidal Height"
    return _get_signed_value(string)


def field_5226(string: str) -> float:
    "Glide Path Angle"
    return _get_scaled_magnitude(string, -2)


def field_5227(string: str) -> float:
    "Orthometric Height"
    return _get_scaled_magnitude(string, -1)


def field_5228(string: str) -> float:
    "Course Width At Threshold"
    return _get_scaled_magnitude(string, -2)


def field_5229(string: str) -> str:
    "Final Approach Segment data CRC Remainder"
    return string


def field_5230(string: str) -> str:
    "Procedure Type"
    return string


def field_5231(string: str) -> int:
    "Along Track Distance"
    return _get_int(string)


def field_5232(string: str) -> str:
    "Number of Engines Restriction"
    return string


def field_5233(string: str) -> str:
    "Turboprop/Jet Indicator"
    return string


def field_5234(string: str) -> bool:
    "RNAV Flag"
    return _get_bool(string)


def field_5235(string: str) -> str:
    "ATC Weight Category"
    return string


def field_5236(string: str) -> str:
    "ATC Identifier"
    return string.strip()


def field_5237(string: str) -> str:
    "Procedure Description"
    return string.strip()


def field_5238(string: str) -> str:
    "Leg Type Code"
    return string


def field_5239(string: str) -> str:
    "Reporting Code"
    return string


def field_5240(string: str) -> tuple[bool, int]:
    "Altitude"
    return _get_altitude_fl(string)


def field_5241(string: str) -> str:
    "Fix Related Transition Code"
    return string


def field_5242(string: str) -> str:
    "Procedure Category"
    return string.strip()


def field_5243(string: str) -> str:
    "GLS Station Identifier"
    return string.strip()


def field_5244(string: str) -> str:
    "GLS Channel"
    return string


def field_5245(string: str) -> int:
    "Service Volume Radius"
    return _get_int(string)


def field_5246(string: str) -> str:
    "TDMA Slots"
    return string


def field_5247(string: str) -> str:
    "Station Type"
    return string


def field_5248(string: str) -> int:
    "Station Elevation WGS84"
    return _get_int(string)


def field_5249(string: str) -> str:
    "Longest Runway Surface Code"
    return string


def field_5250(string: str) -> str:
    "Alternate Record Type"
    return string


def field_5251(string: str) -> int:
    "Distance to Alternate"
    return _get_int(string)


def field_5252(string: str) -> str:
    "Alternate Type"
    return string


def field_5253(string: str) -> str:
    "Primary and Additional Alternate Identifier"
    return string.strip()


def field_5254(string: str) -> float:
    "Fix Radius Transition Indicator"
    return _get_scaled_magnitude(string, -1)


def field_5255(string: str) -> str:
    "SBAS Service Provider Identifier"
    return string


def field_5256(string: str) -> str:
    "Reference Path Data Selector"
    return string


def field_5257(string: str) -> str:
    "Reference Path Identifier"
    return string


def field_5258(string: str) -> str:
    "Approach Performance Designator"
    return string


def field_5259(string: str) -> int:
    "Length Offset"
    return _get_int(string)


def field_5260(string: str) -> float:
    "Terminal Procedure Flight Planning Leg Distance"
    return _get_scaled_magnitude(string, -1)


def field_5261(string: str) -> str:
    "Speed Limit Description"
    return string


def field_5262(string: str) -> str:
    "Approach Type Identifier"
    return string.strip()


def field_5263(string: str) -> float:
    "HAL"
    return _get_scaled_magnitude(string, -1)


def field_5264(string: str) -> float:
    "VAL"
    return _get_scaled_magnitude(string, -1)


def field_5265(string: str, type: str) -> float:
    """
    Path Point TCH

    REQUIRES TYPE
    """
    if string == "" or not string.isnumeric():
        return None
    if type == "F":
        return _get_scaled_magnitude(string, -1)
    if type == "M":
        return _get_scaled_magnitude(string, -2)
    return None


def field_5266(string: str) -> str:
    "TCH Units Indicator"
    return string


def field_5267(string: str) -> float:
    "High Precision Latitude"
    return _get_lat(string, True)


def field_5268(string: str) -> float:
    "High Precision Longitude"
    return _get_lon(string, True)


def field_5269(string: str) -> int:
    "Helicopter Procedure Course"
    return _get_int(string)


def field_5270(string: str) -> str:
    "TCH Value Indicator"
    return string


def field_5271(string: str) -> str:
    "Procedure Turn"
    return string.strip()


def field_5272(string: str) -> str:
    "TAA Sector Identifier"
    return string


def field_5273(string: str) -> str:
    "TAA IAF Waypoint"
    return string.strip()


def field_5274(string: str) -> str:
    "TAA Sector Radius"
    return string


def field_5275(string: str) -> str:
    "Level of Service Name"
    return string.strip()


def field_5276(string: str) -> bool:
    "Level of Service Authorized"
    if string == "A":
        return True
    if string == "N":
        return False
    return None
