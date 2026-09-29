---
title: 'Integrated supervisory control and fixed path speed trajectory generation for hybrid electric ships via convex optimization'
# If group member, use folder name in /content/authors
authors:
  - Antti Ritari
  - Niklas Katzenburg
  - g_fabricio-oliveira
  - Kari Tammi
date: 2023-07-13
doi: 10.48550/arXiv.2307.06184

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['3']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*arXiv*'
publication_short: ''

abstract: 'Battery-hybrid power source architectures can reduce fuel consumption and emissions for ships with diverse operation profiles. However, conventional control strategies may fail to improve performance if the future operation profile is unknown to the controller. This paper proposes a guidance, navigation, and control (GNC) function that integrates trajectory generation and hybrid power source supervisory control. We focus on time and fuel optimal path-constrained trajectory planning. This problem is a nonlinear and nonconvex optimal control problem, which means that it is not readily amenable to efficient and reliable solution onboard. We propose a nonlinear change of variables and constraint relaxations that transform the nonconvex planning problem into a convex optimal control problem. The nonconvex three-degree-of-freedom dynamics, hydrodynamic forces, fixed pitch propeller, battery, and general energy converter (e.g., fuel cell or generating set) dissipation constraints are expressed in convex functional form. A condition derived from Pontryagin''s Minimum Principle guarantees that, when satisfied, the solution of the relaxed problem provides the solution to the original problem. The validity and effectiveness of this approach are numerically illustrated for a battery-hybrid vessel in model scale. First, the convex hydrodynamic hull and rudder force models are validated with towing tank test data. Second, optimal trajectories and supervisory control schemes are evaluated under varying mission requirements. The convexification scheme in this work lays the path for the employment of mature, computationally robust convex optimization methods and creates a novel possibility for real-time optimization onboard future smart and unmanned surface vehicles.'

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.48550/arXiv.2307.06184'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Categories
#  These asociate the publications with the icons representing reearch topics and application areas
categories: [Efficient formulation and solution methods, Energy systems]

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