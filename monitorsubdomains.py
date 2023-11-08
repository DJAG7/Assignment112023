#importing requests to search for url, time , sublist3r to find subdomains and tabulate to display tabular form
import requests
import time
import sublist3r
from tabulate import tabulate

# Function to check subdomain_status
def check_subdomain_status(domain, subdomain):   
    url = f"https://{subdomain}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code >= 100 and response.status_code <200:
            return subdomain, domain, "Up but Protocol Error"
        if response.status_code >= 200 and response.status_code <300:
            return subdomain, domain, "Up"
        
        #Checking for Redirects using HTTP Response Codes 3XX
        elif response.status_code >=300 and response.status_code <400:
            return subdomain, domain, "Up but Redirected"
        
        #Checking Client Error Responses using HTTP Response Codes 4XX
        elif response.status_code >=400 and response.status_code <500:
            if response.status_code == 400:
                return subdomain, domain, "Bad Request" 
            elif response.status_code == 401:
                return subdomain, domain, "Unauthorized" 
            elif response.status_code == 403:
                return subdomain, domain, "Forbidden" 
            elif response.status_code == 404:
                return subdomain, domain, "Not Found" 
            elif response.status_code == 405:
                return subdomain, domain, "Method Not Allowed" 
            elif response.status_code == 406:
                return subdomain, domain, "Not Acceptable" 
            elif response.status_code == 407:
                return subdomain, domain, "Proxy Authentication Error" 
            elif response.status_code == 408:
                return subdomain, domain, "Request Timeout" 
            elif response.status_code == 409:
                return subdomain, domain, "Conflict" 
            elif response.status_code == 410:
                return subdomain, domain, "Content Missing" 
            elif response.status_code == 418:
                return subdomain, domain, "I am a Teapot" 
            else :
                return subdomain, domain, "Down"
            
        #Checking Server Errors using HTTP response codes 5XX
        elif response.status_code >=500 and response.status_code <600:
            if response.status_code == 500:
                return subdomain, domain, "Internal Server Error" 
            elif response.status_code == 501:
                return subdomain, domain, "Not Implemented" 
            elif response.status_code == 503:
                return subdomain, domain, "Service Unavailable" 
            elif response.status_code == 504:
                return subdomain, domain, "Gateway Timeout" 
            else :
                return subdomain, domain, "Server Error. Down"   
        else:
            return subdomain, domain, "Down"
        
    #SSL Certificate Error
    except requests.exceptions.SSLError:
        return subdomain, domain, "SSL Error"
    
    #Connect Timeout Error
    except requests.exceptions.ConnectTimeout:
        return subdomain, domain, "Connection TimeOut"
    
    #Proxy Error
    except requests.exceptions.ProxyError:
        return subdomain,domain, "Proxy Error"
    
    #Connection Errors
    except requests.exceptions.ConnectionError as ce:
        error_message = str(ce)
        if "NewConnectionError" in error_message:
            return subdomain, domain, "New Connection Error"
        elif "Connection aborted" in error_message:
            return subdomain, domain, "Connection Aborted Error"
        elif "Connection refused" in error_message:
            return subdomain, domain, "Connection Refused Error"
        elif "Connection reset by peer" in error_message:
            return subdomain, domain, "Connection Reset by Peer"
        else:
            return subdomain, domain, "Connection Error"
        
    #HTTP Error
    except requests.exceptions.HTTPError:
        return subdomain,domain, "HTTP Error"
    
    #Redirect Error
    except requests.exceptions.TooManyRedirects:
        return subdomain,domain, "Too Many Redirects Error"
    
    #Request Exception
    except requests.exceptions.RequestException:
        return subdomain, domain, "Error getting Request"

# Function to display the status in tabular format
def display_status(subdomain_status):
    table = tabulate(subdomain_status, headers=["Subdomain", "Domain", "Status"], tablefmt="pretty")
    print(table)

# Sublist3r function to find subdomains
def find_subdomains(domain):
    subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
    return subdomains

# User defined subdomains
def user_subdomains(domain):
    subdomains = []

    while True:
        subdomain = input("Enter subdomain name (i.e www if the website url is www.google.com) /n Enter to Submit ")
        if subdomain == "":
            break
        url = f"{subdomain}.{domain}"
        subdomains.append(url) 

    return subdomains


#main function

if __name__ == "__main__":
    print("Subdomain Monitor. \n\n\n " )
    
    # Choosing between different type of modes for operation. 
    mode = 0 

    while mode != 1 and mode != 2 :
        mode=int(input("Choose Mode: Type 1 for normal mode (Specify subdomains),2 for advanced mode (Automatic Subdomains)  \n "))

    #Domain Name
    if mode==1 :
        print("\n You are now in Normal Mode")
        domain = input("Enter the domain name (e.g., example.com): ")
        available_subdomains = user_subdomains(domain)
    elif mode==2 :
        print("\n You are in Advanced Mode")
        domain = input("Enter the domain name (e.g., example.com): ")
        available_subdomains = find_subdomains(domain)
    else :
        print("Wrong Value Entered")

    #Printing Available Subdomains
    print("Available subdomains:")
    for subdomain in available_subdomains:
        print(str(subdomain))

    # Main loop to continuously check subdomain status
    while True:
        subdomain_status = []
        for subdomain in available_subdomains:
            subdomain_status.append(check_subdomain_status(domain, subdomain))

        display_status(subdomain_status)

        time.sleep(60)  # Wait for 1 minute before the next check
