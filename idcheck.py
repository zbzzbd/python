import  string

alpahas = string.letters +'_'
nums = string.digits

print 'welcome to the Identifier checker v1.0'
print 'Testees must be at least 2 chars long.'
print alpahas,nums

myInput = raw_input('Identifier to test?')

if len(myInput) > 1:
    if myInput[0] not in alpahas:
        print ''' invalid: first symbol must be alphaabetic'''
    else:
        for otherChar in myInput[1:]:

            if otherChar not in alpahas + nums:
                print ''' invalid: remaining symbols must be alphanumeric '''
                break
        else:
            print "okay as an identifier"


