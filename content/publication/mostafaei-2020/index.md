---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Efficient formulation for transportation scheduling of single refinery multiproduct pipelines
subtitle: ''
summary: ''
authors:
- p_hossein-mostafaei
- Pedro M. Castro
- g_fabricio-oliveira
- Iiro Harjunkoski

tags: 

categories: 

keywords: 

date: '2020-12-27'
lastmod: 2023-04-06T16:01:41+03:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

# Schedule page publish date (NOT publication's date).
publishDate: 

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

abstract: Multiproduct pipeline transportation scheduling is a complex operations research problem that is characterized by the movement of the cargo rather than the carrier. Hence, it cannot be solved using vehicle routing methods. While most formulations for short-term scheduling adopt a continuous-time representation, they often lead to suboptimal solutions because of the dependence on the number of time slots in the grid, which is difficult to predict. Furthermore, some of these formulations have poor linear relaxations due to the presence of inefficient big-M constraints. In this paper, we develop a discrete-time mixed integer linear programming (MILP) model for the detailed scheduling of a straight pipeline with a single refinery and multiple depots. The proposed formulation rigorously detects interface material generated between adjacent products and considers planned shutdowns in pipeline segments due to maintenance operations, as well as local market demands occurring at multiple intermediate due dates. The main novelty is that continuous tasks can span multiple time slots to enforce minimum batch sizes on injection and delivery nodes, which allows for the model to generate better schedules than those obtained with previously proposed formulations. To ensure an efficient model by design, we rely on generalized disjunctive programming (GDP) and on the convex hull reformulation of disjunctions, which results in stronger and often more computationally efficient formulations. We present numerical results for a set of benchmark instances and show that the proposed model applies to large-scale industrial cases.

publication: '*European Journal of Operational Research*'
doi: 10.1016/j.ejor.2020.12.034
---
