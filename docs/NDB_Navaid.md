# NDB Navaid

The NDB Navaid object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- airport_id: The ICAO ID of the associated airport.
- airport_region: The ICAO region of the associated airport.
- ndb_id: The ID of the VHF navaid.
- ndb_region: The ICAO region of the VHF navaid.
- frequency: The frequency.
- cont_rec_no: An identifier for additional available data.
- nav_class: The class of NDB.\*
- lat: The latitude of the NDB.
- lon: The longitude of the NDB.
- mag_var: The magnetic variation.
- datum_code: The reference system used in surveying.
- ndb_name: The name of the NDB.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.

\* Column-based field. May contain intentional leading or trailing spaces.
