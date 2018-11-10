import subprocess

def nameserverlookup(domain_name):
    """Runs nslookup for domain_name

    :domain_name: Give a hostname, as a string 
    :returns: IP address of host, as string 

    """
    
    lookedup = subprocess.run(["nslookup", domain_name], stdout= subprocess.PIPE)
    return lookedup.stdout.decode("UTF-8") 


if __name__ == '__main__':
    nameserverlookup("www.google.com")

