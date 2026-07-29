# Versioning

VPMS separates schema, manifest format, and project versions.

- `schemaVersion`: major schema generation; Version 1 uses integer `1`.
- `manifestVersion`: VPMS format release within major version 1, such as `1.0.0`.
- `project.version`: semantic version of the described project.

Breaking schema changes require a new major directory such as `v2/`. Version 1 remains available for existing consumers.
