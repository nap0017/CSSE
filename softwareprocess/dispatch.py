import math

def dispatch(values=None):

    String1="0123456789"
    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        #newCode - Start
        #observation validations
        if(not('observation' in values)):
            values['error'] = 'mandatory information is missing'
            return values
        else:
            obv=""
            obv=values['observation']
            if("d" not in obv):
                values['error'] = 'observation is invalid'
                return values
            obvarray=[]
            for x in obv.split("d"):
                #print(x)
                obvarray.append(x)
            #print(obvarray)
            if(obvarray[0]==""):
                values['error'] = 'observation is invalid'
                return values
                #return {'error': 'observation is invalid'}}
            if(obvarray[1]==""):
                values['error'] = 'observation is invalid'
                return values
                #return {'error': 'observation is invalid'}
            for ch in obvarray[0]:
                if(ch not in String1):
                    values['error'] = 'observation is invalid'
                    return values
                    #return {'error': 'observation is invalid'}

            if(int(obvarray[0])>=int(90) or int(obvarray[0])<0 ):
                values['error'] = 'observation is invalid'
                return values
                #return {'error': 'observation is invalid'}
            if("." not in obvarray[1]):
                values['error'] = 'observation is invalid'
                return values
                #return {'error': 'observation is invalid'}
            minutearray=[]
            for x in obvarray[1].split("."):
                #print(x)
                minutearray.append(x)
            if(minutearray[0]==""):
                values['error'] = 'observation is invalid'
                return values
                #return {'error': 'observation is invalid'}
            if(minutearray[1]==""):
                values['error'] = 'observation is invalid'
                return values
                #return {'error': 'observation is invalid'}
            for ch in minutearray[0]:
                if(ch not in String1):
                    values['error'] = 'observation is invalid'
                    return values
                    #return {'error': 'observation is invalid'}
            for ch in minutearray[1]:
                if(ch not in String1):
                    values['error'] = 'observation is invalid'
                    return values
                    #return {'error': 'observation is invalid'}

        #newCode - End
        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values
