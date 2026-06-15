# Live Market Data Ribbon Controls

## Problem Description

A portfolio management team wants a PyXLL ribbon to control live market data in
their Excel workbook. The "Market Data" tab should contain:

1. A **toggle button** to enable or disable live streaming (the button must reflect
   its current on/off state — the ribbon should show whether streaming is active)
2. A **dropdown** to select the data provider: Bloomberg, Reuters, or Internal
3. A **"Refresh Now" button** to force an immediate data pull

When the user switches data provider, the ribbon controls should be refreshed to
reflect any state changes (e.g. some providers may affect which other controls are
enabled).

## Output Specification

Produce two files:

- `portfolio_ribbon.xml` — complete ribbon XML for the Market Data tab
- `portfolio_ribbon.py` — Python module with full callback implementations for all
  controls. Stub out any business logic with `pass` or a print statement, but
  implement the function signatures correctly and include the mechanism for
  refreshing ribbon controls after a provider change.
