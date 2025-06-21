# Migration from 1.x to 2.0

Version 2.0 is a lot more database-focused. All of the `find_` functions have been removed, as they provide little utility versus being able to properly query the data in a database.

The update to 2.0 streamlines the code, provides closer access to the individual objects, improves the parsing and adds parsing for all of the objects available within the CIFP standard. Depending on what the FAA includes in the specific cycle of data, these may or may not be used.

## Modifications

### General

All database methods have been internalized. Just specify a file path when using the `cifp.to_db()` method. No need to manually connect and create a cursor to pass in.

```python
c = CIFP("FAACIFP18")
c.parse()
c.to_db("FAACIFP18.db")
```

### Hierarchy

Version 1.x used an implicit hierarchy for the various objects. This meant that parsing the CIFP for Runway or Localizer records required parsing all of the Airport objects. This isn't necessary and added complexity. Now, all objects are independent and at the top level.

### General Table Modifications

Many fields removed from the tables have been moved to other tables, as the original parser would have never added data to them. Waypoints are now split between Enroute and Terminal Waypoints. Additionally, Terminal Waypoints and Procedures have dedicated `heli_` tables for helicopter-specific points and procedures. Specific changes to existing tables is in [Detail](#detail). New tables are available at the bottom of the page in [New Tables](#new-tables).

### General Field Modifications

Altitude- and heading-related fields now have additional boolean fields as modifiers. This had been irregularly applied in version 1, where airway points had everything in `altitude` fields, whereas procedure points had the data split into `altitude` and `flight_level` fields, depending on if the value was an altitude or flight level.

For altitudes, the altitude value will always be found in a field with `alt` in the name. If that value is a flight level, a `1` will be found in the associated `fl` field. For example, `min_alt_1` will contain the minimum altitude value. If the `min_fl_1` field is `0` or `NULL`, the value is an altitude. If it is `1`, it is a flight level.

Similarly, certain heading fields may be provided in true versus magnetic. If a heading is meant to be true, an associated `true` field will be populated with a `1`. Otherwise, it will be `0` or `NULL`.

Certain fields are now column-based. This means that some will have intentional leading and or trailing spaces. For example, on a VHF Navaid record, if the record is for a low DME with no voice capability, it will be listed as `DLW` (with a leading and trailing space). These fields are marked in the documentation for each type with an asterisk.

## Detail

### Airport

**Table Name**

- _No changes_

**Fields**

- Added: `st`
- Changed: `region` -> `airport_region`, `limit` -> `speed_limit`
- Removed: _No changes_

### Airway

**Table Name**

- _No changes_

**Fields**

- Added: `st`
- Changed: _No changes_
- Removed: `application`, `notes`

### Airway Points

**Table Name**

- _No changes_

**Fields**

- Added: `st`, `cont_rec_no`, `min_fl_1`, `min_fl_2`, `max_fl`
- Changed: `sequence_number` -> `seq_no`, `description_code` -> `desc_code`, `min_alt` -> `min_alt_1`
- Removed: `application`, `notes`, `sig_point`

NOTE: `sig_point` was a duplicate of the data available in `desc_code`.

### Controlled Airspace

**Table Name**

- `controlled_airspace` -> `controlleds`

**Fields**
airspace_class, airspace_name

- Added: `st`, `center_region`, `airspace_name`
- Changed: _No changes_
- Removed: `application`, `time_code`, `notam`, `time_ind`, `op_time_1`, `op_time_2`, `op_time_3`, `op_time_4`, `op_time_5`, `op_time_6`, `op_time_7`, `controlling_agency`

### Controlled Airspace Segment

**Table Name**

- `controlled_airspace_segments` -> `controlled_segments`

**Fields**

- Added: `st`, `area`, `sec_code`, `sub_code`, `center_region`, `airspace_type`, `center_sec_code`, `center_sub_code`, `airspace_class`
- Changed: `multiple_code` -> `mult_code`
- Removed: _No changes_

### Controlled Airspace Point

**Table Name**

- `controlled_airspace_points` -> `controlled_points`

**Fields**

- Added: `st`, `cont_rec_no`
- Changed: `region` -> `center_region`, `multiple_code` -> `mult_code`, `sequence_number` -> `seq_no`
- Removed: _No changes_

### Heliports

**Table Name**

- _No changes_

**Fields**

- Added: `st`
- Changed: `region` -> `heliport_region`, `limit` -> `speed_limit`
- Removed: _No changes_

### Localizers

**Table Name**

- `loc_gs` -> `loc_gss`

**Fields**

- Added: `st`, `cont_rec_no`, `true`
- Changed: _No changes_
- Removed: `application`, `notes`

### NDB Navaid

**Table Name**

- Changed: `ndbs` -> `ndb_navaids`

**Fields**

- Added: `st`, `cont_rec_no`
- Changed: `name` -> `ndb_name`
- Removed: `application`, `notes`

### Procedures

**Table Name**

- _No changes_

**Fields**

- Added: `st`, `fac_id`, `fac_region`, `fac_sub_code`
- Changed: _No changes_
- Removed: _No changes_

### Procedure Points

**Table Name**

- _No changes_

**Fields**

- Added: `st`, `cont_rec_no`, `time`
- Changed: `sequence_number` -> `seq_no`, `description_code` -> `desc_code`, `dist` -> `dist_time`, `altitude` -> `alt_1`, `flight_level` -> `fl_1`, `altitude_2` -> `alt_2`, `flight_level_2` -> `fl_2`, `multiple_code` -> `mult_code`, `speed_limit_2` -> `speed_desc`
- Removed: _No changes_

### Restrictive Airspace

**Table Name**

- `restrictive_airspace` -> `restrictives`

**Fields**

- Added: `st`
- Changed: `restrictive_designation` -> `restrictive_id`
- Removed: `application`, `time_ind`, `op_time_1`, `op_time_2`, `op_time_3`, `op_time_4`, `op_time_5`, `op_time_6`, `op_time_7`, `controlling_agency`

### Restrictive Airspace Segment

**Table Name**

- `restrictive_airspace_segments` -> `restrictive_segments`

**Fields**

- Added: `st`, `area`, `sec_code`, `sub_code`, `region`, `restrictive_type`
- Changed: `restrictive_designation` -> `restrictive_id`, `multiple_code` -> `mult_code`
- Removed: _No changes_

### Restrictive Airspace Point

**Table Name**

- `restrictive_airspace_points` -> `restrictive_points`

**Fields**

- Added: `st`, `cont_rec_no`
- Changed: `restrictive_designation` -> `restrictive_id`, `multiple_code` -> `mult_code`, `sequence_number` -> `seq_no`
- Removed: _No changes_

### Runways

**Table Name**

- _No changes_

**Fields**

- Added: `st`, `cont_rec_no`
- Changed: `ls_ident` -> `ls_ident_1`, `cat` -> `cat_1`
- Removed: _No changes_

### VHF Navaid

**Table Name**

- Changed: `vhf_dmes` -> `vhf_navaids`

**Fields**

- Added: `st`, `cont_rec_no`
- Changed: `name` -> `vhf_name`
- Removed: `application`, `notes`

### Waypoint

**Table Name**

- Added: `terminal_waypoints`
- Changed: `waypoints` now only contains enroute waypoints.

Both tables share the same field names and types.

**Fields**

- Added: `st`, `cont_rec_no`
- Changed: `region` -> `environment_region`, `name` -> `name_indicator`
- Removed: `application`, `notes`

## New Tables

| Object                       | Table Name                |
| ---------------------------- | ------------------------- |
| Airport Gate                 | `airport_gates`           |
| Airway Marker                | `airway_markers`          |
| Alternate Record             | `alternate_records`       |
| Company Route                | `company_route`           |
| Cruise Table                 | `cruise_tables`           |
| Enroute Communications       | `enroute_comms`           |
| FIR/UIR                      | `fir_uirs`                |
| Flight Planning              | `flight_plannings`        |
| GLS                          | `glss`                    |
| Heli MSA                     | `heli_msas`               |
| Heli Procedure               | `heli_procedures`         |
| Heli Procedure Segment       | `heli_procedure_segments` |
| Heli Procedure Point         | `heli_procedure_points`   |
| Heli TAA                     | `heli_taas`               |
| Heli Terminal Communications | `heli_terminal_comms`     |
| Heli Terminal Waypoint       | `heli_terminal_waypoints` |
| Hold                         | `holds`                   |
| MLS                          | `mlss`                    |
| MORA                         | `moras`                   |
| MSA                          | `msas`                    |
| Path Point                   | `path_points`             |
| Preferred Route              | `preferred_routes`        |
| Procedure Segment            | `procedure_segments`      |
| Reference Table              | `reference_tables`        |
| Restriction Altitude         | `restriction_altitudes`   |
| Restriction Closure          | `restriction_closures`    |
| Restriction Cruise           | `restriction_cruises`     |
| Restriction Note             | `restriction_notes`       |
| TAA                          | `taas`                    |
| Terminal Communications      | `terminal_comms`          |
| Terminal Marker              | `terminal_markers`        |
| Terminal Waypoint            | `terminal_waypoints`      |
