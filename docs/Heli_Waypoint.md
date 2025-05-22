# The Heli Waypoint Object

NOTE: The Heli Waypoint object is used in for both Terminal and Enroute waypoints.

The Heli Waypoint object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- heliport: The associated heliport.
- heliport_region: The region of the heliport.
- heliport_sub_code: The sub code of the heliport.
- waypoint_id: The ICAO code of the waypoint.
- waypoint_region: The region of the waypoint.
- cont_rec_no: An identifier for additional available data.
- type: The waypoint type. \*
- usage: The use type (e.g. high, low, or both).\*
- lat: The waypoint latitude.
- lon: The waypoint longitude.
- mag_var: The magnetic variation.
- elevation: The elevation of the waypoint.
- datum_code: The reference system used in surveying.
- name_indicator: The name indicator of the waypoint.\*
- name_description: The description of the name.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.

\* Column-based field. May contain intentional leading or trailing spaces.
