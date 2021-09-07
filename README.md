# Python Google Analytics API Tools

Zur vereinfachten Nutzung der Google Analtyics APIs:
- Reporting API v4
- MCF Reporting API v3
- Realtime API v3
- Queries auf BigQuery Export

```python
import gapy

client = gapy.Client(credentials_path, ga_view_id)
data = client.get_report(daterange, dimensions, metrics)
data.info() # display pd.DataFrame
```
