---
title: 'Predicer: abstract stochastic optimisation model framework for multi-market operation'
# If group member, use folder name in /content/authors
authors:
  - Esa Pursiheimo
  - Dennis Sundell
  - Juha Kiviluoma
  - g_helmi-hankimaa
date: 2023-08-09
doi: 10.1007/s11081-023-09824-w

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*Optimization and Engineering*'
publication_short: ''

abstract: An open-source modelling framework Predicer, standing for Predictive Decider, for multi-market day-ahead market operation purposes is described in this paper. The Predicer model uses scenario-based stochastic optimisation to obtain decision variables and bid matrixes for energy and reserve markets by maximising the risk-adjusted expected value of the profit during the model time frame. The modelled energy system structure is abstract, that is, based on basic elements such as nodes representing different energy types and processes representing flows between nodes. The abstract model structure enables user to construct arbitrary energy systems and define links between assets, commodities, energy markets and reserve markets. Predicer model can include properties such as unit ramp rates, online units, dynamic energy storages, market realisation and market bidding requirements. The aggregation of unit-based energy and reserve opportunities into a virtual power plant allows the asset owner to make optimized portfolio-level bids for different market products. The model scenarios consist of user defined forecasts for market prices, renewable energy supply, energy demand and other system related time series. Predicer is implemented in Julia programming language and uses the JuMP optimisation package.

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.1007/s11081-023-09824-w'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Categories
#  These asociate the publications with the icons representing reearch topics and application areas
categories: [Energy systems, Modelling decision-making and uncertainty, Production and operations planning]

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false
  
# remove social media icons 
share: false
---