# Interior Duct Ltd — QR Code Generator

This repository contains a simple, client-side QR code generator tailored for Interior Duct Ltd. It runs entirely in the browser and doesn't send data to external servers.

Files:
- `index.html` — main app (single-file web app)
- `assets/kitchen_cabinet_logo.svg` — company logo used in header and as embedded logo option
- `assets/furniture-bg.svg` — placeholder background used on mobile view

Features:
- Single URL QR generation with optional embedded logo
- Batch generation: paste multiple label,URL lines and generate a grid of QR codes
- Download single PNGs or download all as a ZIP (client-side)
- Responsive layout; mobile view includes furniture background

How to use locally:
1. Open `index.html` in a browser (double-click or use `Live Server` extension).
2. Enter a URL and click "Generate QR Code".
3. Use the Batch section to paste multiple lines for bulk generation.

Deploy to GitHub Pages (quick):
1. Create a new repository on GitHub and push these files.
2. In the repository settings, enable GitHub Pages from the `main` branch and root folder.
3. After publishing, the site will be available at `https://<your-user>.github.io/<repo-name>/`.

Notes:
- The QR generation uses `qrcodejs` (client-side). ZIP creation uses `JSZip` and `FileSaver.js` via CDN.
- If you want custom high-resolution logos, replace `assets/kitchen_cabinet_logo.svg` with your logo file.

Next steps I can take for you:
- Replace the placeholder SVG logo with your provided PNG or vector file
- Tweak visual design and export DPI for print-quality QR codes
- Add campaign tracking metadata & a small local CSV export for records

