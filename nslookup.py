import dns.resolver


def nameserverlookup(domain_name):
    """Runs nslookup for domain_name

    :domain_name: Give a hostname, as a string 
    :returns: IP address of host, as string 

    """

    try:
        lookedup = dns.resolver.query(domain_name, 'A')

        addresses = ''
        for data in lookedup:
            addresses = addresses + str(data)

        return addresses
    except dns.resolver.NXDOMAIN:
        return 'nxdomain'

if __name__ == '__main__':
    print(nameserverlookup("www.google.com"))

