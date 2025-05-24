# The Airport Object

The Airport object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- airport_id: The ICAO code of the airport.
- airport_region: The ICAO region (e.g. `K6` for NE US).
- sub_code: The subsection code, used in parsing.
- iata: The IATA code of the airport.
- cont_rec_no: The continuation record number, used in parsing.
- fl: A boolean value to note that `limit_alt` is true rather than magnetic.
- limit_alt: The speed limit altitude.
- longest: The longest runway length.
- is_ifr: An IFR capability marker.
- longest_surface: The surface type of the longest runway.
- lat: The airport reference point latitude.
- lon: The airport reference point longitude.
- mag_var: The magnetic variation.
- elevation: The field elevation.
- limit_speed: The speed limit.
- rec_vhf: The recommended/associated navaid.
- rec_vhf_region: The region of the recommended/associated navaid.
- transition_alt: The transition altitude.
- transition_level: The transition level.
- usage: The use type (e.g. Civilian or Military).
- time_zone: The time zone.
- daylight_ind: A DST marker.
- mag_true: A marker for magnetic or true heading usage.
- datum_code: The reference system used in surveying.
- airport_name: The name of the airport.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
