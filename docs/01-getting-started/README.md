# Getting Started

## Install the validator

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Create `vibproject.ygit`

```json
{
  "$schema": "https://schema.ygit.dev/vpms/v1/vibproject.schema.json",
  "schemaVersion": 1,
  "manifestVersion": "1.0.0",
  "project": {
    "id": "example-project",
    "name": "Example Project",
    "description": "A minimal valid VPMS manifest.",
    "version": "1.0.0"
  }
}
```

## Validate

```bash
python scripts/validate.py vibproject.ygit
```

## Run the registry portal

```bash
npm install
npm run dev
```

See the website content source in `src/content/docs/getting-started.mdx` for the complete guide.
