"""Build a CA bundle that Python can use on this machine.

Norton Web/Mail Shield intercepts HTTPS and re-signs certificates with its own
root CA. Python's certifi bundle doesn't trust that root, so every request dies
with CERTIFICATE_VERIFY_FAILED. This appends Norton's root to a copy of certifi.

Re-run after upgrading certifi:  pipenv run python make_ca_bundle.py
"""

import pathlib
import shutil

import certifi

EXTRA_CERTS = [
    pathlib.Path(r"C:\ProgramData\Norton\Antivirus\wscert.pem"),
]

out = pathlib.Path(__file__).parent / "certs" / "ca-bundle.pem"
out.parent.mkdir(exist_ok=True)
shutil.copyfile(certifi.where(), out)

added = []
with out.open("a", encoding="utf-8") as bundle:
    for cert in EXTRA_CERTS:
        if not cert.exists():
            continue
        bundle.write("\n" + cert.read_text(encoding="utf-8").strip() + "\n")
        added.append(cert.name)

print(f"wrote {out}")
print(f"base: certifi at {certifi.where()}")
print(f"appended: {', '.join(added) if added else 'nothing (no extra CAs found)'}")
