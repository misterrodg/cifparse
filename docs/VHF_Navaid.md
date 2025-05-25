# VHF Navaid

The VHF Navaid object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- airport_id: The ICAO ID of the associated airport.
- airport_region: The ICAO region of the associated airport.
- vhf_id: The ID of the VHF navaid.
- vhf_region: The ICAO region of the VHF navaid.
- frequency: The frequency.
- cont_rec_no: An identifier for additional available data.
- nav_class: The class of navaid.\*
- lat: The latitude of the navaid.
- lon: The longitude of the navaid.
- dme_id: The ID of the DME.
- dme_lat: The latitude of the DME.
- dme_lon: The longitude of the DME.
- mag_var: The magnetic variation.
- dme_elevation: The elevation of the DME.
- figure_of_merit: The figure of merit.
- dme_bias: The DME bias.
- frequency_protection: The frequency protection.
- datum_code: The reference system used in surveying.
- vhf_name: The name of the VHF navaid.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.

\* Column-based field. May contain intentional leading or trailing spaces.
