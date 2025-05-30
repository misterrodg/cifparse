# Flight Planning

The Flight Planning object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- airport_id: The ICAO ID of the associated airport.
- airport_region: The ICAO region of the associated airport.
- sub_code: The subsection code, used in parsing.
- procedure_id: The ID (or computer code) of the procedure.
- procedure_type: The procedure type (e.g. SID, STAR, IAP)
- runway_transition_id: The ID of the runway transition.
- runway_transition_point: The ID of the point of the runway transition.
- runway_transition_region: The region of the point of the runway transition.
- runway_transition_sec_code: The section code of the point of the runway transition.
- runway_transition_sub_code: The subsection code of the point of the runway transition.
- runway_transition_atd: The ATD of the point of the runway transition.
- common_point: The ID of the point of the common point.
- common_point_region: The region of the point of the common point.
- common_point_sec_code: The section code of the point of the common point.
- common_point_sub_code: The subsection code of the point of the common point.
- common_point_atd: The ATD of the point of the common point.
- enroute_transition_id: The ID of the enroute transition.
- enroute_transition_point: The ID of the point of the enroute transition.
- enroute_transition_region: The region of the point of the enroute
- enroute_transition_sec_code: The section code of the point of the enroute transition.
- enroute_transition_sub_code: The subsection code of the point of the enroute transition.
- enroute_transition_atd: The ATD of the point of the enroute transition.
- seq_no: The sequence number of the point in the procedure.
- cont_rec_no: An identifier for additional available data.
- noe: An identifier for the number of engines.
- turbo: An identifier for turboprop/jet only.
- rnav: A boolean for RNAV only.
- atc_wc: The weight class.
- atc_id: The ATC ID (official procedure name).
- time_zone: The time zone.
- description: The textual description.
- ltc: The leg type code.
- rpt: The reporting code.
- out_mag_crs: The outbound magnetic course.
- alt_desc: The altitude descriptor.
- alt_1: The minimum altitude.
- fl_1: A boolean value to note that `alt_1` is a Flight Level.
- alt_2: The second minimum altitude.
- fl_2: A boolean value to note that `alt_2` is a Flight Level.
- speed_limit: The speed limit.
- cruise_id: The ID of the associated cruise table.
- speed_desc: The speed descriptor.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
