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
        #my code - start


        #altitude check
        if(('altitude' in values)):
            values['error'] = 'altitude already exists'
            return values
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
                #return {'error': 'observation is invalid'}
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
            if(int(minutearray[0])<0 or int(minutearray[0])>59):
                values['error'] = 'observation is invalid'
                return values
                #return {'error': 'observation is invalid'}
            if(int(minutearray[1])<0 or int(minutearray[1])>9):
                values['error'] = 'observation is invalid'
                return values
                #return {'error': 'observation is invalid'}
           # print(int(obvarray[0])+int(-1))

        #height validations

        if(not('height' in values)):
            h1=0
            #values['height'] = 0
        else:
            if(values['height']==""):
                values['error'] = 'height is invalid'
                return values
                #return {'error': 'height is invalid'}
            height1=values['height']

            #if(height1.isdigit()==False):
            #    values['error'] = 'height is invalid1'
            #    return values
                #return {'error': 'height is invalid'}

            if(float(values['height']) < 0.0 ):
                values['error'] = 'height is invalid'
                return values
                #return {'error': 'height is invalid'}
            h1=values['height']

        #temperature validations

        if(not('temperature' in values)):
            #values['temperature'] = 72
            t1=72
        else:
            if(values['temperature']==""):
                values['error'] = 'temperature is invalid'
                return values
                #return {'error': 'temperature is invalid'}
            temp=values['temperature']
            #print(temp.isdigit())
            if(temp.isdigit()==False):
                values['error'] = 'temperature is invalid'
                return values
                #return {'error': 'temperature is invalid'}

            if(int(values['temperature']) < -20 or int(values['temperature']) > 120):
                values['error'] = 'temperature is invalid'
                return values
                #return {'error': 'temperature is invalid'}
            t1=values['temperature']

        #pressure validations

        if(not('pressure' in values)):
            #values['pressure'] = 1010
            p1=1010
        else:
            if(values['pressure']==""):
                values['error'] = 'pressure is invalid'
                return values
                #return {'error': 'pressure is invalid'}
            pressure1=values['pressure']
            #print(temp.isdigit())
            if(pressure1.isdigit()==False):
                values['error'] = 'pressure is invalid'
                return values
                #return {'error': 'pressure is invalid'}

            if(int(values['pressure']) < 100 or int(values['pressure']) > 1100):
                values['error'] = 'pressure is invalid'
                return values
                #return {'error': 'pressure is invalid'}
            p1=values['pressure']


        #horizon validations

        if(not('horizon' in values)):
            #values['horizon'] = "natural"
            h2="natural"
        else:

            if(values['horizon']==""):
                values['error'] = 'horizon is invalid'
                return values
                #return {'error': 'horizon is invalid'}

            if(values['horizon'].lower() != "artificial" and values['horizon'].lower() != "natural"):
                values['error'] = 'horizon is invalid'
                return values
                #return {'error': 'horizon is invalid'}
            h2=values['horizon']

        #Calculations
        if(h2.lower() == "natural"):
            dip= (-0.97 * math.sqrt(int(h1))) / 60
        else:
            dip=0
        #print(dip)
        #converttemperature
        tempc=(int(t1)-32.0)*(5/9.0)
        #print(tempc)
        #altitudeconversiontoradians
        minutedegree=float(obvarray[1])/60.0
        totaldegree=float(obvarray[0])+minutedegree
        altituderadian=(totaldegree*3.14)/180.0

        #print (altituderadian)
        refraction=(-0.00452*int(p1)) / (273+tempc)/(math.tan(altituderadian))
        correctedaltitude=totaldegree+dip+refraction
        #print (correctedaltitude)
        newdegree,newminute = divmod(correctedaltitude,1)
        newdegree=int(newdegree)
        #print (newdegree)

        #print (newminute)
        newminute=newminute*60
        #print (newminute)
        correctedminute=round(newminute,1)
        while correctedminute>60.0:
            correctedminute=correctedminute-60.0
            newdegree=newdegree+1

        #print (correctedminute)
        correctedaltitude1=str(newdegree)+"d"+str(correctedminute)
        #print (correctedaltitude1)
        values['altitude']=correctedaltitude1
        #my code - end
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





#sighting = {'op':'correct', 'observation':'015d04.9', 'height':'6.0', 'temperature':'72','pressure':'1010', 'horizon':'artificial'}
#sighting={'observation': '15d04.9', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'temperature': '72'}
#sighting={'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
#result=dispatch(sighting)
#print (result)
