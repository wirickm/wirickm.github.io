# Sydney Travel Map

An interactive map of Sydney highlights and New Year's Eve (NYE) activities, with each location's distance from Sydney Airport (SYD). Built with [Folium](https://python-visualization.github.io/folium/).

**Live map:** <https://wirickm.github.io/sydney_map_consolidated.html>

## Files

- `sydney_map_consolidated.py` - generator script (locations and markers live here)
- `sydney_map_consolidated.html` - rendered map, served by GitHub Pages

## Regenerate the map

```
pip install -r requirements.txt
python sydney_map_consolidated.py
```

Commit the updated HTML. Pushing to the default branch deploys it via `.github/workflows/static.yml`.

This repo replaces the old `SydneyTravelPlanning` repo.

## Retiring the old SydneyTravelPlanning repo

The map used to also live in `wirickm/SydneyTravelPlanning`. That repo is now just a pointer here and can be removed.

**What gets deleted:** only `wirickm/SydneyTravelPlanning` (its README, history, issues and PRs). Nothing in this repo or the live map is affected.

**How (repo owner only):**

1. Open <https://github.com/wirickm/SydneyTravelPlanning/settings>
2. Scroll to **Danger Zone** at the bottom.
3. Pick one:
   - **Archive this repository** - read-only, reversible. Safer choice.
   - **Delete this repository** - permanent. Type `wirickm/SydneyTravelPlanning` to confirm.
