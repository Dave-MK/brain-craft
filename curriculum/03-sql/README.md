# 03 — SQL

**Mission:** Manipulate Data (Mission 2)

## Capstone contribution

Grid and consumption data storage — the AI Energy OS needs a real relational store for historical demand, weather, price, and simulation data.

## Learning objectives

- Core querying: SELECT, WHERE, JOIN, GROUP BY, aggregate functions
- Schema design for time-series-heavy data (energy consumption, weather)
- Window functions (flagged early per the Architect's "prepare ahead" behavior — see [`docs/04-adaptive-learning/overview.md`](../../docs/04-adaptive-learning/overview.md), since these matter again later for forecasting features)
- Indexing and query performance basics

## Prerequisites

[`01-python`](../01-python/README.md)

## Leads into

[`04-apis`](../04-apis/README.md), [`05-pandas`](../05-pandas/README.md)

## Status

Complete. All 6 lessons authored and schema-validated in [`lessons/03-sql/`](../../lessons/03-sql/): SELECT & WHERE → JOIN → Aggregation → Schema Design → Window Functions → Indexing & Performance (boss battle). `sql.select-where` depends on `python.files-io`, tying Mission 2 back to Mission 1's ingestion work.
