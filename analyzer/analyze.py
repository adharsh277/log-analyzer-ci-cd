import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Log file path and output folders
LOG_FILE = "logs/sample.log"
REPORT_FOLDER = "reports"
SUMMARY_CSV = os.path.join(REPORT_FOLDER, "summary.csv")
ERROR_PLOT = os.path.join(REPORT_FOLDER, "error_graph.png")

# Regex pattern (Apache log style with custom timestamp)
log_pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<endpoint>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+)'
)

def parse_logs():
    data = []
    with open(LOG_FILE, "r") as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                entry = match.groupdict()
                try:
                    # Match timestamp: Wed Jul 16 12:17:19 UTC 2025
                    entry["time"] = datetime.strptime(entry["time"], "%a %b %d %H:%M:%S %Z %Y")
                except ValueError as ve:
                    print(f"⚠️ Skipping line with invalid time format: {entry['time']}")
                    continue
                entry["status"] = int(entry["status"])
                entry["size"] = int(entry["size"])
                data.append(entry)
    return pd.DataFrame(data)

def generate_report(df):
    print("🔎 Generating report...")
    total_requests = len(df)
    errors = df[df["status"] >= 400]
    error_count = len(errors)
    error_rate = round((error_count / total_requests) * 100, 2) if total_requests else 0

    # Create summary
    summary = {
        "Total Requests": [total_requests],
        "Error Count": [error_count],
        "Error Rate (%)": [error_rate]
    }
    pd.DataFrame(summary).to_csv(SUMMARY_CSV, index=False)
    print(f"✅ Summary CSV saved at {SUMMARY_CSV}")

def plot_errors_over_time(df):
    print("📊 Plotting error graph...")
    errors = df[df["status"] >= 400]
    if errors.empty:
        print("⚠️ No errors to plot.")
        return

    errors_by_minute = errors.groupby(errors["time"].dt.strftime("%H:%M"))["status"].count()

    plt.figure(figsize=(8, 4))
    errors_by_minute.plot(kind="line", marker="o", color="red")
    plt.title("Errors Over Time")
    plt.xlabel("Time (HH:MM)")
    plt.ylabel("Error Count")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(ERROR_PLOT)
    print(f"✅ Error graph saved at {ERROR_PLOT}")

if __name__ == "__main__":
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    df = parse_logs()
    if df.empty:
        print("❌ No valid logs found. Exiting.")
    else:
        generate_report(df)
        plot_errors_over_time(df)
        print("🎉 Log analysis complete.")
