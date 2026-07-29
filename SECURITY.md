# Security Policy

## Supported versions

Security fixes are applied to the current stable VPMS major version and the current `main` branch.

| Version | Supported |
| --- | --- |
| VPMS 1.x | Yes |
| Unreleased future versions | No production support |

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability, exposed credential, malicious manifest, dependency compromise, or deployment weakness.

Use the repository's **Security** tab to create a private security advisory. Include:

- Affected file, version, or commit.
- Reproduction steps or a minimal proof of concept.
- Expected security boundary and observed impact.
- Suggested mitigation when available.

Remove real credentials, private manifests, personal data, and production secrets from evidence. Maintainers will acknowledge a complete report, assess severity, coordinate a fix, and publish disclosure details after remediation.

## Security boundaries

YGit Schema validates manifest structure. It does not execute manifest commands, access referenced files, authenticate external URLs, or guarantee that referenced software is safe. Consumers must treat manifest content as untrusted input and apply their own authorization, path, command, and network controls.
