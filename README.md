# MW Business Solutions

Static website for MW Workflow, presenting custom business software and project case studies.

## Local preview

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000. No dependencies are required.

## Check and build

```sh
python scripts/check_site.py
python scripts/build_site.py
```

The build produces `dist/` and `website-upload.zip`, containing only public pages and their referenced assets.

## Cloudflare Pages

- Production branch: `main`
- Framework preset: None
- Build command: `python scripts/check_site.py && python scripts/build_site.py`
- Build output directory: `dist`

Deploy the generated output, not the repository root.
