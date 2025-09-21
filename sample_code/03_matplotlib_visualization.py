# Episode 3: Visualizing Tabular Data with Matplotlib
# Sample code for creating plots and visualizations

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Load and Prepare Data
# ============================================================

# Load inflammation data
data = np.loadtxt("data/inflammation-01.csv", delimiter=",")

# Calculate daily statistics
daily_means = np.mean(data, axis=0)
daily_max = np.max(data, axis=0)
daily_min = np.min(data, axis=0)

print("Data loaded successfully!")
print("Shape:", data.shape)
print("Daily means calculated for", len(daily_means), "days")

# ============================================================
# Basic Line Plots
# ============================================================

# Create a simple line plot of daily means
plt.figure(figsize=(10, 6))
plt.plot(daily_means)
plt.title("Average Inflammation Per Day")
plt.xlabel("Day")
plt.ylabel("Average Inflammation")
plt.grid(True, alpha=0.3)
plt.savefig("sample_code/plots/01_daily_means.png", dpi=150, bbox_inches="tight")
plt.show()

# Plot multiple statistics on the same graph
plt.figure(figsize=(12, 8))
plt.plot(daily_means, label="Mean", linewidth=2)
plt.plot(daily_max, label="Maximum", linewidth=2)
plt.plot(daily_min, label="Minimum", linewidth=2)
plt.title("Daily Inflammation Statistics")
plt.xlabel("Day")
plt.ylabel("Inflammation Level")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("sample_code/plots/02_daily_statistics.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
# Customizing Plot Appearance
# ============================================================

# Create a more customized plot
plt.figure(figsize=(12, 8))

# Use different line styles and colors
plt.plot(daily_means, "b-", label="Mean", linewidth=2, alpha=0.8)
plt.plot(daily_max, "r--", label="Maximum", linewidth=2, alpha=0.8)
plt.plot(daily_min, "g:", label="Minimum", linewidth=2, alpha=0.8)

# Customize appearance
plt.title("Inflammation Data Over Time", fontsize=16, fontweight="bold")
plt.xlabel("Day of Treatment", fontsize=12)
plt.ylabel("Inflammation Level", fontsize=12)
plt.legend(fontsize=10, loc="upper right")
plt.grid(True, alpha=0.3)

# Add annotations
max_day = np.argmax(daily_means)
plt.annotate(
    f"Peak: Day {max_day}",
    xy=(max_day, daily_means[max_day]),
    xytext=(max_day + 5, daily_means[max_day] + 1),
    arrowprops=dict(arrowstyle="->", color="red"),
)

plt.tight_layout()
plt.savefig("sample_code/plots/03_customized_plot.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
# Subplots - Multiple Plots in One Figure
# ============================================================

# Create subplots for different views of the data
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Subplot 1: Daily means
ax1.plot(daily_means, "b-", linewidth=2)
ax1.set_title("Daily Mean Inflammation")
ax1.set_xlabel("Day")
ax1.set_ylabel("Mean Inflammation")
ax1.grid(True, alpha=0.3)

# Subplot 2: Individual patient data (first 5 patients)
for i in range(5):
    ax2.plot(data[i, :], label=f"Patient {i}", alpha=0.7)
ax2.set_title("First 5 Patients Over Time")
ax2.set_xlabel("Day")
ax2.set_ylabel("Inflammation")
ax2.legend()
ax2.grid(True, alpha=0.3)

# Subplot 3: Histogram of all inflammation values
ax3.hist(data.flatten(), bins=30, alpha=0.7, color="green")
ax3.set_title("Distribution of All Inflammation Values")
ax3.set_xlabel("Inflammation Level")
ax3.set_ylabel("Frequency")
ax3.grid(True, alpha=0.3)

# Subplot 4: Heatmap of inflammation data
im = ax4.imshow(data, cmap="hot", interpolation="nearest", aspect="auto")
ax4.set_title("Inflammation Heatmap (All Patients)")
ax4.set_xlabel("Day")
ax4.set_ylabel("Patient")
plt.colorbar(im, ax=ax4, label="Inflammation Level")

plt.tight_layout()
plt.savefig("sample_code/plots/04_subplots.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
# Different Plot Types
# ============================================================

# Scatter plot - relationship between first and last day
plt.figure(figsize=(10, 8))
first_day = data[:, 0]
last_day = data[:, -1]

plt.scatter(first_day, last_day, alpha=0.6, s=50)
plt.title("First Day vs Last Day Inflammation")
plt.xlabel("First Day Inflammation")
plt.ylabel("Last Day Inflammation")
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(first_day, last_day, 1)
p = np.poly1d(z)
plt.plot(first_day, p(first_day), "r--", alpha=0.8, linewidth=2, label="Trend")
plt.legend()

plt.savefig("sample_code/plots/05_scatter_plot.png", dpi=150, bbox_inches="tight")
plt.show()

# Bar plot - average inflammation by day ranges
plt.figure(figsize=(12, 6))

# Group days into weeks
week_1 = np.mean(daily_means[0:7])
week_2 = np.mean(daily_means[7:14])
week_3 = np.mean(daily_means[14:21])
week_4 = np.mean(daily_means[21:28])
week_5 = np.mean(daily_means[28:35])
week_6 = np.mean(daily_means[35:])

weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"]
week_means = [week_1, week_2, week_3, week_4, week_5, week_6]

bars = plt.bar(
    weeks, week_means, color=["red", "orange", "yellow", "green", "blue", "purple"]
)
plt.title("Average Inflammation by Week")
plt.xlabel("Treatment Week")
plt.ylabel("Average Inflammation")
plt.grid(True, alpha=0.3, axis="y")

# Add value labels on bars
for bar, value in zip(bars, week_means):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        f"{value:.1f}",
        ha="center",
        va="bottom",
    )

plt.savefig("sample_code/plots/06_bar_plot.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
# Comparing Multiple Data Files
# ============================================================

# Load and compare three data files
data_01 = np.loadtxt("data/inflammation-01.csv", delimiter=",")
data_02 = np.loadtxt("data/inflammation-02.csv", delimiter=",")
data_03 = np.loadtxt("data/inflammation-03.csv", delimiter=",")

# Calculate daily means for each file
daily_means_01 = np.mean(data_01, axis=0)
daily_means_02 = np.mean(data_02, axis=0)
daily_means_03 = np.mean(data_03, axis=0)

# Plot comparison
plt.figure(figsize=(12, 8))
plt.plot(daily_means_01, "b-", label="Dataset 1", linewidth=2)
plt.plot(daily_means_02, "r-", label="Dataset 2", linewidth=2)
plt.plot(daily_means_03, "g-", label="Dataset 3", linewidth=2)

plt.title("Comparison of Daily Means Across Datasets")
plt.xlabel("Day")
plt.ylabel("Average Inflammation")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("sample_code/plots/07_dataset_comparison.png", dpi=150, bbox_inches="tight")
plt.show()

# ============================================================
# Save Summary Figure
# ============================================================

# Create a comprehensive summary figure
fig = plt.figure(figsize=(16, 12))

# Main plot - daily statistics
ax_main = plt.subplot(2, 2, (1, 2))
plt.plot(daily_means, "b-", label="Mean", linewidth=3)
plt.fill_between(
    range(len(daily_means)), daily_min, daily_max, alpha=0.3, label="Min-Max Range"
)
plt.title("Inflammation Treatment Analysis - Dataset 1", fontsize=16, fontweight="bold")
plt.xlabel("Day of Treatment")
plt.ylabel("Inflammation Level")
plt.legend()
plt.grid(True, alpha=0.3)

# Histogram
ax_hist = plt.subplot(2, 2, 3)
plt.hist(data.flatten(), bins=20, alpha=0.7, color="skyblue", edgecolor="black")
plt.title("Inflammation Value Distribution")
plt.xlabel("Inflammation Level")
plt.ylabel("Count")
plt.grid(True, alpha=0.3)

# Patient progression
ax_patient = plt.subplot(2, 2, 4)
patient_means = np.mean(data, axis=1)
plt.plot(patient_means, "ro-", markersize=3, linewidth=1)
plt.title("Average Inflammation per Patient")
plt.xlabel("Patient ID")
plt.ylabel("Average Inflammation")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("sample_code/plots/08_summary_analysis.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n=== Visualization Complete ===")
print(f"Created plots for {len(daily_means)} days of treatment data")
print(f"Analyzed {data.shape[0]} patients")
print("All plots saved to 'sample_code/plots/' directory")
