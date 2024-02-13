# -----------------------------------------------------------------------------
# REQUIRED VALUES
# -----------------------------------------------------------------------------
# Environment choices: {DEV, TEST, PROD}
ENVIRONMENT = 'DEV'

# Name of machine running the application
ALLOWED_HOSTS = ['mike-1049650.com', 'localhost']

# Debug mode (probably only true in DEV)
DEBUG = True

# GMAIL PASSWORD
EMAIL_HOST_PASSWORD = 'sqrsmtcobscocvjz'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '375760887503-u4smspn7t0eo97g5r1i8tgpnmm75c3vb.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    #     "apple": {
    #         "APP": {
    #             # Your service identifier.
    #             "client_id": "your.service.id",
    #
    #             # The Key ID (visible in the "View Key Details" page).
    #             "secret": "KEYID",
    #
    #             # Member ID/App ID Prefix -- you can find it below your name
    #             # at the top right corner of the page, or it’s your App ID
    #             # Prefix in your App ID.
    #             "key": "MEMAPPIDPREFIX",
    #
    #             # The certificate you downloaded when generating the key.
    #             "certificate_key": """-----BEGIN PRIVATE KEY-----
    # s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr
    # 3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3
    # c3ts3cr3t
    # -----END PRIVATE KEY-----
    # """
    #         }
    #     }

}


# -----------------------------------------------------------------------------
# OPTIONAL VALUES
# -----------------------------------------------------------------------------

# You may want to disable elevated developer access while running locally
# ELEVATE_DEVELOPER_ACCESS = False

# You may want to extend session expiration during local development
# SESSION_COOKIE_AGE = 4 * 60 * 60  # 4 hours


# python manage.py createsuperuser --username=mjg --email=mikegostomski@gmail.com
