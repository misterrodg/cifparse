# Runway

The Runway object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- airport_id: The ICAO ID of the associated airport.
- airport_region: The ICAO region of the associated airport.
- sub_code: The subsection code, used in parsing.
- runway_id: The ICAO code of the runway.
- cont_rec_no: An identifier for additional available data.
- length: The length of the runway.
- bearing: The bearing of the runway.
- true: A boolean value to note that `bearing` is true rather than magnetic.
- lat: The latitude of the threshold of the runway.
- lon: The longitude of the threshold of the runway.
- gradient: The gradient of the runway.
- ellipsoidal_height: The ellipsoidal height of the runway.
- threshold_elevation: The threshold elevation.
- displaced_threshold: The length of the displaced threshold, if any.
- tch: The threshold crossing height.
- width: The width of the runway.
- tch_id: The threshold crossing height ID (describes what path was used to determine the TCH).
- ls_ident_1: The associated landing system.
- cat_1: The category of the associated landing system.
- stopway: The stopway length, if any.
- ls_ident_2: The second associated landing system.
- cat_2: The category of the associated landing system.
- description: The runway description.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
