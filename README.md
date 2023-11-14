<h1>Subdomain Checker </h1>

<h3> Disclaimer </h3>
This code is slow to run depending on the speed of internet connection. Please wait until it loads.

Certain domains and subdomains could be blocked from access (sublist3r). Please try another website or subdomain incase it is blocked.

<h3> Overview </h3>
This code helps monitor the status of subdomains and services running on a website. This script periodically checks the availability of specified subdomains and updates the status in a tabular format on the screen. 

<h3> Requirements</h3>
Python 3.8 and above
Sublist3r Library
Tabulate package
Python bundled packages- time and requests
Internet Connection (recommended 100mbps or higher): This program takes a long time to run as it has to fetch multiple domains at a time.  A better internet connection is an added plus to run this code.
To install the required package, try the command pip install sublist3r and pip install tabulate

<h3> Procedure</h3>
1. Running the Script
To start monitoring the subdomains, run the script using the following command:
python montiorsubdomains.py

2. Run Time Configuration
While the script is running ,you will receive a script where you need to configure it by either specifying the subdomains or by choosing a mode which gets and displays all the subdomains available on the website. However some domains might be blocked for your network access, might be blocked by your browser or by your router/service provider.
There are 2 modes for operation:
1 to configure your own domains and 2 to run the advanced mode

  
 
	


  
 
	


