# Antimicrobial Resistance Simple Data Analysis
# Author: Bushra Mumtaz

import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (you can replace later with real data)
data = {
    "Antibiotic": ["Ampicillin", "Ciprofloxacin", "Gentamicin", "Ceftriaxone", "Meropenem"],
    "Resistance_Rate": [80, 45, 30, 60, 10]
}

df = pd.DataFrame(data)

print("Antimicrobial Resistance Dataset:")
print(df)

# Plotting
plt.figure(figsize=(8,5))
plt.bar(df["Antibiotic"], df["Resistance_Rate"])
plt.title("Antimicrobial Resistance Pattern in Klebsiella pneumoniae")
plt.xlabel("Antibiotics")
plt.ylabel("Resistance Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
