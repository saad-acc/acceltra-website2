/**
 * Acceltra Cookie Consent Manager
 * GDPR-compliant cookie consent management
 */

(function() {
    'use strict';

    // Configuration
    const STORAGE_KEY = 'acceltra_cookie_consent';
    const CONSENT_EXPIRY_DAYS = 365; // Consent expires after 1 year

    // Cookie Consent Manager
    const CookieConsent = {
        /**
         * Initialize cookie consent on page load
         */
        init: function() {
            // Check if consent banner exists
            const banner = document.getElementById('flowappz-cookie-consent');
            if (!banner) {
                return; // Banner not found, exit
            }

            // Check if user has already given consent
            const consent = this.getConsent();
            
            if (consent) {
                // User has consented, hide banner
                this.hideBanner();
                // Load scripts based on consent
                this.loadScripts(consent);
            } else {
                // Show banner and attach event listeners
                this.showBanner();
                this.attachEventListeners();
            }
        },

        /**
         * Get consent from localStorage
         * @returns {Object|null} Consent object or null
         */
        getConsent: function() {
            try {
                const stored = localStorage.getItem(STORAGE_KEY);
                if (!stored) {
                    return null;
                }

                const consent = JSON.parse(stored);
                
                // Check if consent has expired
                if (consent.timestamp) {
                    const consentDate = new Date(consent.timestamp);
                    const expiryDate = new Date(consentDate);
                    expiryDate.setDate(expiryDate.getDate() + CONSENT_EXPIRY_DAYS);
                    
                    if (new Date() > expiryDate) {
                        // Consent expired, remove it
                        localStorage.removeItem(STORAGE_KEY);
                        return null;
                    }
                }

                return consent;
            } catch (e) {
                console.error('Error reading consent:', e);
                return null;
            }
        },

        /**
         * Save consent to localStorage
         * @param {Object} consent - Consent preferences object
         */
        saveConsent: function(consent) {
            try {
                consent.timestamp = new Date().toISOString();
                localStorage.setItem(STORAGE_KEY, JSON.stringify(consent));
            } catch (e) {
                console.error('Error saving consent:', e);
            }
        },

        /**
         * Check if user has consented to a specific category
         * @param {string} category - Cookie category ('essential', 'analytics', 'marketing')
         * @returns {boolean}
         */
        hasConsent: function(category) {
            const consent = this.getConsent();
            if (!consent) {
                return category === 'essential'; // Essential cookies always allowed
            }
            
            // Essential cookies are always true
            if (category === 'essential') {
                return true;
            }

            return consent[category] === true;
        },

        /**
         * Show consent banner
         */
        showBanner: function() {
            const banner = document.getElementById('flowappz-cookie-consent');
            if (banner) {
                banner.style.display = 'block';
                // Add animation class if needed
                banner.classList.add('cookie-consent-visible');
            }
        },

        /**
         * Hide consent banner
         */
        hideBanner: function() {
            const banner = document.getElementById('flowappz-cookie-consent');
            if (banner) {
                banner.style.display = 'none';
                banner.classList.remove('cookie-consent-visible');
            }
        },

        /**
         * Accept all cookies
         */
        acceptAll: function() {
            const consent = {
                essential: true,
                analytics: true,
                marketing: true
            };
            
            this.saveConsent(consent);
            this.hideBanner();
            this.loadScripts(consent);
            
            // Dispatch custom event for other scripts to listen
            this.dispatchConsentEvent('accepted', consent);
        },

        /**
         * Reject all non-essential cookies
         */
        rejectAll: function() {
            const consent = {
                essential: true,
                analytics: false,
                marketing: false
            };
            
            this.saveConsent(consent);
            this.hideBanner();
            this.loadScripts(consent);
            
            // Dispatch custom event for other scripts to listen
            this.dispatchConsentEvent('rejected', consent);
        },

        /**
         * Attach event listeners to Accept/Reject buttons
         */
        attachEventListeners: function() {
            const acceptBtn = document.getElementById('flowappz-cookie-consent-approve');
            const rejectBtn = document.getElementById('flowappz-cookie-consent-reject');

            if (acceptBtn) {
                acceptBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    CookieConsent.acceptAll();
                });
            }

            if (rejectBtn) {
                rejectBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    CookieConsent.rejectAll();
                });
            }
        },

        /**
         * Load scripts based on consent
         * @param {Object} consent - Consent preferences
         */
        loadScripts: function(consent) {
            // Analytics scripts (e.g., Google Analytics)
            if (consent.analytics) {
                // Load analytics scripts here
                // Example: this.loadGoogleAnalytics();
            }

            // Marketing scripts (e.g., Facebook Pixel, LinkedIn Insight)
            if (consent.marketing) {
                // Load marketing scripts here
                // Example: this.loadMarketingPixels();
            }
        },

        /**
         * Dispatch custom consent event
         * @param {string} action - 'accepted' or 'rejected'
         * @param {Object} consent - Consent preferences
         */
        dispatchConsentEvent: function(action, consent) {
            const event = new CustomEvent('cookieConsent', {
                detail: {
                    action: action,
                    consent: consent
                }
            });
            window.dispatchEvent(event);
        },

        /**
         * Reset consent (for testing or user preference changes)
         */
        resetConsent: function() {
            localStorage.removeItem(STORAGE_KEY);
            // Reload page to show banner again
            window.location.reload();
        }
    };

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            CookieConsent.init();
        });
    } else {
        // DOM already loaded
        CookieConsent.init();
    }

    // Expose CookieConsent to window for external access
    window.CookieConsent = CookieConsent;

})();
