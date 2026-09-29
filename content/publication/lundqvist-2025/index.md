---
title: 'Employing Deep Neural Operators for PDE control by decoupling training and optimization'
# If group member, use folder name in /content/authors
authors:
  - g_oliver_lundqvist
  - g_fabricio-oliveira
date: 2025-06-06
doi: 10.48550/arXiv.2506.04742

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

abstract: 'Neural networks have been applied to control problems, typically by combining data, differential equation residuals, and objective costs in the training loss or by incorporating auxiliary architectural components. Instead, we propose a streamlined approach that decouples the control problem from the training process, rendering these additional layers of complexity unnecessary. In particular, our analysis and computational experiments demonstrate that a simple neural operator architecture, such as DeepONet, coupled with an unconstrained optimization routine, can solve tracking-type partial differential equation (PDE) constrained control problems with a single physics-informed training phase and a subsequent optimization phase. We achieve this by adding a penalty term to the cost function based on the differential equation residual to penalize deviations from the PDE constraint. This allows gradient computations with respect to the control using automatic differentiation through the trained neural operator within an iterative optimization routine, while satisfying the PDE constraints. Once trained, the same neural operator can be reused across different tracking targets without retraining. We benchmark our method on scalar elliptic (Poisson''s equation), nonlinear transport (viscous Burgers'' equation), and flow (Stokes equation) control problems. For the Poisson and Burgers problems, we compare against adjoint-based solvers: for the time-dependent Burgers problem, the approach achieves competitive accuracy with iteration times up to four times faster, while for the linear Poisson problem, the adjoint method retains superior accuracy, suggesting the approach is best suited to nonlinear and time-dependent settings. For the flow control problem, we verify the feasibility of the optimized control through a reference forward solver.'

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.48550/arXiv.2506.04742'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Categories
#  These asociate the publications with the icons representing reearch topics and application areas
categories: [Efficient formulation and solution methods]

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