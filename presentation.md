---
marp: true
title: Cross-platform comparison of social media data in natural disaster management
author: Nikola Vračević
date: June 2024
theme: gaia
class: lead
paginate: true

---
![bg](img/rrt8.jpg)

## Cross-platform comparison of social media data in natural disaster management

#### MASTER’S THESIS

**Author**: Nikola Vračević


**PLUS supervisor**: Prof. Bernd Resch

**UBS supervisor**: Prof. Sébastien Lefèvre

---
![bg](img/rrt8.jpg)

## Disasters

- **Definition**: Disturbance to community's normal functioning
- **Types**: *Natural*, man-made, and hybrid
- **Frequency**: Increased from 369/year (2003-2022) to 399 in 2023
- **Impact**: Floods, storms, earthquakes, droughts

---
![bg](img/rrt8.jpg)

## Disaster Management Cycle

1. **Prevention**
2. **Preparedness**
3. **Response**
4. **Recovery**

- **Data Sources**: Remote sensing, sensors, *crowdsourcing*, *GNSS* 
    - pronounced spatial component
- **Social Media**: Key role in preparedness, response phase

---
![bg](img/rrt8.jpg)

## Social Media Data

- **Importance**: Valuable for sociology, communication, environmental studies
- **Content**: *Textual*, visual, *metadata*
- **General Challenges**: Underutilized datasets, advanced analysis techniques not fully leveraged

---
![bg](img/rrt8.jpg)

## Geographic Information

- **Critical**: Understanding hazards, exposure, vulnerability
- **Social media data**:
  - **Geotagging**: GNSS services
  - **Geoparsing**: Inferring location from the content
    - LER
    - Geocoding
---
![bg](img/rrt8.jpg)

## LER examples

- HOW TO HELP #HurricaneIan victims if you're in #**miami** #coralgables #doral #kendall #hialeah #**Florida**

- hurricaneian is little fun through the destruction of **fort myers**
- I'm in **Tampa** going to **Fort Lauderdale** for two days, flying tonight and then flying back to **Tampa** Monday night, really don't want to leave my husband and pets alone at home in **Tampa** in the storm if my flight is canceled, how do I find out if my Monday night flight we be affected? If it is what are alternatives to get back to **Tampa** from **Fort Lauderdale** before the storm hits?

---
![bg](img/rrt8.jpg)

## Geocoding example
![width:700px](img/geocoding.png)


---
![bg](img/rrt8.jpg)

## Platforms Overview

- **Geotagging**: Twitter (X), Facebook, Instagram, Flickr...
- **Geoparsing**: TikTok, Reddit, Telegram, Mastodon...

---
![bg](img/rrt8.jpg)

## API Limitations
- **Facebook (April 2018)** -> APIcalypse
- **Twitter (May 2023)** -> PostAPI age

---
![bg](img/rrt8.jpg)

## Platforms Utilization

- **Twitter (X)**: 
    - omni present -> single-platform bias 
- **Others**: 
    - TikTok, Reddit, Telegram, Mastodon - unknown capabilities

---
![bg](img/rrt8.jpg)

## Motivation - Research Questions

*Simplified*

1. Are and how useful are underexplored platforms? (in the new Post-API era?)

2. If yes? - how different platforms are in terms of their geoparsed and geotagged locations?

---
![bg](img/rrt8.jpg)


## Methodology

1. Event selection
2. Platforms selection
3. Data collection
4. Geoparsing
5. Metrics definition
6. Dataset comparison

---
![bg](img/rrt8.jpg)


## Case Study: 
### Hurricane Ian
#### Florida, September 2022


---
![bg](img/rrt8.jpg)

## Examined platforms

Open API, user base, growth potential

![width:100](img/telegram2.png) ![width:80](img/mastodon.jpeg) ![width:100](img/twitter.png) ![width:90](img/reddit.jpg) ![width:100](img/tiktok.jpg)


---
![bg](img/rrt8.jpg)

## API comparison

![](img/api.jpg)

---
![bg](img/rrt8.jpg)

## Data collection
Filtering and relatedness algorithm

