#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    ## a list of Alta3 classes
    alta3classes = ['python_basics', 'python_api_design', 'python_for_networking', 'kubernetes', \
      'sip', 'ims', '5g', '4g', 'avaya', 'ansible', 'python_and_ansible_for_network_automation']
      
    ## display the list
    print(alta3classes)

    ## how long is the list? use the built in len function
    ## THEN print (display) the results
    print(len(alta3classes))

    # display python_basics
    print(alta3classes[0])

    # display SIP
    print(alta3classes[4])

    # display Ansible
    print(alta3classes[9])

    ##Uncomment to see a list index out of range error
    #print(alta3classes[99])

    print(alta3classes[0:3])

    print(alta3classes[2:5])

    print(alta3classes[-1])

    testlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    
    print ("last item: testlist[-1]: ", testlist[-1]);
    print ("last 2 items: testlist[-2:]: ", testlist[-2:]);
    print ("everything exception the last 2 items: testlist[:-2]: ", testlist[:-2]);
    print ("all items in the array, reversed: testlist[::-1]: ", testlist[::-1]);
    print ("the 1st 2 items, reversed: testlist[1::-1]: ", testlist[1::-1]);
    print ("thest last 2 items, reversed; testlist[:-3:-1]: ", testlist[:-3:-1]);
    print ("everything except the last 2 items, reversed, testlist[-3::-1]: ", testlist[-3::-1]);

if __name__ == "__main__":
    main()

