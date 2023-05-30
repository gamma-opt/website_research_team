---
# Documentation: https://wowchemy.com/docs/page-builder/
title: Research topics
widget: featurette 
weight: 15
headless: true  # This file represents a page section.

feature:
  - icon: decision_making
    icon_pack: custom
    name: Modelling decision-making and uncertainty
    description: '
   - Endogenous uncertainty
   
   - Robust optimisation
   
   - Stochastic programming
   
   - Machine learning & surrogate modelling
    '
  - icon: decomposition 
    icon_pack: custom
    name: Efficient formulation and solution methods
    description: '
     - Convexification techniques
     
     - Cutting planes & column generation
     
    - Lagrangian-based decomposition methods
    
    - Parallelisation
    '

---

<style>
	/* set font size for all undefined lists in the section research*/
	#research ul {font-size: 1.0rem}
	/* set image size*/
	#research .row.featurette .col-12 .featurette-icon img {
   	 height: 300px;
 	 width: 300px}
@media (min-width: 576px)
{   /* remove unnecessary "grey" object that appears on the page for some reason */
    #research .row.featurette .col-md-12:nth-child(2) {display: none}
    /* centre and make fit the whole space for the research topics  (each research topic takes 50% of the total width*/
    #research .row.featurette {justify-content: center}
    #research .row.featurette .col-12:nth-child(3), 
    #research .row.featurette .col-12:nth-child(4) {
    max-width: 100% !important;
    flex: 0 0 50%; }
    
}
 </style>