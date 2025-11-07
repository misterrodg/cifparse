# cifparse

cifparse is a parser for the Coded Instrument Flight Procedures file, released 
every 28 days by the FAA. It allows pilots, dispatchers, and others interested 
in flight data to quickly parse the file into Python dictionaries or a SQLite 
database for use in other programs. For example, the parsed data can then be 
used to draw maps of the flight paths, individual named points, or airspace.

If you are interested in the mapping aspect, have a look at 
[FacilityMapper](https://github.com/misterrodg/FacilityMapper).

## Versions

| Version | Description                                                         | Release Date |
| ------- | ------------------------------------------------------------------- | ------------ |
| 2.0.9   | Bugfix for missing `vert_angle` in `procedure_points` records.      | 2025-11-07   |
| 2.0.8   | Bugfix for incorrect lat/lon parse in `controlled_points` records.  | 2025-10-23   |
| 2.0.7   | Bugfix for incorrect time scale in `dist_time` field.               | 2025-08-20   |
| 2.0.6   | Bugfix for missing `time` field in `procedure_points`.              | 2025-08-20   |
| 2.0.5   | Section parsing fixes.                                              | 2025-06-21   |
| 2.0.4   | Field parsing fixes.                                                | 2025-06-18   |
| 2.0.3   | NDB Parsing bugfix.                                                 | 2025-06-18   |
| 2.0.2   | Build bugfix.                                                       | 2025-05-25   |
| 2.0.1   | Minor fixes to internal module handling.                            | 2025-05-25   |
| 2.0.0   | Major update. See [MIGRATION.md](./MIGRATION.md) for details.       | 2025-05-22   |
| 1.0.1   | Minor fixes to SQL statements.                                      | 2025-04-24   |
| 1.0.0   | Updated table handling to include additional detail and data types. | 2024-12-11   |
| 0.9.3   | Updated procedure handling (breaking changes) and database support. | 2024-11-15   |
| 0.9.2   | Minor fixes.                                                        | 2024-07-13   |
| 0.9.0   | Initial public release.                                             | 2024-07-13   |

A changelog is available in the [CHANGELOG.md](./CHANGELOG.md) with additional detail and guidance.

## Installation

Install using `pip`:

```
pip install cifparse
```

## Usage

Usage is relatively straightforward. Setting the path to the file can be somewhat finnicky, as it will only accept relative paths. To keep things simple, place the CIFP file in your project directory. Otherwise, if you want to go up several folders into a download folder, it might end up looking like `../../../../Downloads/FAACIFP18`.

Given the amount of data, parsing can take a moment. If dumping the data to a file, that can also add time. Dumping every airport to JSON can take around 15 seconds, and the resulting file is about 330MB.

### Examples

Start by importing `cifparse`, setting the path to the CIFP file, and then parsing the data.

```python
import cifparse

# Initialize the parser:
from cifparse import CIFP

# Set the relative path to where you have the CIFP file:
c = CIFP("FAACIFP18")

# Parse the data in the file:
c.parse()
# ...or parse only a specific subset by using any combination of the following:
c.parse_moras()
c.parse_vhf_navaids()
c.parse_ndb_navaids()
c.parse_enroute_waypoints()
c.parse_airway_markers()
c.parse_holds()
c.parse_airway_points()
c.parse_preferred_routes()
c.parse_airway_restrictions()
c.parse_enroute_comms()
c.parse_heliports()
c.parse_heli_terminal_waypoints()
c.parse_heli_procedures()
c.parse_heli_taas()
c.parse_heli_msas()
c.parse_heli_terminal_comms()
c.parse_airports()
c.parse_gates()
c.parse_terminal_waypoints()
c.parse_procedures()
c.parse_runways()
c.parse_loc_gss()
c.parse_company_routes()
c.parse_alternate_records()
c.parse_taas()
c.parse_mlss()
c.parse_terminal_markers()
c.parse_path_points()
c.parse_flight_plannings()
c.parse_msas()
c.parse_glss()
c.parse_terminal_comms()
c.parse_cruise_tables()
c.parse_reference_tables()
c.parse_controlled()
c.parse_fir_uir()
c.parse_restrictive()
```

#### Working with Entire Segments

After parsing the data, the results will be in the CIFP object, accessible via getters that return lists of the objects.

```python
all_moras = c.get_moras()
all_vhf_navaids = c.get_vhf_navaids()
all_ndb_navaids = c.get_ndb_navaids()
all_enroute_waypoints = c.get_enroute_waypoints()
all_airway_markers = c.get_airway_markers()
all_holds = c.get_holds()
all_airway_points = c.get_airway_points()
all_preferred_routes = c.get_preferred_routes()
all_airway_restrictions = c.get_airway_restrictions()
all_enroute_comms = c.get_enroute_comms()
all_heliports = c.get_heliports()
all_heli_terminal_waypoints = c.get_heli_terminal_waypoints()
all_heli_procedures = c.get_heli_procedures()
all_heli_taas = c.get_heli_taas()
all_heli_msas = c.get_heli_msas()
all_heli_terminal_comms = c.get_heli_terminal_comms()
all_airports = c.get_airports()
all_gates = c.get_gates()
all_terminal_waypoints = c.get_terminal_waypoints()
all_procedures = c.get_procedures()
all_runways = c.get_runways()
all_loc_gss = c.get_loc_gss()
all_company_routes = c.get_company_routes()
all_alternate_records = c.get_alternate_records()
all_taas = c.get_taas()
all_mlss = c.get_mlss()
all_terminal_markers = c.get_terminal_markers()
all_path_points = c.get_path_points()
all_flight_plannings = c.get_flight_plannings()
all_msas = c.get_msas()
all_terminal_comms = c.get_terminal_comms()
all_fir_uir = c.get_fir_uir()
all_cruise_tables = c.get_cruise_tables()
all_reference_tables = c.get_reference_tables()
all_controlled = c.get_controlled()
all_restrictive = c.get_restrictive()
```

#### Exporting Data

##### Dictionaries

Each object has its own `to_dict()` method. This is useful when you need to dump the data to json:

```python
from cifparse import CIFP
import json

c = CIFP("FAACIFP18")
c.parse_airports()
airports = c.get_airports()
airport_dicts = [item.to_dict() for item in airports]
with open("output.json", "w") as json_file:
    json.dump(airport_dicts, json_file, indent=2)
```

##### Database

Each object has its own `to_db()` method. This is useful when you would like the data to persist, or query it using standard database methods:

```python
c = CIFP("FAACIFP18")
c.parse()
c.to_db("FAACIFP18.db")
```

NOTE: The resulting tables are somewhat less-optimally normalized than they could be. This is mostly to allow flexibility in querying. For example, the `airway_points` table can be queried directly to retrieve all points on the airways, or a summary can be found on `airways` in a way similar to using `SELECT DISTINCT ...` on a subset of fields. Airspace follows a similar principle.

### CIFP Objects

A breakdown of the different objects can be found in the [Docs](./docs/) directory.
