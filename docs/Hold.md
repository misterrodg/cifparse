# Hold

The Hold object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- environment_id: The waypoint environment (e.g. `ENRT` for airway waypoints or an airport ID if associated with an airport).
- environment_region: The region of the environment.
- dup_ind: An indication that there are multiple holds for the given point.
- point_id: The ID of the hold point.
- point_region: The ICAO region of the hold point.
- point_sec_code: The section code of the hold point.
- point_sub_code: The subsection code of the hold point.
- cont_rec_no: An identifier for additional available data.
- in_course: The inbound course.
- turn_dir: The turn direction.
- leg_length: The length of the hold leg, if in nautical miles.
- leg_time: The length of the hold leg, if in minutes.
- min_alt: The minimum altitude for the hold.
- max_alt: The maximum altitude for the hold.
- hold_speed: The maximum speed for the hold.
- rnp: The RNP value.
- arc_radius: The arc radius for RNP holds.
- hold_name: The name of the hold.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
