# VPMS Version 1 Schema Reference

The official schema is `v1/vibproject.schema.json` and is published at:

```text
https://schema.ygit.dev/vpms/v1/vibproject.schema.json
```

## Required root properties

| Property | Type | Constraint |
| --- | --- | --- |
| `$schema` | String | Canonical Version 1 schema URI |
| `schemaVersion` | Integer | Must equal `1` |
| `manifestVersion` | String | Version 1 semantic version |
| `project` | Object | Project identity and version |

## Required project properties

- `id`
- `name`
- `description`
- `version`

All supported root and nested properties are defined explicitly. Unknown properties are rejected with `additionalProperties: false`.

The complete property table is maintained in `src/data/schema-list.json` and rendered at `/schemas/vibproject/`.
