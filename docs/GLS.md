# The GLS Object

The GLS object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- fac_id: The facility ID.
- fac_region: The ICAO region (e.g. `K6` for NE US) of the facility.
- sub_code: The subsection code, used in parsing.
- gls_ref_id: The ID of the reference path.
- gls_cat: The category of the GLS.
- cont_rec_no: An identifier for additional available data.
- gls_channel: The GLS channel.
- runway_id: The associated runway ID.
- gls_bearing: The bearing of the GLS.
- true: A boolean value to note that `gls_bearing` is true rather than magnetic.
- station_lat: The GLS station latitude.
- station_lon: The GLS station longitude.
- gls_id: The GLS ID.
- svc_vol: The service volume.
- tdma_slots: The TDMA slots.
- min_elev_angle: The minimum elevation angle.
- mag_var: The magnetic variation.
- station_elev: The elevation of the GLS station.
- datum_code: The datum code.
- station_type: The station type.
- wgs84_elev: The WGS84 elevation.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
