#!/usr/bin/python3
"""Learning about Dictionaries | alta3 research"""

def main():
    """runtime code"""
    hostipdict = {'host01':'10.0.2.3', 'host02':'192.168.3.3', 'host03':'72.4.23.22'}

    ## display the current state of our dictionary
    print(hostipdict)

    ## add another entry to the dict
    hostipdict ['host04'] = '10.23.43.224'

    ## display the dict with the new entry for host4
    print (hostipdict)

    ## rewrite the value for host02
    hostipdict['host02'] = '192.168.70.55'

    ## display the dict wit new entry applied
    print (hostipdict)

    ## recall from the dict
    ## 'host02' should now print to '192.168.70.55'
    print(hostipdict['host02'])

    ## this will cause a key error
    ## toast01 is not a key
   ## print (hostipdict['toast01'])
    print (hostipdict.get('toast01'));
    if __name__ == "__main__":
        main()
