---
title: A two-stage stochastic programming model for periodic replenishment control
  system under demand uncertainty
# If group member, use folder name in /content/authors
authors:
  - Paulo Cunha
  - Fernanda Raupp
  - g_fabricio-oliveira
date: 2017-05-01
doi: 10.1016/j.cie.2017.03.025

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*Computers & Industrial Engineering*'
publication_short: ''

abstract: The inventory control system consists of defining strategies to manage inventory
  replenishment such that costs involved in ordering, holding, and meeting the demands
  are optimized. Although several methods for inventory management are proposed in
  the literature, the assumptions made necessary can hinder their applicability in
  practice. Motivated by this fact, we propose a methodology for determining the optimal
  parameters of an inventory control system for single-item one-echelon supply chains
  using two-stage stochastic programming, considering periodic review and uncertain
  demand. The proposed approach is flexible enough to consider backlogs or lost sales
  cases without limitations on the number of outstanding orders and allows the consideration
  of uncertainties in a more comprehensive manner when compared to currently available
  methods. The optimal review periodicity and the inventory target level are determined
  using a nonlinear mixed-integer programming model, which takes into account the
  uncertain nature of the item demand levels through a finite set of scenarios. We
  present how this model can be reformulated as a deterministic equivalent mixed-integer
  linear programing model and how the Sample Average Approximation method can be used
  to incorporate the uncertainty into it. To validate the proposed approach, we perform
  a simulation-based sensitivity analysis in the neighborhood of the solutions obtained.
  We also compare them with those obtained applying the Hadley-Whitin method, considering
  the premises that are necessary for the later. Further, we present results from
  a case in which the stochastic demand is not stationary. The results obtained provide
  strong evidence of the potential of the proposed approach.

# Summary. An optional shortened abstract.
summary: 

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Categories
#  These asociate the publications with the icons representing reearch topics and application areas
categories: [Modelling decision-making and uncertainty, Production and operations planning]

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
---