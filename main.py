import requests
import pandas as pd

workspace_id = "64db74c87d07c741807de394"
project_id = "64db75426e1d7578a3c967e2"
api_key = "NTk4NTRjODctOGI0MC00MDhkLWE5NDMtOGFiN2EwOTc0YWNl"
report_url = f"https://reports.api.clockify.me/v1/workspaces/{workspace_id}/reports/detailed"

headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

payload = {"dateRangeStart": "2023-01-22T00:00:00.000",
"dateRangeEnd": "2023-12-22T23:59:59.000",
"detailedFilter": {
"page": 1,
"pageSize": 50},
"exportType": "CSV"}

response = requests.post(report_url, json=payload, headers=headers)

if response.status_code == 200:
    with open("tasks_report.csv", "wb") as f:
        f.write(response.content)

    # Read the CSV file into a DataFrame
    df = pd.read_csv("tasks_report.csv")

    # Sort the DataFrame by the "time started" column
    df.sort_values(by="Start Time", inplace=True)

    # Save the sorted DataFrame back to the same CSV file
    df.to_csv("tasks_report.csv", index=False)

    print("CSV file 'tasks_report.csv' sorted and saved successfully.")
else:
    error_message = response.text
    print("Error generating report. Status code:", response.status_code)
    print("Error message:", error_message)

url = "https://api.clockify.me/api/v1/workspaces/{workspaceId}/projects/{projectId}/tasks"

headers1 = {
    "x-api-key": "NTk4NTRjODctOGI0MC00MDhkLWE5NDMtOGFiN2EwOTc0YWNl"
}

response = requests.get(url.format(workspaceId=workspace_id, projectId=project_id), headers=headers1)
print(response.json())
data = response.json()
df = pd.DataFrame(data)
sorted_df = df.sort_values(by="name")
sorted_df.to_csv("tasks.csv", index=False)
print("Done!")
