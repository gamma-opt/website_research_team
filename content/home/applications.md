---
# Documentation: https://wowchemy.com/docs/page-builder/
title: Application areas
widget: featurette 
weight: 20

feature:
  - icon: energy 
    icon_pack: custom
    name: Energy systems
    description: 
    
  - icon: production
    icon_pack: custom
    name: Production and operations planning
    description:
    
  - icon: supply_chain
    icon_pack: custom
    name: Supply chain management
    description:
    
  - icon: humanitarian_logistics
    icon_pack: custom
    name: Humanitarian and healthcare logistics
    description:

---
/* @media applies the features only if the specific conditions are met. In our case, it is if the minimum width of the device's screen used to see the website exceeds 576px. This number has been chosen in accordance with the HTML code of the main page. The code transforms the objects to be in one column, hence, more suitable for reading from smartphone and etc, once the device screen width is smaller than 576px */

<style>
	/* set icons sizes*/
	#applications .row.featurette .col-12 .featurette-icon img {
   	 height: 50%;
 	 width: 50%}
@media (min-width: 576px)
{   /* remove unnecessary "grey" object that appears on the page for some reason */
    #applications .row.featurette .col-md-12:nth-child(2) {display: none}
    /* centre and make fit the whole space for the applications section (each application takes 25% of the total width*/
    #applications .row.featurette {justify-content: center}
    #applications .row.featurette .col-sm-4 {
    max-width: 100% !important;
    flex: 0 0 25%; }

    
}
 </style>