# Vietnam Stock Market Pipeline (archived)

**Status:** stopped on 2026-11-11. Kept as a record of the exploration work.

## What this was
A daily data pipeline: Vietnamese stock data (vnstock API) → BigQuery → Looker Studio.

## What I completed
- Project setup: GCP project, BigQuery access, repo structure, decision log
- Explored the ticker listing, daily prices (OHLCV) and intraday trades (`notebooks/explore.ipynb`)
- Built a paging loop to fetch a full day of trades, including days with few or no trades
- Reconciled trades against daily volume and traced a 100-share gap to a single
  wrong record in the provider's data (`notebooks/trades_reconciliation.ipynb`)

## Why I stopped
- vnstock v5 stopped authenticating on 2026-11-10, with a forced upgrade to v6.
- v6 removed the data sources this project used (VCI and KBS).
- Every remaining source needs a personal API key from a Vietnamese brokerage account.

A pipeline that must run every day needs a source that stays stable, so I moved on.

## What I took from it
- Save raw data before analysing it, and never overwrite a saved file
- Check one source against another before trusting either
- Pin versions, and expect an upstream provider to change without warning
- Record decisions and their reasons as you go (`docs/decision_log.md`)

## Project structure
```
vietnam-stock-market-pipeline/
├── data/                           # Local landing zone for raw API extracts (git-ignored)
├── docs/                           # Decision log, data exploration notes, data dict, architecture diagram
├── notebooks/                      # Exploring the API. Experiments only
│   └── ...
├── src/                            # Get data from the API and load it into BigQuery
│   └── ...
├── .env.example                    # Template showing which settings are needed
├── .gitignore                      # Ignore secrets/unnecessary files
├── README.md                       
└── requirements.txt                # Python packages with pinned versions
```
