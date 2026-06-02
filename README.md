# Dota 2 Heroes K-Means Clustering

## Overview
This project applies unsupervised machine learning (K-Means Clustering) to categorize Dota 2 heroes based purely on their raw statistical attributes, without any prior knowledge of the game's meta or hero roles. The goal is to discover hidden mathematical patterns in hero design.

## Tech Stack
* **Python**
* **Pandas** (Data manipulation and cleaning)
* **OpenDota API** (Automated data collection)
* **Custom K-Means Algorithm** (Math module)

## Methodology
1. **Data Collection:** Automated extraction of live hero statistics via the OpenDota API.
2. **Data Preprocessing:** * Handled dirty data (e.g., dropping newly added heroes with missing stats).
   * Applied **Min-Max Scaling** to normalize features like `move_speed` and `attribute_gain` to a 0-1 range, ensuring equal weight in distance calculations and preventing zero-division errors for static attributes.
3. **Modeling:** Implemented a K-Means algorithm from scratch using Euclidean distance to group heroes into 4 distinct clusters.

## Key Insights
The algorithm successfully reconstructed established game roles entirely blind, using only raw integers:
* **Cluster 1 (Casters/Supports):** Clustered heroes with low armor/health but massive intelligence gain (e.g., Zeus, Witch Doctor).
* **Cluster 2 (Carries):** Identified agility-based heroes with high movement speed and physical scaling (e.g., Anti-Mage, Phantom Assassin).
* **Cluster 3 (Tanks/Initiators):** Grouped massive strength heroes with high base health and strength gain (e.g., Axe, Tidehunter, Centaur).

This project demonstrates the power of unsupervised learning in extracting meaningful business logic and categorizations from raw, unstructured data.