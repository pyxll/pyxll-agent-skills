# Runtime-Populated Pricing Model Menu

## Problem Description

A trading operations team uses a PyXLL Excel add-in. Quants regularly deploy new
pricing model Python modules to the server, so the list of available models changes
over time. Hard-coding a fixed ribbon menu would go stale within days.

The team lead wants a ribbon button that opens a menu populated at runtime: each
time a user clicks the arrow, Python is called to determine which models are currently
available and the menu is built on the fly. The ribbon module is `pricing_ribbon`.

## Output Specification

Produce two files:

- `pricing_ribbon.xml` — ribbon XML with a "Pricing" tab containing a menu button
  that is populated at runtime. The menu should refresh its contents each time it is
  opened (in case new models have been deployed since the last open).

- `pricing_ribbon.py` — Python module containing all callback functions referenced
  from the XML. For the demo implementation, return a menu with at least two example
  pricing model buttons (e.g. Black-Scholes and Monte Carlo). Each button's
  `onAction` should also be implemented as a stub function.
