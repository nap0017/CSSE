import urllib

def convertString2Dictionary(inputString = ""):


    String1="0123456789."
    String2="abcdefghijklmnopqrstuvwxyz"
    String3="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    errorDict = {'error':'true'}

    #1 check inputString is null or not
    if inputString == "" :
        return errorDict

    #####Checks
    if "%3D" not in inputString:
        #print ("NO 3D")
        return errorDict
    #2 check valid separator use and alphanumeric check
    counter1=0
    #final1=0

    def remove_space_end(str1):
        str2=str1
        if str1[len(str1)-3]=="%":

            str2=str1[:len(str1)-3]

            str2=remove_space_end(str2)

        return str2

    def remove_space_start(str1):
        str2=str1
        if str1[0]=="%":
            str2=str1[3:]

            str2=remove_space_start(str2)

        return str2

    def first_alpha_check(ch1):

        if ch1 in String2 or ch1 in String3 :
            return 1
        else:
            return 0

    def first_alpha_numeric_check(ch1):

        if ch1 in String1 or ch1 in String2 or ch1 in String3 :
            return 1
        else:
            return 0



    for ch in inputString :

        if ch != "%":
            c1=first_alpha_numeric_check(ch)
            if c1==0:
                #print ("ERROR2")
                return errorDict
        if ch=="%":
            if inputString[counter1:counter1+3] != "%20" and inputString[counter1:counter1+3] != "%3D" and inputString[counter1:counter1+3] != "%2C" and inputString[counter1:counter1+3] != "%2E":
                #print ("ERROR3")
                return errorDict

        counter1=counter1+1

    #3 check whether key or value contains spaces
    for x in inputString.split("%2C"):
        for y in x.split("%3D"):
            if "%20" in y :
                r=remove_space_start(y)
                #print (r)
                if "%20" in r :
                    s=remove_space_end(r)
                    #print (s)
                    if "%20" in s :
                        #print("Key or Value contains white spaces")
                        return errorDict


    #4 Remove White Spaces
    inputstring1=inputString.replace("%20","")

    #5 Check for Key first letter
    counter=0
    counter2=0
    counter3=0
    for ch in inputstring1 :
        if counter == counter3:
            c1=first_alpha_check(ch)
            if c1==0:
                #print ("ERROR1")
                return errorDict
                #print(ch)
                #print(counter)
        if ch == "%":
            if inputstring1[counter:counter+3] != "%20" and inputstring1[counter:counter+3] != "%3D" and inputstring1[counter:counter+3] != "%2C" and inputstring1[counter:counter+3] != "%2E":
                #print("ERROR-Not Valid Separator")
                return errorDict
            else:
                if inputstring1[counter:counter+3] == "%2C" :
                    counter3 = counter+3
        counter=counter+1


    #6 Check missing key or value
    #keys1=[]
    for x in inputstring1.split("%2C"):
        for y in x.split("%3D"):
            if y =="":
                #print("Value Missing")
                return errorDict

    #7 Check for duplicate key
    keys=[]
    i=0
    k=0
    j=0
    for x in inputstring1.split("%2C"):
        for y in x.split("%3D"):
            keys.append(y)
            break

    for i in range(len(keys)-1):
        k=i
        for j in range(len(keys)-1-i):
            if keys[i]==keys[k+1] :
                #print("Duplicate")
                return errorDict
                break
            k=k+1



    x_dict=dict(x.split("%3D") for x in inputstring1.split("%2C"))

    return x_dict

#answer=convertString2Dictionary("a123%3Dabcd")
#print (answer)
