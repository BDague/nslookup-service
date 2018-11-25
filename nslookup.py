import dns.resolver


def nameserverlookup(domain_name):
    """Runs nslookup for domain_name

    :domain_name: Give a hostname, as a string 
    :returns: information about as domain, as dict 

    """
    domain_info = {}

    resolver = dns.resolver.Resolver()

    domain_info['nameservers'] = ",".join(resolver.nameservers)

    domain_info['name'] = domain_name

    try:
        lookedup = dns.resolver.query(domain_name, 'A')

        addresses = ''
        for data in lookedup:
            addresses = addresses + str(data)

        domain_info['addresses'] = addresses 
    except dns.resolver.NXDOMAIN:
        domain_info['addresses'] = None
    
        
    return domain_info

if __name__ == '__main__':
    print(nameserverlookup("www.google.com"))

