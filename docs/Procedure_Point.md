# The Procedure Object

The Procedure object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- fac_id: The ID of the associated facility (airport or heliport ID).
- fac_region: The ICAO region of the associated facility.
- fac_sub_code: The subsection code of the associated facility.
- procedure_id: The ID (or computer code) of the procedure.
- route_type: The route type (e.g. SID, STAR, IAP)
- transition_id: The ID (or computer code) of the associated transition.
- seq_no: The sequence number of the point in the procedure.
- fix_id: The ICAO code of the fix.
- fix_region: The ICAO region of the fix.
- fix_sec_code: The section code of the fix.
- fix_sub_code: The subsection code of the fix.
- cont_rec_no: An identifier for additional available data.
- desc_code: The description code, used in parsing.\*
- turn_direction: The direction of the turn.
- rnp: The RNP requirement for the leg.
- path_term: The path termination.
- tdv: Turn direction valid marker, used in conjunction with `turn_direction`.
- rec_vhf: The recommended/associated navaid.
- rec_vhf_region: The region of the recommended/associated navaid.
- arc_radius: The arc radius for RTF legs.
- theta: The magnetic bearing to the `fix_id` from the `rec_vhf`.
- rho: The distance to the `fix_id` from the `rec_vhf`.
- course: The course.
- dist_time: The distance or time of the leg.
- time: A boolean value to note that `dist_time` is a time.
- rec_vhf_sec_code: The section code of the recommended/associated navaid.
- rec_vhf_sub_code: The subsection code of the recommended/associated navaid.
- alt_desc: The altitude descriptor.
- atc: An ATC override marker.
- alt_1: The altitude for the leg.
- fl_1: The flight level for the leg.
- alt_2: The second altitude for the leg.
- fl_2: The second flight level for the leg.
- trans_alt: The transition altitude.
- speed_limit_1: The speed limit.
- vert_angle: The vertical angle.
- center_fix: The center fix for an RTF leg.
- mult_code: The multiple code, used in parsing.
- center_fix_region: The center fix region.
- center_fix_sec_code: The center fix section code.
- center_fix_sub_code: The center fix subsection code.
- gns_fms_id: The GNS/FMS ID.
- speed_limit_2: The second speed limit.
- rte_qual_1: The route qualifier (specifies requirements).
- rte_qual_2: The second route qualifier (denotes approach types).
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.

\* Column-based field. May contain intentional leading or trailing spaces.
