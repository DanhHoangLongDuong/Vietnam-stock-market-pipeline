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