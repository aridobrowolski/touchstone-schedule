#!/usr/bin/env python3
"""Swap the active app icon between the stored variants in ./icons.

Usage:
    python swap-icon.py night
    python swap-icon.py sunset

Copies icons/<name>-512.png and icons/<name>-180.png over the active
icon-512.png / icon-180.png. No dependencies (standard library only).

After running: commit & push, then delete and re-add the app to your
iPhone home screen so iOS picks up the new icon.
"""
import sys, os, glob, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = os.path.join(HERE, "icons")

def variants():
    return sorted(os.path.basename(p)[:-len("-512.png")]
                  for p in glob.glob(os.path.join(ICONS, "*-512.png")))

def main():
    choices = variants()
    if len(sys.argv) != 2 or sys.argv[1] not in choices:
        print("Available icons:", ", ".join(choices))
        print("Usage: python swap-icon.py <name>")
        sys.exit(1)
    name = sys.argv[1]
    for size in (512, 180):
        shutil.copyfile(os.path.join(ICONS, f"{name}-{size}.png"),
                        os.path.join(HERE, f"icon-{size}.png"))
    print(f"Active icon set to '{name}'.")
    print(f"Next: git add -A && git commit -m \"Use {name} icon\" && git push")

if __name__ == "__main__":
    main()
