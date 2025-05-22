# The Preferred Routes Object

The Preferred Routes object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- route_id: The ID of the route.
- use: The route use.
- seq_no: The sequence number of the point in the airspace.
- cont_rec_no: An identifier for additional available data.
- fix_id: The ICAO code of the fix.
- fix_region: The ICAO region of the fix.
- fix_sec_code: The section code of the fix.
- fix_sub_code: The subsection code of the fix.
- via: The path to the listed fix.
- path_id: The ID of the path.
- path_area: The areas of the path.
- level: The route level.
- route_type: The route type.
- int_point: The initial point.
- int_region: The region of initial point.
- int_sec_code: The section code of the initial point.
- int_sub_code: The subsection code of the initial point.
- term_point: The terminating point.
- term_region: The region of terminating point.
- term_sec_code: The section code of the terminating point.
- term_sub_code: The subsection code of the terminating point.
- min_alt: The minimum altitude.
- min_fl: A boolean value to note that `min_alt` is a Flight Level.
- max_alt: The second minimum altitude.
- max_fl: A boolean value to note that `max_alt` is a Flight Level.
- time_zone: The time zone.
- aircraft_use: The aircraft use group.\*
- direct: The direction restriction.
- alt_desc: The altitude descriptor.
- alt_1: The minimum altitude.
- fl_1: A boolean value to note that `alt_1` is a Flight Level.
- alt_2: The second minimum altitude.
- fl_2: A boolean value to note that `alt_2` is a Flight Level.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.

\* Column-based field. May contain intentional leading or trailing spaces.
