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
