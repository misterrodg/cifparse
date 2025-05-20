# The FIR/UIR Object

The FIR/UIR object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- fir_uir_id: The ID of the FIR/UIR.
- fir_uir_addr: The communication address of the FIR/UIR.
- fir_uir_ind: An FIR (F), UIR (U), or combined (B) identifier.
- seq_no: The sequence number of the FIR/UIR record.
- cont_rec_no: An identifier for additional available data.
- adj_fir_id: An `fir_uir_id` for the adjacent FIR at this segment.
- adj_uir_id: An `fir_uir_id` for the adjacent UIR at this segment.
- rus: The reporting unit speed.
- rua: The reporting unit altitude.
- entry: The entry requirement.
- boundary_via: The boundary definition.
- fir_uir_lat: The latitude of the boundary point.
- fir_uir_lon: The longitude of the boundary point.
- arc_lat: The latitude of the arc point, if the boundary is defined by an arc.
- arc_lon: The longitude of the arc point, if the boundary is defined by an arc.
- arc_dist: The radius of the arc.
- arc_bearing: The starting bearing of the arc.
- fir_upper_limit: The upper altitude limit of the FIR.
- uir_lower_limit: The lower altitude limit of the UIR.
- uir_upper_limit: The upper altitude limit of the UIR.
- cruise_id: The ID of the associated cruise table.
- fir_uir_name: The FIR/UIR name.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
