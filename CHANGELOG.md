## Changelog

### [2.0.1] - 2025-05-25

- Minor fixes to internal module handling.

### [2.0.0] - 2025-05-22

- Major update to parsing, record recognition, and record types. See [MIGRATION.md](./MIGRATION.md) for details.

### [1.0.1] - 2025-04-24

- Minor fixes to SQL statements.

### [1.0.0] - 2024-12-11

#### Added

- Added `validity` table to easily verify the validity period for the data in the database.

#### Changed

- Fixed the lack of foreign key references on the `controlled_airspace_segments` and `restrictive_airspace_segments` tables.
- Added detail to the `controlled_airspace_segments` and `restrictive_airspace_segments` to make querying the segment altitudes easier.

### [0.9.3] - 2024-11-25

#### Added

- Support for sqlite.

#### Changed

- All procedure parts are on the same level. This was done to handle certain procedures that are only transitions, without a core segment. In addition, it keeps all of the subsections on the same level of nesting. Access the `core` segment in the same way as you would a `runway_transition`.
- The generic `transition` has been renamed `enroute_transition` to distinguish it from other types.

#### Removed

- "Top level" `core` section of procedures. This has been relocated as a segment of type `core`, accessed in the same way as `runway_transition` and `enroute_transition`.

### [0.9.2] - 2024-07-13

- Minor fixes.

### [0.9.0] - 2024-07-13

- Initial public release.
