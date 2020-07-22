# Lists users in Power BI service

Since Power BI service has yet to implement an option to export all workspace users, this little 
script might come in handy.

#### Getting started
Make sure to install the required libraries by running `pip install -r requirements.txt`, then

1. Log on to Power BI service and navigate to your workspace
1. **Right click > Save As...** to save the page with users as html file 
(in Microsoft Edge, other browsers might require you to inspect the source code first and save the html code from there)
1. Run the script `python list-users.py <your file.html>`

#### Example
    > python list-users.py example.html
        Alice (Lezer)
        Bob (Lezer)
        Carol (Lid)
        Dave (Inzender)
        Eve (Beheerder)
