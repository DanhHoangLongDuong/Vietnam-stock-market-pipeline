## 0. Setup
1. using vnstock for API \
Reason: free API for Vietnamese stock market. Daily refresh, 10M+ rows 
2. ADC for local gcloud sign in\
Reason: No service account key exists, nothing secret is inside the project folder.  
3. using .env\
Reason: Secrets and settings kept out of code
4. requirements.txt \
Reason: Easier for users to setup the project

## 1. Explore
5. Use `vci` instead of `kbs` \
Reason: when using `kbs`, `last_id` is ignored. Also `kbs` can only return 5,000 rows \
-> can not get a full day for busy tickers \
See: explore.ipynb, 1.3
6. Use parquet file instead of csv\
Reason: parquet file can keep columns datatype
7. OHLCV is the source of truth for daily volume. Daily check sum(trades volume) vs OHLCV volume\
Reason: `vci` recorded one trade wrong on 2026-11-06\
See: trades_reconciliation.ipynb