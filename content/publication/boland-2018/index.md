---
title: A parallelizable augmented Lagrangian method applied to large-scale non-convex-constrained
  optimization problems
# If group member, use folder name in /content/authors
authors:
  - Natashia Boland
  - Jeffrey Christiansen
  - Brian Dandurand
  - Andrew Eberhard
  - g_fabricio-oliveira
date: 2019-05-01
doi: 10.1007/s10107-018-1253-9

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*Mathematical Programming*'
publication_short: ''

abstract: LWe contribute improvements to a Lagrangian dual solution approach applied
  to large-scale optimization problems whose objective functions are convex, continuously
  differentiable and possibly nonlinear, while the non-relaxed constraint set is compact
  but not necessarily convex. Such problems arise, for example, in the split-variable
  deterministic reformulation of stochastic mixed-integer optimization problems. The
  dual solution approach needs to address the nonconvexity of the non-relaxed constraint
  set while being efficiently implementable in parallel. We adapt the augmented Lagrangian
  method framework to address the presence of nonconvexity in the non-relaxed constraint
  set and the need for efficient parallelization. The development of our approach
  is most naturally compared with the development of proximal bundle methods and especially
  with their use of serious step conditions. However, deviations from these developments
  allow for an improvement in efficiency with which parallelization can be utilized.
  Pivotal in our modification to the augmented Lagrangian method is the use of an
  integration of approaches based on the simplicial decomposition method (SDM) and
  the nonlinear block Gauss-Seidel (GS) method. An adaptation of a serious step condition
  associated with proximal bundle methods allows for the approximation tolerance to
  be automatically adjusted. Under mild conditions optimal dual convergence is proven,
  and we report computational results on test instances from the stochastic optimization
  literature. We demonstrate improvement in parallel speedup over a baseline parallel
  approach.

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
---