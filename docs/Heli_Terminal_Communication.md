# Heli Terminal Communication

The Heli Terminal Communication object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- heliport_id: The ICAO ID of the associated heliport.
- heliport_region: The ICAO region of the associated heliport.
- sub_code: The subsection code, used in parsing.
- comm_type: The associated type of communication.
- comm_freq: The associated frequency.
- gt: An guard (G) versus transmit (T) identifier.
- freq_unit: The frequency unit ID.
- cont_rec_no: An identifier for additional available data.
- serv_ind: An identifier for the services provided on the frequency.\*
- radar: A boolean for if the frequency is associated with a radar facility.
- modulation: The modulation type ID.
- sig_em: The signal emission type ID.
- lat: The latitude of the transmitter.
- lon: The longitude of the transmitter.
- mag_var: The magnetic variation in signed notation (+ values for East, - for West).
- fac_elev: The elevation of the transmitter.
- h24_ind: A boolean value to note that the frequency is available 24 hours in a day.
- sector: The sector definition, if defined.
- alt_desc: The altitude descriptor.
- fl_1: A boolean value to note that `alt_1` is a Flight Level.
- alt_1: The minimum altitude.
- fl_2: A boolean value to note that `alt_2` is a Flight Level.
- alt_2: The second minimum altitude.
- sector_fac: The associated facility for sectors, if defined.
- sector_region: The region of the associated facility for sectors, if defined.
- sector_sec_code: The sec_code of the associated facility for sectors, if defined.
- sector_sub_code: The sub_code associated facility for sectors, if defined.
- dist_desc: A distance descriptor.
- comm_dis: The distance the frequency is available to or beyond.
- remote_fac: The facility used as an RCO, if defined.
- remote_region: The region of the facility used as an RCO, if defined.
- remote_sec_code: The sec_code of the facility used as an RCO, if defined.
- remote_sub_code: The sub_code of the facility used as an RCO, if defined.
- callsign: The callsign.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.

\* Column-based field. May contain intentional leading or trailing spaces.
