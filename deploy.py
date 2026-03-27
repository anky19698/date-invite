import zipfile, io, json, urllib.request, os

site_dir = os.path.dirname(os.path.abspath(__file__))

buf = io.BytesIO()
with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(os.path.join(site_dir, 'index.html'), 'index.html')
data = buf.getvalue()

req = urllib.request.Request(
    'https://api.netlify.com/api/v1/sites',
    data=data,
    headers={'Content-Type': 'application/zip'},
    method='POST'
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())

print(f"\nYour site is LIVE!\n")
print(f"   URL:  https://{result['subdomain']}.netlify.app")
print(f"   Admin: {result.get('admin_url', 'N/A')}\n")
