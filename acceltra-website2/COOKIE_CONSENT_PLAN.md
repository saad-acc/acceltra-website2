# Cookie Consent Implementation Plan

## Overview
This document outlines the plan to re-implement cookie consent functionality for the Acceltra website, ensuring GDPR compliance while maintaining a lightweight, user-friendly solution.

## Current State

### ✅ What Already Exists
1. **CSS Styling** (`css/webflow.shared.css`):
   - `.flowappz-cookie-consent` - Main banner container (fixed position, bottom-right)
   - `.cookie-heading` - Heading styles
   - `.cookie-description` - Description text styles
   - `.cookie-buttons-group` - Button container with flex layout
   - `.accept-button` - Accept button (blue background)
   - `.reject-button` - Reject button (white background)

2. **HTML Structure** (exists in some pages):
   ```html
   <div id="flowappz-cookie-consent" class="flowappz-cookie-consent text-size-tiny">
     <h5 class="cookie-heading">Cookies</h5>
     <p class="cookie-description">We use cookies to improve user experience...</p>
     <div class="cookie-buttons-group">
       <button id="flowappz-cookie-consent-approve" class="accept-button">Accept all</button>
       <button id="flowappz-cookie-consent-reject" class="reject-button">Reject all</button>
     </div>
   </div>
   ```

### ❌ What's Missing
1. **JavaScript Functionality**: No script to handle consent logic
2. **Consent Storage**: No mechanism to store user preferences
3. **Cookie Categories**: No granular control (essential, analytics, marketing)
4. **Integration**: No integration with analytics scripts (for future Google Analytics)
5. **Consistency**: HTML structure missing from some pages
6. **Privacy Policy**: No dedicated cookie policy section

---

## Implementation Plan

### Phase 1: Core JavaScript Implementation

#### 1.1 Create Cookie Consent Manager (`js/cookie-consent.js`)

**Features:**
- Check if consent has been given (using localStorage)
- Show/hide consent banner based on consent status
- Handle Accept/Reject button clicks
- Store consent preferences in localStorage
- Support for cookie categories (essential, analytics, marketing)
- GDPR-compliant (no cookies set before consent)

**Storage Structure:**
```javascript
{
  consent: {
    essential: true,      // Always true (required for site functionality)
    analytics: false,     // User choice
    marketing: false,     // User choice
    timestamp: "2025-01-XX" // When consent was given
  }
}
```

**Key Functions:**
- `initCookieConsent()` - Initialize on page load
- `showConsentBanner()` - Display banner if no consent
- `hideConsentBanner()` - Hide banner after consent
- `acceptAll()` - Accept all cookie categories
- `rejectAll()` - Reject non-essential cookies
- `hasConsent(category)` - Check if user consented to category
- `setConsent(categories)` - Store consent preferences

#### 1.2 Cookie Categories

**Essential Cookies** (Always enabled):
- Session management
- Security
- Load balancing
- Cannot be disabled

**Analytics Cookies** (Optional):
- Google Analytics (when implemented)
- Website usage statistics
- Performance monitoring

**Marketing Cookies** (Optional):
- Social media tracking
- Advertising pixels
- Retargeting (if implemented)

---

### Phase 2: HTML Integration

#### 2.1 Add Consent Banner to All Pages

**Pages to Update:**
- `index.html`
- `404.html`
- `impressum.html`
- `tos.html`
- `privacy.html`
- `services/*.html` (10 pages)
- `solutions/*.html` (3 pages)

**Placement:**
- Before closing `</body>` tag
- After footer, before scripts
- Consistent structure across all pages

#### 2.2 Enhanced HTML Structure (Optional - for future granular control)

```html
<div id="flowappz-cookie-consent" class="flowappz-cookie-consent text-size-tiny" style="display: none;">
  <h5 class="cookie-heading">Cookies</h5>
  <p class="cookie-description">
    We use cookies to improve user experience. Choose what cookies you allow us to use. 
    You can read more about our Cookie Policy in our <a href="privacy.html">privacy policy</a>.
  </p>
  <div class="cookie-buttons-group">
    <button id="flowappz-cookie-consent-approve" class="accept-button">Accept all</button>
    <button id="flowappz-cookie-consent-reject" class="reject-button">Reject all</button>
    <!-- Future: Add "Customize" button for granular control -->
  </div>
</div>
```

