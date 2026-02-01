# Interior Duct Ltd — QR Code Generator

This repository contains a simple, client-side QR code generator tailored for Interior Duct Ltd. It runs entirely in the browser and doesn't send data to external servers.

Files:
- `index.html` — main QR generator app (single-file web app)
- `scan.html` — mobile view app that displays social media links when QR is scanned
- `assets/logo.jpg` — company logo used in header and as embedded logo option
- `assets/furniture-bg.svg` — responsive background used on mobile view

Features:
- **Single URL QR Generation** — Enter any URL and generate a QR code with optional embedded logo
- **Social Media Links Mode** — Add multiple social platforms (WhatsApp Business, Instagram, Facebook, etc.), then generate a single QR code that links to a branded mobile view page displaying all channels
- **Batch Generation** — Paste multiple label,URL lines and generate a grid of QR codes
- **Download Options** — Download single PNGs or download all as a ZIP (client-side)
- **Responsive Design** — Mobile-optimized with furniture background

How to use locally:
1. Open `index.html` in a browser (double-click or use `Live Server` extension).
2. **For single URL QR**: Enter a URL and click "Generate QR Code".
3. **For social media links**: 
   - Go to "Social Media Links Mode" section
   - Add each platform (WhatsApp, Instagram, etc.) with its URL
   - Click "Generate Social QR Code" to create a QR that links to `scan.html` with all links
4. Use the Batch section to paste multiple lines for bulk generation.

Social Media Links Mode Workflow:
- Users add social channels with their URLs (e.g., WhatsApp Business link, Instagram Channel)
- A single QR code is generated pointing to `scan.html?links=[encoded-json]`
- When the QR is scanned on mobile, it displays a branded page with all social channels as clickable cards
- The mobile view (`scan.html`) shows the Interior Duct Ltd logo, company description, and social media options

Deploy to GitHub Pages:
1. Create a new repository on GitHub and push these files.
2. Enable GitHub Pages in repository settings from the `main` branch and root folder.
3. After publishing, the site will be available at `https://<your-user>.github.io/<repo-name>/`.

The social media QR codes will link to:
- `https://<your-user>.github.io/<repo-name>/scan.html?links=[social-links-json]`

Dependencies:
- `qrcodejs` (CDN) — client-side QR code generation
- `JSZip` (CDN) — batch ZIP file creation
- `FileSaver.js` (CDN) — client-side file downloads

Notes:
- All QR generation and processing happens in the browser; no data is sent to external servers
- Social media links are encoded in the URL query parameter, visible but not transmitted to any third party
- The embedded logo on QR codes uses canvas composition for quality output

Next steps I can take for you:
- Customize the social media platform selection (add/remove channels)
- Adjust the styling of the mobile view (`scan.html`)
- Add analytics tracking within your own infrastructure
- Optimize QR code sizes for print quality