| **Platform**         | **Retrieved Posts** | **Filtered Posts** |
|----------------------|---------------------|---------------------|
| Twitter              | 704,342             | 13,531              |
| TikTok               | 168,761             | 168,761             |
| Reddit Submissions   | 31,187              | 31,187              |
| Reddit Comments      | 169,861             | 169,861             |
| Telegram             | 41 million          | 7,268               |
| Mastodon             | 1,068,618           | 902                 |

**Table** Summary of retrieved and filtered posts 




---
![bg](img/rrt8.jpg)

## Geoparsing

1. SpaCy over BERT for LER
2. Nominatim over Google Maps for geocoding
3. Remove remote locations and "Florida"


---
![bg](img/rrt8.jpg)

## Geoparsing results 

![](img/geoparsingindices.png)


---
![bg](img/rrt8.jpg)

## Time series 

![](img/timeseriesgeoparsed.png)


---
![bg](img/rrt8.jpg)

## Metrics Definition

1. **Distance-based metrics**
   - Focus on proximity

2. **Distribution-based metrics**
   - Emphasize geographic location and spatial distribution.
---
![bg](img/rrt8.jpg)

## Key Considerations in Metrics Definition

- Avoid heavy influence of input parameters 
- Metrics build upon each other

![width:1000](img/distance_based_overview.png)
**Figure 1:** Characteristics of distance-based metrics



---
![bg](img/rrt8.jpg)

## Monte Carlo Simulation
![width:800](img/montecarlo_nn_good_area.png)



---
![bg](img/rrt8.jpg)

## Nearest neighbor analysis

![width:900](img/nntable.jpg)

---
![bg](img/rrt8.jpg)

## Ripley's K function
![width:550](img/ripleys_K.png)


---
![bg](img/rrt8.jpg)

## ECDF of pairwise distances
![width:800](img/ecdf_pairwise.png)


---
![bg](img/rrt8.jpg)

## Distribution-based metrics


- **Standard Deviational Ellipse**: Summarizes distribution patterns.
- **Point Density**: Analyzes global distribution and density peaks.
- **Multiscale Correlation**: Assesses pattern similarity at different scales.


---
![bg](img/rrt8.jpg)

## SDEs and Mean Centers
![](img/ellipses_map.png)

---
![bg](img/rrt8.jpg)

## Point Density
![width:800](img/kde.png)

---
![bg](img/rrt8.jpg)

## ECDF of Latitude and Longitude
![width:800](img/ecdf_coordinates.png)

---
![bg](img/rrt8.jpg)

## Posts Distribution Across Different Levels
![width:350](img/map_counties.png) ![width:350](img/map_county_subdivisions.png)  ![width:350](img/map_census_tracts.png) 


---
![bg](img/rrt8.jpg)

## Pearson's r For Different ADM Levels
![width:350](img/counties_correlation.png) ![width:350](img/counties_subdivisions_correlation.png) ![width:350](img/census_tracts_correlation.png)



---
![bg](img/rrt8.jpg)

## Scatterplot matrices
![width:350](img/pearsons_counties.png) ![width:350](img/pearsons_county_subdivisions.png) ![width:350](img/pearsons_census_tracts.png)


---
![bg](img/rrt8.jpg)

# Conclusion

---
![bg](img/rrt8.jpg)

## Contributions

- Uncovered usability of underexplored platforms
- Highlighted need for tailored approaches to extract geographic information
- Demonstrated that metric choices affect dataset similarity and dissimilarity
- Suggested combining geoparsed and geotagged data for better representation

---
![bg](img/rrt8.jpg)

## Limitations

- Query selection bias due to keyword "hurricane".
- Platform-specific data collection challenges, e.g., TikTok lacks comments.
- Inconsistencies in API data collection methods affected data comparability.
- Temporal and regional bias from studying Hurricane Ian.
- Using general-purpose models like spaCy for location entity recognition may produce false results.
- Text length and style variations across platforms challenge geoparsing accuracy.
---

![bg](img/rrt8.jpg)

## Future work

- Need for LER models trained and validated on datasets other than Twitter.



---
![bg](img/rrt8.jpg)

## Acknowledgements

- Prof. Bernd Resch and Prof. Sébastien Lefèvre
- Nefta Kanilmaz Umut and Sebastian Schmidt
- David Hanny and Helen Ngonidzashe Serere 


---

# Thank You!

Questions?

Nikola Vračević

