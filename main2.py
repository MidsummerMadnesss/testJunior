import requests
import pandas as pd

workspace_id = "64db74c87d07c741807de394"
project_id = "64db75426e1d7578a3c967e2"

url = "https://api.clockify.me/api/v1/workspaces/{workspaceId}/projects/{projectId}/tasks"

headers = {
    "x-api-key": "NTk4NTRjODctOGI0MC00MDhkLWE5NDMtOGFiN2EwOTc0YWNl"
}

response = requests.get(url.format(workspaceId=workspace_id, projectId=project_id), headers=headers)
print(response.json())
data = response.json()
df = pd.DataFrame(data)
sorted_df = df.sort_values(by="name")
sorted_df.to_csv("tasks.csv", index=False)
print("Done!")