1. using vnstock for API \
Reason: free API for Vietnamese stock market. Daily refresh, 10M+ rows 
2. ADC for local gcloud sign in\
Reason: No service account key exists, nothing secret is inside the project folder.  
3. using .env\
Reason: Secrets and settings kept out of code
4. requirements.txt \
Reason: Easier for users to setup the project
5. service account as scheduler \
Reason: `planned` 