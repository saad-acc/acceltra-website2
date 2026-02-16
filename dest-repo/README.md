# Acceltra Website

This repository contains the static website for Acceltra, ready to be hosted on GitHub Pages.

## Structure

```
.
├── index.html          # Main homepage
├── 404.html           # Custom 404 error page
├── impressum.html      # Imprint/Legal page
├── tos.html           # Terms of Service
├── privacy.html       # Privacy Policy
├── services/          # Service pages
│   ├── digital-strategy.html
│   ├── agile-transformation.html
│   ├── cloud.html
│   ├── devops-consulting.html
│   ├── sre-consulting.html
│   ├── cyber-security.html
│   ├── software-development.html
│   ├── data-science.html
│   ├── artificial-intelligence.html
│   └── technology-solutions.html
├── solutions/         # Solution pages
│   ├── bestmodal.html
│   ├── cargoflo.html
│   └── storylob.html
├── css/               # Stylesheets
├── js/                # JavaScript files
│   └── cookie-consent.js  # GDPR-compliant cookie consent manager
├── images/            # Image assets
├── fonts/             # Font files
└── .nojekyll          # GitHub Pages configuration
```

## Deployment to GitHub Pages

### Option 1: Automatic Deployment (Recommended)

1. Push this repository to GitHub
2. Go to your repository settings
3. Navigate to "Pages" in the left sidebar
4. Under "Source", select the branch (usually `main` or `master`)
5. Select the folder (usually `/ (root)`)
6. Click "Save"
7. Your site will be available at `https://saad-acc.github.io/acceltra-website/`

### Option 2: Using GitHub Actions

If you want to use GitHub Actions for deployment, you can set up a workflow file in `.github/workflows/deploy.yml`.

## Local Development

To view the website locally:

1. Clone this repository
2. Open `index.html` in a web browser, or
3. Use a local server:
   ```bash
   # Using Python 3
   python3 -m http.server 8000
   
   # Using Node.js (if you have http-server installed)
   npx http-server
   ```
4. Navigate to `http://localhost:8000` in your browser

## Notes

- All external URLs have been converted to relative paths for GitHub Pages compatibility
- All internal links have been updated to work with GitHub Pages structure
- Custom 404 error page created and styled to match the site design
- GDPR-compliant cookie consent system implemented on all pages
- The website uses Webflow-generated HTML/CSS/JS
- Images and assets are stored locally in the repository
- External fonts (Google Fonts) are loaded from CDN
- Webflow badge has been removed from all pages

## To-Do / Future Improvements

- [ ] **Form Handler:** Set up a form submission handler for the contact form (consider Formspree, Netlify Forms, or similar)
- [x] **Cookie Consent:** GDPR-compliant cookie consent system implemented ✅
  - Cookie consent banner on all pages
  - Accept/Reject functionality with localStorage persistence
  - Cookie policy section added to privacy policy
  - Ready for analytics integration (Google Analytics, etc.)
- [ ] **Blog Integration:** Add blog functionality (as mentioned, this will be handled separately)
- [ ] **SEO Optimization:** Add meta descriptions, Open Graph tags, and structured data
- [ ] **Performance:** Optimize images (compress, use WebP format where possible)
- [ ] **Analytics:** Add Google Analytics or similar tracking if needed
  - Note: Cookie consent system is ready - integrate using `CookieConsent.hasConsent('analytics')`
- [x] **404 Page:** Create a custom 404.html page for GitHub Pages ✅
- [ ] **Testing:** Test all internal links and navigation on GitHub Pages
- [ ] **Mobile Testing:** Verify responsive design works correctly on all devices
- [ ] **Accessibility:** Run accessibility audit and fix any issues

## Customization

- To update content, edit the HTML files directly
- To modify styles, edit files in the `css/` directory
- To change functionality, edit files in the `js/` directory
- Images can be replaced in the `images/` directory

## License

Copyright © Acceltra. All rights reserved.
