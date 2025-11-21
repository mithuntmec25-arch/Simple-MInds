from google_play_scraper import search

sus_keywords = [
    "mods","hacks","pro","unlock","vip","premium","free download",
    "get for free","no ads","adfree","modded","apk","cracked",
    "unlimited gems","unlimited coins","cheat","mod version",
    "patched","root","lucky patch","diamond","reward"
]

def extract_name(app_id):
    parts = app_id.split(".")
    if len(parts) >= 2:
        return parts[1] 
    return "developer"


def generate_impersonation_email(dev_name, app_title):
    subject = f"Report: Potential Impersonation / Fake App — {app_title}"

    body = f"""
Hi {dev_name.capitalize()} Team,

I'm reaching out to report a possible impersonation issue involving an app on Google Play.
The app appears to use misleading branding or keywords that may confuse users or imitate
your product.

Details:
• App Title: {app_title}
• Developer ID Extracted: {dev_name}
• Issue: Suspicious content / potential impersonation

Please review this app at your convenience.

Regards,
A concerned user
"""

    return subject, body

user_input = input("Enter the app name: ")
result = search(user_input, lang='en', country='us')

if not result:
    print("No apps found.")
    exit()

potential_fake_apps = []

print("\n--- SEARCH RESULTS ---\n")
for app in result:
    print("App Name:", app["title"])
    print("Package:", app["appId"])
    print("Rating:", app["score"])
    print("Icon URL:", app["icon"])
    print("--------------")

    title = app["title"]
    rating = app["score"]
    app_id = app["appId"]

    if rating is None:
        continue

    for keyword in sus_keywords:
        if keyword.lower() in title.lower() and rating < 4.0:
            potential_fake_apps.append(app)
            break


print("\n==============================")
print(" SUSPECTED FAKE / IMPERSONATION APPS ")
print("==============================\n")

if len(potential_fake_apps) == 0:
    print("No suspicious apps detected.")
    exit()


for fake in potential_fake_apps:
    title = fake["title"]
    app_id = fake["appId"]

    dev_name = extract_name(app_id)
    subject, body = generate_impersonation_email(dev_name, title)

    print("App Detected:", title)
    print("App ID:", app_id)
    print("--------------")
    print("EMAIL SUBJECT:")
    print(subject)
    print("\nEMAIL BODY:")
    print(body)
    print("--------------\n")
