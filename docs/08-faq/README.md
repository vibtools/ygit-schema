# Frequently Asked Questions

## Is `.ygit` JSON?

Yes. VPMS uses JSON syntax and the `.ygit` extension.

## Are unknown fields allowed?

No. Version 1 rejects unsupported properties at the root and in defined nested objects.

## Can a manifest contain secrets?

No. Use environment variables or a secret manager.

## How do I validate everything?

```bash
python scripts/validate.py --all
```

## How is production deployed?

Cloudflare Pages Git integration builds `main`. GitHub Actions performs quality checks but does not deploy production.
