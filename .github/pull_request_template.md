## Summary

Describe the exact change and its approved scope.

## Verification

- [ ] `python scripts/audit.py`
- [ ] `python scripts/validate.py --all`
- [ ] `python -m unittest discover -s test -p "test_*.py"`
- [ ] `npm run format:check`
- [ ] `npm run check`
- [ ] `npm run build`

## Consistency

- [ ] Architecture and existing behavior are preserved.
- [ ] Schema, examples, fixtures, and documentation remain synchronized.
- [ ] `CHANGELOG.md` is updated when user-visible behavior changes.
- [ ] No secrets, generated caches, or local artifacts are included.
