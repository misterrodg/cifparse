# The Path Point Object

The Path Point object comprises the following fields:

- st: A standard (S) versus tailored (T) identifier.
- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- airport_id: The ICAO ID of the associated airport.
- airport_region: The ICAO region of the associated airport.
- sub_code: The subsection code, used in parsing.
- approach_id: The ID of the associated approach.
- surface_id: The ID of the runway or helipad.
- ops_type: The operation type.
- cont_rec_no: An identifier for additional available data.
- route_ind: A differentiator for multiple final approach segments.
- sbas_spi: The SBAS service provider ID.
- ref_path_data_sel: The path data selector.
- ref_path_data_id: The path data ID.
- app_pd: The type or category of the approach.
- ltp_lat: The LTP latitude.
- ltp_lon: The LTP longitude.
- ltp_ellipsoid_height: The LTP height using WGS84.
- gpa: The glide path angle.
- fpap_lat: The FPAP latitude.
- fpap_lon: The FPAP longitude.
- course_width: The course width at the LTP.
- length_offset: The distance between the runway and FPAP.
- path_point_tch: The threshold crossing height.
- tch_ind: The TCH height unit.
- hal: The horizontal alert limit.
- val: The vertical alert limit.
- crc: A data integrity check.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
