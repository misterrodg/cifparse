# The Heliport Object

The Heliport object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- heliport_id: The ICAO code of the heliport.
- heliport_region: The ICAO region (e.g. `K6` for NE US).
- sub_code: The subsection code, used in parsing.
- iata: The IATA code of the heliport.
- pad_id: The ID of the helipad (similar to a runway ID).
- cont_rec_no: The continuation record number, used in parsing.
- limit_alt: The speed limit altitude.
- datum_code: The reference system used in surveying.
- is_ifr: An IFR capability marker.
- lat: The heliport reference point latitude.
- lon: The heliport reference point longitude.
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
- pad_dimensions: The dimensions of the helipad.
- mag_true: A marker for magnetic or true heading usage.
- heliport_name: The name of the heliport.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