---

### Phase 3: Privacy Policy Updates

#### 3.1 Add Cookie Policy Section to `privacy.html`

**New Section: "Cookies and Tracking Technologies"**

**Content to Include:**
- What cookies are
- Types of cookies used (Essential, Analytics, Marketing)
- Purpose of each cookie category
- How to manage cookie preferences
- Third-party cookies (if any)
- Cookie retention periods
- How to withdraw consent

**Example Structure:**
```html
<h3>Cookies and Tracking Technologies</h3>
<h4>What are Cookies?</h4>
<p>Cookies are small text files stored on your device...</p>

<h4>Types of Cookies We Use</h4>
<h5>Essential Cookies</h5>
<p>These cookies are necessary for the website to function...</p>

<h5>Analytics Cookies</h5>
<p>These cookies help us understand how visitors interact...</p>

<h5>Marketing Cookies</h5>
<p>These cookies are used to deliver relevant advertisements...</p>

<h4>Managing Your Cookie Preferences</h4>
<p>You can manage your cookie preferences at any time...</p>
```

---

### Phase 4: Analytics Integration (Future)

#### 4.1 Google Analytics Integration

**Conditional Loading:**
- Only load Google Analytics script if user consented to "analytics" cookies
- Use `hasConsent('analytics')` check before initializing GA

**Implementation Pattern:**
```javascript
if (hasConsent('analytics')) {
  // Load Google Analytics script
  // Initialize tracking
}
```

#### 4.2 Other Third-Party Scripts

- Social media widgets (LinkedIn, etc.)
- Marketing pixels
- All non-essential scripts should respect consent

---

### Phase 5: Enhanced Features (Optional - Future)

#### 5.1 Granular Cookie Control

**Customize Button:**
- Allow users to select individual cookie categories
- Expandable section with checkboxes
- Save preferences button

#### 5.2 Consent Management Page

**Dedicated Page:**
- `/cookie-preferences.html` or section in privacy policy
- Allow users to change preferences anytime
- Show current consent status
- Easy-to-use toggle switches

#### 5.3 Consent Logging

**For Compliance:**
- Log consent decisions (timestamp, choice)
- Store in localStorage or send to backend (if available)
- Useful for GDPR compliance audits

---

## Technical Implementation Details

### File Structure
```
js/
  └── cookie-consent.js    # Main consent manager script

css/
  └── webflow.shared.css   # Existing styles (already present)

All HTML files:
  └── Include consent banner HTML
  └── Include cookie-consent.js script
```

### Script Loading Order
1. jQuery (if needed for other functionality)
2. `cookie-consent.js` (should load early, before analytics)
3. Other site scripts
4. Analytics scripts (conditionally loaded based on consent)

### localStorage Keys
- `acceltra_cookie_consent` - Stores consent preferences
- Format: JSON string with consent object

### Banner Display Logic
- Show banner if `localStorage.getItem('acceltra_cookie_consent')` is null
- Hide banner if consent exists
- Banner should appear on first visit only
- User can change preferences later (via privacy policy link)

---

## GDPR Compliance Checklist

- [x] **Consent Before Cookies**: No non-essential cookies set before consent
- [x] **Clear Information**: Banner explains what cookies are used for
- [x] **Easy Opt-Out**: Reject button clearly visible
- [x] **Granular Control**: Support for different cookie categories
- [x] **Withdraw Consent**: Users can change preferences anytime
- [x] **Privacy Policy**: Cookie information documented
- [x] **No Pre-ticked Boxes**: User must actively consent
- [x] **Consent Storage**: Preferences stored locally

---

## Implementation Steps

### Step 1: Create JavaScript File
1. Create `js/cookie-consent.js`
2. Implement core consent management functions
3. Add event listeners for Accept/Reject buttons
4. Test localStorage functionality

