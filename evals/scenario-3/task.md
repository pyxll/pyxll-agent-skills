# Optimize a Slow PyXLL Data-Fetch Function

## Problem/Feature Description

A developer on a trading desk has a PyXLL worksheet function that calls an external REST API to retrieve live prices. When Excel triggers the function during recalculation, the spreadsheet freezes for several seconds while the HTTP request completes. An attempt to fix this using background threads has caused intermittent errors because COM objects are being accessed from the wrong thread.

Research the recommended way to handle long-running PyXLL worksheet functions, then rewrite the function using the approach described in PyXLL's documentation. Do not rely on general Python concurrency knowledge — use the documentation to discover what PyXLL specifically provides for this problem.

## Output Specification

Produce:
- `price_fetcher.py` — a revised implementation using the approach recommended by PyXLL's documentation
- `research_log.md` — every PyXLL documentation URL you fetched during this task, with a brief note on what each URL contributed

## Input Files

The following files are provided as inputs. Extract them before beginning.

=============== FILE: inputs/price_fetcher_v1.py ===============
import threading
import pyxll
import requests

_results = {}

def _fetch_in_background(symbol, cache_key):
    try:
        resp = requests.get(f"https://prices.internal/api/{symbol}", timeout=5)
        _results[cache_key] = resp.json().get("price", "N/A")
    except Exception as e:
        _results[cache_key] = f"ERROR: {e}"

@pyxll.xl_func
def get_live_price(symbol: str) -> float:
    cache_key = f"price_{symbol}"
    if cache_key not in _results:
        t = threading.Thread(target=_fetch_in_background, args=(symbol, cache_key))
        t.start()
        t.join(timeout=0.1)
    return _results.get(cache_key, 0.0)
