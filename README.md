# Touchstone Schedule

A combined live class schedule for all 17 Touchstone Climbing gyms, in one mobile web app.

- **Live data** — pulls straight from Touchstone's public booking portal API (`portal.touchstoneclimbing.com/graphql-public`), no server required.
- **Filter by gym** — toggle any of the 17 gyms on/off, grouped by region.
- **Filter by program** — Intro Classes, Climbing Clinics, Yoga, Fitness, Affinity Groups, Youth Programs, Gym Events.
- **Book in one tap** — every class links to its exact booking page on the Touchstone portal.
- **Installable** — open in Safari on iPhone → Share → *Add to Home Screen* for a full-screen app.

Filters persist on your device (localStorage). Gym program lists refresh every 24h; schedules refresh on every view.

## App icon

The active icon lives at `icon-512.png` / `icon-180.png`. Both artwork variants are stored in [`icons/`](icons/):

- **night** — El Capitan under a starry sky (currently active)
- **sunset** — El Capitan at golden-hour dusk

To switch, run the swap script, then commit, push, and re-add the app to your home screen:

```
python swap-icon.py sunset      # or: night
git add -A && git commit -m "Use sunset icon" && git push
```

Each variant has a full-resolution master (`icons/<name>-1024.png`) plus pre-rendered `-512`/`-180` sizes. To add a new variant, drop a cleaned square `icons/<name>-1024.png` in and re-render the two sizes.
