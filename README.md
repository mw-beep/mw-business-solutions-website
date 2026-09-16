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

Contact links use `michalwypych98@gmail.com` and open the visitor's email application; there is no contact-form backend. No messages are sent by the site itself.

The £111 average and lower-cost results are retained from the original case study. The owner confirmed that the tool was built for a retail chain with 5–6 locations and historically tested against one branch's rotas, with savings calculated from fewer paid labour hours. These are historical comparisons, not claims of realised savings across the chain. The underlying test data and exact sample size are not included in this website repository. Original screenshots have been preserved; they illustrate the workflow and outputs rather than providing a downloadable application.

The pricing section reflects the owner's offer: free preliminary testing, a free trial, and an agreed price based on demonstrable time or money savings. It does not invent a fixed fee, trial length or savings percentage.

Publish the four HTML pages and the `assets`, `css` and `js` folders to a static host. Keep their relative paths intact. This work has not deployed or changed any live website. A public domain has not been supplied, so no canonical URL or domain-specific sitemap is generated. Stylesheet/script version query strings should be updated when changing these assets on a caching host.
