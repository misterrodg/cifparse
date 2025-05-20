# The Enroute Communication Object

The Enroute Communication object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- fir_rdo_id: The ID of the associated FIR.
- fir_uir_addr: The communication address of the FIR/UIR.
- fir_uir_ind: An FIR (F), UIR (U), or combined (B) identifier.
- remote_site_name: The remote site name.
- comm_type: The associated type of communication.
- comm_freq: The associated frequency.
- gt: An guard (G) versus transmit (T) identifier.
- freq_unit: The frequency unit ID.
- cont_rec_no: An identifier for additional available data.
- serv_ind: An identifier for the services provided on the frequency.
- radar: A boolean for if the frequency is associated with a radar facility.
- modulation: The modulation type ID.
- sig_em: The signal emission type ID.
- lat: The latitude of the transmitter.
- lon: The longitude of the transmitter.
- mag_var: The magnetic variation.
- fac_elev: The elevation of the transmitter.
- h24_ind: A boolean value to note that the frequency is available 24 hours in a day.
- alt_desc: The altitude descriptor.
- alt_1: The minimum altitude.
- fl_1: A boolean value to note that `alt_1` is a Flight Level.
- alt_2: The second minimum altitude.
- fl_2: A boolean value to note that `alt_2` is a Flight Level.
- remote_fac: The facility used as an RCO, if defined.
- remote_region: The region of the facility used as an RCO, if defined.
- remote_sec_code: The sec_code of the facility used as an RCO, if defined.
- remote_sub_code: The sub_code of the facility used as an RCO, if defined.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