### Step 2: Add HTML to All Pages
1. Add consent banner HTML to all 18 pages
2. Ensure consistent structure
3. Add script tag to load `cookie-consent.js`
4. Verify banner appears on pages without consent

### Step 3: Update Privacy Policy
1. Add "Cookies and Tracking Technologies" section
2. Document all cookie types
3. Explain how to manage preferences
4. Link to privacy policy from consent banner

### Step 4: Testing
1. Test consent banner display/hide
2. Test Accept/Reject functionality
3. Test localStorage persistence
4. Test across different browsers
5. Test on mobile devices
6. Verify banner doesn't reappear after consent

### Step 5: Future Analytics Integration
1. When Google Analytics is added, integrate with consent system
2. Only load GA if analytics consent is given
3. Test conditional loading

---

## Browser Compatibility

**Target Browsers:**
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

**Required Features:**
- localStorage support (all modern browsers)
- ES6 JavaScript (use Babel if needed for older browsers)
- CSS Flexbox (already used in existing styles)

---

## Performance Considerations

- **Lightweight**: Keep script under 5KB minified
- **No Dependencies**: Avoid external libraries if possible
- **Lazy Loading**: Don't block page rendering
- **Minimal DOM Manipulation**: Efficient show/hide logic

---

## Accessibility

- **ARIA Labels**: Add proper ARIA attributes to banner
- **Keyboard Navigation**: Ensure buttons are keyboard accessible
- **Screen Readers**: Banner should be announced properly
- **Focus Management**: Focus should be managed when banner appears

**Example ARIA:**
```html
<div id="flowappz-cookie-consent" 
     class="flowappz-cookie-consent text-size-tiny" 
     role="dialog" 
     aria-labelledby="cookie-heading"
     aria-describedby="cookie-description">
  <h5 id="cookie-heading" class="cookie-heading">Cookies</h5>
  ...
</div>
```

---

## Testing Checklist

- [ ] Banner appears on first visit
- [ ] Banner doesn't appear after consent is given
- [ ] Accept button stores consent correctly
- [ ] Reject button stores consent correctly
- [ ] Consent persists across page navigations
- [ ] Consent persists after browser restart
- [ ] Privacy policy link works correctly
- [ ] Banner is responsive on mobile
- [ ] Banner doesn't overlap with content
- [ ] Buttons are clickable and responsive
- [ ] Works in all target browsers
- [ ] No console errors
- [ ] localStorage is used correctly

---

## Future Enhancements

1. **Cookie Preferences Page**: Dedicated page for managing preferences
2. **Granular Control**: Individual toggles for each cookie category
3. **Consent Analytics**: Track consent acceptance rates
4. **Multi-language Support**: Translate banner text
5. **Cookie List**: Display all cookies used on the site
6. **Auto-expiry**: Consent expires after X months (if required by law)
7. **Backend Integration**: Sync consent with backend (if available)

---

## Resources

- **GDPR Cookie Consent Guidelines**: https://gdpr.eu/cookies/
- **ICO Cookie Guidance**: https://ico.org.uk/for-organisations/guide-to-pecr/guidance-on-the-use-of-cookies-and-similar-technologies/
- **Web.dev Cookie Best Practices**: https://web.dev/cookie-best-practices/

---

## Notes

- The existing CSS styling is already well-designed and matches the site's aesthetic
- The HTML structure exists in some pages but needs to be added consistently
- The implementation should be lightweight and not impact site performance
- Consider adding a "Cookie Preferences" link in the footer for easy access
- The consent banner should be non-intrusive but clearly visible

---

## Estimated Implementation Time

- **Phase 1 (JavaScript)**: 2-3 hours
- **Phase 2 (HTML Integration)**: 1-2 hours
- **Phase 3 (Privacy Policy)**: 1 hour
- **Phase 4 (Testing)**: 1-2 hours
- **Total**: 5-8 hours

---

## Next Steps

1. Review and approve this plan
2. Create `js/cookie-consent.js` with core functionality
3. Add HTML banner to all pages
4. Update privacy policy
5. Test thoroughly
6. Deploy to GitHub Pages
