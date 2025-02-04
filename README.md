# Michigan-Water-Usage-Kaggle-DA
Analyze water usage by Michigan industries from 2013-2022 using a Kaggle dataset. Python project using NumPy, TKinter, and Matplotlib.

Libraries Used
<ul>
    <li>Numpy: Used to load and preprocess data</li>
    <li>TKinter: Used to create windows</li>
    <li>Matplotlib: Used to create plots and graphs</li>
</ul>
<br>
Dev-Log
<ul>
    <li>6-28-2024: Initialize Project - loaded data with Numpy and created TKinter window with a single button</li>
    <li>6-29-2024: Bar Graph day 1 - Created labels for bar graph option, exploring TKinter's geometry options</li>
    <li>6-30-2024: Bar Graph day 2 - Cretaed labels and dropdown menus for the bar graph option and created a frame for the window</li>
    <li>7-4-2024: Bar Graph day 3 - Created bars graphs with x and y data specified by user, creates multiple graphs if 1 graph would be too crowded. All graphs have the same y-axis so data can be fairly compared.</li>
    <li>7-7-2024: Bar Graph day 4 - Started working on creating a specifier for bar graphs so users can be more specific in their analysis</li>
    <li>7-8-2024: Bar Graph day 5 - Specifier works so when a user selects a limiting field, the options for that field are in the next menu, working on those updated options functioning as changes/clicks on the menu</li>
    <li>7-14-2024: Bar Graph day 6 - OptionsMenus now work so that users cannot limit the option on the x-axis and can change between x-axis options while limiting the others. Next task is having this reflected in the produced graphs.</li>
    <li>7-18-2024: Bar Graph day 7 (Final) - Bar graphs now show data with or without selected limiters, small optimizations to presentation. Added comments and spacing for code for readability.</li>
    <li>7-20-2024: Multi-line Graph day 1 - Started work on multi-line graphs, simplified code by making similar label creation its own function.</li>
    <li>7-21-2024: Multi-line Graph day 2 - Continued work on creating elements for multi-line window: added 'Compare' menus so users can select 3 data points to compare on a line graph</li>
    <li>7-29-2024: Multi-line Graph day 3 - Started work on creating actual graph; grabbing data for each x-axis point by year</li>
    <li>8-3-2024: Multi-line Grapg day 4 (Final) - Finished creating graph for multiline comparisons, copare counties or industries in specific water usage per year</li>
</ul>
