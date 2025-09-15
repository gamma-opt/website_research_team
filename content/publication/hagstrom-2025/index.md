---
title: 'A novel strong duality-based reformulation for trilevel infrastructure models in energy systems development'
# If group member, use folder name in /content/authors
authors:
  - p_fredrik-hagstrom
  - Vikas Garg
  - g_Fabricio-Oliveira 	

date: 2025-08-01
doi: 10.1016/j.enbuild.2025.115761

# Schedule page publish date (NOT publication's date).
publishDate: 2017-01-01

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name. Notice * * on title. # Publication name and optional abbreviated publication name. Quote marks needed for Markdown typesetting
publication: '*Energy and Buildings*'
publication_short: 'ENB'

abstract: Buildings account for 40 % of global energy consumption. A considerable portion of building energy consumption stems from heating, ventilation, and air conditioning (HVAC), and thus implementing smart, energy-efficient HVAC systems has the potential to significantly impact the course of climate change. In recent years, model-free reinforcement learning algorithms have been increasingly assessed for this purpose due to their ability to learn and adapt purely from experience. They have been shown to outperform classical controllers in terms of energy cost and consumption, as well as thermal comfort. However, their weakness lies in their relatively poor data efficiency, requiring long periods of training to reach acceptable policies, making them inapplicable to real-world controllers directly. In this paper, we demonstrate that using federated learning to train the reinforcement learning controller of HVAC systems can improve the learning speed, as well as improve their ability to generalize, which in turn facilitates transfer learning to unseen building environments. In our setting, a global control policy is learned by aggregating local policies trained on multiple data centers located in different climate zones. The goal of the policy is to simultaneously minimize energy consumption and maximize thermal comfort. We perform a thorough set of experiments, evaluating three different optimizers for local policy training, as well as three different federated learning algorithms against two alternative baselines. We demonstrate through experimental evaluation that these effects lead to a faster learning speed, as well as greater generalization capabilities in the federated policy compared to any individually trained policy. Furthermore, the learning stability is significantly improved, with the learning process and performance of the federated policy being less sensitive to the choice of parameters and the inherent randomness of reinforcement learning.

# Summary. An optional shortened abstract.
summary:  

# Not in use. Could be used for keywords 
tags:
  
featured: false

# links:
url_pdf: 'https://doi.org/10.1016/j.enbuild.2025.115761'
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
projects: [2022-AF-Easy_DR]

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