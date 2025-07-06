# Terminal Marker

The Terminal Marker object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- facility_id: The ICAO ID of the associated facility.
- facility_region: The ICAO region of the associated facility.
- sub_code: The subsection code, used in parsing.
- loc_id: The ID of the associated localizer.
- marker_type: The marker type.\*
- cont_rec_no: An identifier for additional available data.
- frequency: The frequency.
- runway_id: The ID of the associated runway.
- marker_lat: The latitude of the marker.
- marker_lon: The longitude of the marker.
- true_bearing: The true bearing of the marker.
- locator_lat: The latitude of the associated locator, if present.
- locator_lon: The longitude of the associated locator, if present.
- locator_class: The class of the associated locator, if present.\*
- locator_fac_char: The characteristics of the associated locator, if present.
- locator_id: The ID of the associated locator, if present.
- mag_var: The magnetic variation in signed notation (+ values for East, - for West).
- fac_elev: The elevation of the facility.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.

\* Column-based field. May contain intentional leading or trailing spaces.
