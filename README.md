# MW Business Solutions

A dependency-free static website presenting bespoke, locally running business tools.

## Run locally

From this folder, run:

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000. No package installation or build step is needed.

## Checks

```powershell
python scripts/check_site.py
node --check js/main.js
git diff --check
```

The Python check verifies local links, fragment targets, page landmarks, duplicate IDs/attributes and screenshot dimensions. Browser review is also needed after layout or interaction changes.

## Pages

- `index.html`: services, featured rota project, value-based pricing, free testing/trial and contact.
- `products.html`: Solutions overview.
- `rota-case-study.html`: workflow, historical findings, screenshots and local/offline explanation.
- `invoice-reader.html`: explicitly marked Coming soon.

Shared styling is in `css/styles.css`. `js/main.js` progressively enhances screenshot links with a native dialog, full-size zoom, keyboard dismissal and focus restoration. Without JavaScript the links open the original image. All fonts, styles, scripts and images are local; there are no third-party scripts, analytics or remote font requests.

## Content and publishing

### Cloudflare Pages setup

Run `python scripts/check_site.py` followed by `python scripts/build_site.py`.
The publishing script creates `dist/` and `website-upload.zip` containing only the four public pages and their referenced assets. Private letters, working documents, unused images and repository files are excluded. Generated output and `deliverables/` are ignored by Git.

For Cloudflare Pages Git integration, select this repository and the `main` branch, use no framework preset, set the build command to `python scripts/check_site.py && python scripts/build_site.py`, and set the build output directory to `dist`. Alternatively, upload `website-upload.zip` using Pages Direct Upload. The intended custom domain is `mwworkflow.co.uk`, registered with Namecheap; configure both the root and `www` domains after deployment. Do not deploy the repository root.

Contact links use `michalwypych98@gmail.com` and open the visitor's email application; there is no contact-form backend. No messages are sent by the site itself.

The owner confirmed that the tool was built for a retail chain with 5–6 locations. The supplied letter draft records three historical comparisons from one branch: 213.5 → 207 hours, 195 → 186 hours and 217 → 206 hours. These total 26.5 fewer scheduled hours, averaging 8.833 hours per week. At the letter's assumed £12.70 hourly rate this is £112.18 per week, rounded conservatively to “around £110” throughout the site and revised letter. This replaces the earlier £111 headline with a consistent, disclosed calculation. These are potential savings from less overstaffing while meeting configured requirements, not claims of realised payroll savings or chain-wide results. Actual cash savings depend on pay arrangements and implementation. Original screenshots have been preserved.

The supplied letter also confirms successful installation/testing on the branch's work laptop. The owner confirms 1–4 week generation and weekend fairness balancing. Processing controls are labelled “Cores” and “Max time (s)” in the existing Solve screenshot. Hardware suitability is checked during initial testing; the site makes no universal speed guarantee.

`deliverables/` contains the private recipient-specific letter and document QA material. It is not linked from the public website and must not be included in the public deployment. Deploy only the HTML pages and their asset folders listed below.

The pricing section reflects the owner's offer: free preliminary testing, a free trial, and an agreed price based on demonstrable time or money savings. It does not invent a fixed fee, trial length or savings percentage.

Publish the four HTML pages and the `assets`, `css` and `js` folders to a static host. Keep their relative paths intact. This work has not deployed or changed any live website. The letter retains the supplied www.mwworkflow.co.uk address; domain-specific hosting settings have not been changed. Stylesheet/script version query strings should be updated when changing these assets on a caching host.
