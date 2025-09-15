---
title: 'Simulator-based surrogate optimisation employing adaptive uncertainty-aware sampling'
# If group member, use folder name in /content/authors
authors:
  - g_Yu-Liu
  - g_Fabricio-Oliveira 	

date: 2025-10-01
doi: 10.1016/j.orl.2025.107308

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*Computers and Chemical Engineering*'
publication_short: 'ORL'

abstract: Optimisation problems involving computationally expensive, black-box functions derived from high-fidelity engineering simulations remain challenging. To efficiently bridge the simulators and optimisation processes, we introduce an adaptive framework for surrogate modelling and optimisation. Our method employs low-discrepancy sequence sampling to select points, followed by training a surrogate model using a piecewise linear neural network (NN) with rectified linear unit (ReLU) activation. Using mixed-integer programming (MIP), we reformulate the ReLU NN as embedded components of an optimisation problem and solve it to find an optimal simulator input. This is achieved by iteratively refining the solution via resampling the simulator, retraining the surrogate model, and rebuilding and resolving the MIP problem. For resampling, an infill strategy that incorporates uncertainty assessment and a solution pool is employed, balancing exploration and exploitation. Moreover, computational efficiency is boosted by bound tightening, lossless model compression, and memory structure reuse. Validation on practical engineering applications confirms significant optimisation efficiency gains from the domain-refined strategy.

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.1016/j.orl.2025.107308'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Categories
#  These asociate the publications with the icons representing reearch topics and application areas
categories: [Modelling decision-making and uncertainty, Efficient formulation and solution methods]

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