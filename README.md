# F1 Race Intelligence

F1 Race Intelligence is a Formula 1 data analysis and visualization project designed to explore driver performance, team rankings, race outcomes, reliability issues, tyre compounds, country-wise participation, and podium achievements.

The project combines a web application, an interactive Tableau dashboard, and a Tableau story to make Formula 1 racing data easier to explore, compare, and understand.

## Project Links

- **GitHub Repository:** https://github.com/vijetanagda18/f1-race-intelligence
- **Live Web Application:** https://f1-race-intelligence-jbil.onrender.com/
- **Tableau Dashboard:** https://public.tableau.com/app/profile/vijeta.nagda/viz/F1_Race_Intelligence/F1RaceIntelligenceDashboard
- **Tableau Story:** https://public.tableau.com/app/profile/vijeta.nagda/viz/F1_Race_Intelligence/F1RaceIntelligenceStory
- **Project Demonstration Video:** https://drive.google.com/file/d/15eI2hx3_APTkmxdC1usUjLN9-OaTAr51/view?usp=drivesdk

## Project Overview

Formula 1 generates data related to race results, qualifying sessions, lap times, driver standings, teams, and circuits. Analyzing this information can help identify performance patterns and compare results across drivers, teams, and seasons.

F1 Race Intelligence organizes racing data into meaningful visualizations and provides an interactive way to explore different aspects of Formula 1.

The project focuses on transforming structured racing data into useful insights through data visualization and analysis.

## Key Features

- Interactive Formula 1 data analysis.
- Driver performance leaderboard.
- Team performance and championship ranking.
- Season-wise points trajectory.
- Driver reliability analysis based on Did Not Finish (DNF) reasons.
- Geographical visualization of country-wise data.
- Country-wise race participation analysis.
- Tyre compound distribution.
- Podium achievements by driver and team.
- Interactive Tableau filters for race years and DNF reasons.
- A deployed web application and a Tableau story for presenting the analysis.

## Tableau Dashboard Visualizations

The dashboard contains the following visualizations:

### 1. Global Driver Distribution Across Grand Prix Nations

A geographical map displaying country-level values to help explore the geographical distribution represented in the dataset.

### 2. Driver Reliability Analysis

A stacked bar chart comparing recorded DNF reasons across drivers. Categories include brake failure, collision, engine problems, gearbox issues, hydraulics, and mechanical failures.

### 3. Driver Performance Leaderboard

A bar chart comparing driver points and highlighting drivers with higher recorded point totals.

### 4. Points Trajectory

A multi-line chart displaying points across seasons from 2010 to 2026. It helps compare changes in points over time.

### 5. Team Performance Ranking

A horizontal bar chart comparing the points associated with different Formula 1 teams.

### 6. Team Championship Analysis

A vertical bar chart comparing team points to show differences in the displayed championship performance.

### 7. Country-wise Race Participation

A treemap representing country-level values through rectangles of different sizes, making comparisons between categories easier.

### 8. Tyre Compound Distribution

A pie chart displaying the distribution of Soft, Medium, Hard, and Intermediate tyre categories.

### 9. Podium Achievements by Driver and Team

A packed bubble chart representing podium-related records through circles of different sizes and colors.

### 10. Interactive Filters

The dashboard includes filters for DNF reasons and race years, allowing users to explore selected categories and seasons where supported by the connected visualizations.

## Dataset Description

The project uses an Excel dataset containing five worksheets and a total of 13,748 data records, excluding header rows.

| Worksheet | Number of Records | Description |
|---|---:|---|
| race_results | 6,464 | Race results, driver and team details, points, finishing positions, DNF information, pit stops, tyre strategy, and other race-related fields. |
| qualifying_results | 3,130 | Qualifying positions, lap times, driver and team details, sector times, gaps to pole, tyre compounds, and speed information. |
| lap_intelligence | 3,814 | Lap times, sector times, tyre compounds, tyre age, DRS status, speed-trap information, and pit-lap indicators. |
| championship_standings | 311 | Driver standings, season points, teams, wins, podiums, pole positions, DNFs, and champion indicators. |
| circuits | 29 | Circuit names, countries, cities, lap counts, lap lengths, circuit types, altitude, and direction. |

### Dataset Notes

- The race_results worksheet contains 6,464 records, matching the race-outcome count displayed on the dashboard.
- The dashboard displays 10 competing teams, 17 seasons, and 24 showcased circuits.
- The circuits worksheet contains 29 records, while the dashboard showcases 24 circuits. These figures represent different aspects of the project.
- The values displayed in each visualization depend on the selected fields, filters, and aggregation methods.
- The dataset should be checked against official Formula 1 records before using its values as verified historical statistics.

## Tools and Technologies

- **Microsoft Excel:** Used to store and organize the structured dataset.
- **Tableau Public:** Used to create interactive visualizations, the dashboard, and the story.
- **Web Application:** Provides browser-based access to the project.
- **GitHub:** Used for source-code management, version control, and project documentation.
- **Render:** Used to host the live web application.

The exact programming languages, libraries, and frameworks used in the web application can be identified from the source code and dependency files in the repository.

## How to Explore the Project

1. Visit the [Live Web Application](https://f1-race-intelligence-jbil.onrender.com/).
2. Explore the [Tableau Dashboard](https://public.tableau.com/app/profile/vijeta.nagda/viz/F1_Race_Intelligence/F1RaceIntelligenceDashboard).
3. View the [Tableau Story](https://public.tableau.com/app/profile/vijeta.nagda/viz/F1_Race_Intelligence/F1RaceIntelligenceStory).
4. Watch the [Project Demonstration Video](https://drive.google.com/file/d/15eI2hx3_APTkmxdC1usUjLN9-OaTAr51/view?usp=drivesdk).
5. Browse the GitHub repository to explore the source code and supporting project files.

## Project Objectives

- Vijeta Nagda
