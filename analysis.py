import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")

df["Average"] = (
    df["Maths"] +
    df["Physics"] +
    df["Chemistry"]
) / 3
df["Rank"] = df["Average"].rank(
    ascending=False,
    method="min"
).astype(int)
print("Student Data:")
print(df)
print("\nShape:")
print(df.shape)
print("\nColumns:")
print(df.columns)
print("\nAverage Maths Marks:")
print(df["Maths"].mean())
max_avg = df["Average"].max()
print("\nTopper(s):")
print(
    df[df["Average"] == max_avg][
        ["Name", "Average"]
    ]
)
print("\nStudents Sorted by Average:")
print(
    df.sort_values(
        by="Average",
        ascending=False
    )[["Name", "Average", "Rank"]]
)
print("\nStudent Rankings:")
print(
    df[["Name", "Average", "Rank"]]
)
plt.figure(figsize=(8, 5))

plt.bar(
    df["Name"],
    df["Average"]
)

plt.title("Student Average Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Average Marks")
for i, avg in enumerate(df["Average"]):
    plt.text(
        i,
        avg + 1,
        round(avg, 2),
        ha="center"
    )
plt.savefig("student_analysis.png")
plt.show()