# Airway Point

The Airway Point object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- airway_id: The ID of the airway.
- six_char: A six character ID if one exists.
- seq_no: The sequence number of the point in the airway.
- point_id: The ID of the point along the airway.
- point_region: The region of the point.
- point_sec_code: The section code of the point.
- point_sub_code: The subsection of the point.
- cont_rec_no: An identifier for additional available data.
- desc_code: The description code, used in parsing.\*
- bound_code: The code of the boundary being crossed.
- route_type: The airway type.
- level: The level of the airway (high, low, or both).
- direct: A one-way restriction in relation to the sequence numbers (forward or backward). Blank if none.
- cruise_id: The cruise table indicator.
- eu_ind: The EU indicator.
- rec_vhf: The ID of the recommended navaid.
- rec_vhf_region: The ICAO region of the recommended navaid.
- rnp: The RNP value.
- theta: The magnetic bearing to the `point_id` from the `rec_vhf`.
- rho: The distance to the `point_id` from the `rec_vhf`.
- out_true: A boolean value to note that `out_mag_crs` is true rather than magnetic.
- out_mag_crs: The outbound magnetic course.
- time: A boolean value to note that `from_dist` is time rather than distance.
- from_dist: The distance from this point to the next.
- in_true: A boolean value to note that `in_mag_crs` is true rather than magnetic.
- in_mag_crs: The inbound magnetic course.
- min_fl_1: A boolean value to note that `min_alt_1` is a Flight Level.
- min_alt_1: The minimum altitude.
- min_fl_2: A boolean value to note that `min_alt_2` is a Flight Level.
- min_alt_2: The second minimum altitude.
- max_fl: A boolean value to note that `max_alt` is a Flight Level.
- max_alt: The maximum altitude.
- fix_radius: The fixed radius transition value.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.

\* Column-based field. May contain intentional leading or trailing spaces.
