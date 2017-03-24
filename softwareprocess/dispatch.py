import math

def dispatch(values=None):

    String1="0123456789"
    String2=".0123456789"
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
                obvarray.append(x)
            if(obvarray[0]==""):
                values['error'] = 'observation is invalid'
                return values
            if(obvarray[1]==""):
                values['error'] = 'observation is invalid'
                return values
            for ch in obvarray[0]:
                if(ch not in String1):
                    values['error'] = 'observation is invalid'
                    return values

            if(int(obvarray[0])>=int(90) or int(obvarray[0])<0 ):
                values['error'] = 'observation is invalid'
                return values
            if("." not in obvarray[1]):
                values['error'] = 'observation is invalid'
                return values
            minutearray=[]
            for x in obvarray[1].split("."):
                minutearray.append(x)
            if(minutearray[0]==""):
                values['error'] = 'observation is invalid'
                return values
            if(minutearray[1]==""):
                values['error'] = 'observation is invalid'
                return values
            for ch in minutearray[0]:
                if(ch not in String1):
                    values['error'] = 'observation is invalid'
                    return values
            for ch in minutearray[1]:
                if(ch not in String1):
                    values['error'] = 'observation is invalid'
                    return values
            if(int(minutearray[0])<0 or int(minutearray[0])>59):
                values['error'] = 'observation is invalid'
                return values
            if(int(minutearray[1])<0 or int(minutearray[1])>9):
                values['error'] = 'observation is invalid'
                return values

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


            if("." in values['height']):
                for ch in values['height']:
                    if(ch not in String2):
                        values['error'] = 'height is invalid'
                        return values
            else:
                if(height1.isdigit()==False):
                    values['error'] = 'height is invalid'
                    return values

            if(float(values['height']) < 0.0 ):
                values['error'] = 'height is invalid'
                return values
            h1=values['height']

        #temperature validations
        if(not('temperature' in values)):
            t1=72
        else:
            if(values['temperature']==""):
                values['error'] = 'temperature is invalid'
                return values
            temp=values['temperature']
            if(temp.isdigit()==False):
                values['error'] = 'temperature is invalid'
                return values
            if(int(values['temperature']) < -20 or int(values['temperature']) > 120):
                values['error'] = 'temperature is invalid'
                return values
            t1=values['temperature']

        #pressure validations

        if(not('pressure' in values)):
            p1=1010
        else:
            if(values['pressure']==""):
                values['error'] = 'pressure is invalid'
                return values
            pressure1=values['pressure']
            if(pressure1.isdigit()==False):
                values['error'] = 'pressure is invalid'
                return values

            if(int(values['pressure']) < 100 or int(values['pressure']) > 1100):
                values['error'] = 'pressure is invalid'
                return values
            p1=values['pressure']

        #horizon validations
        if(not('horizon' in values)):
            h2="natural"
        else:

            if(values['horizon']==""):
                values['error'] = 'horizon is invalid'
                return values

            if(values['horizon'].lower() != "artificial" and values['horizon'].lower() != "natural"):
                values['error'] = 'horizon is invalid'
                return values
            h2=values['horizon']
        #Calculations
        if(h2.lower() == "natural"):
            dip= (-0.97 * math.sqrt(float(h1))) / 60
        else:
            dip=0

        #converttemperature
        tempc=(int(t1)-32.0)*(5/9.0)

        #altitudeconversiontoradians
        minutedegree=float(obvarray[1])/60.0
        totaldegree=float(obvarray[0])+minutedegree
        altituderadian=(totaldegree*3.14)/180.0
        #print (altituderadian)

        refraction=(-0.00452*int(p1)) / (273+tempc)/(math.tan(altituderadian))
        correctedaltitude=totaldegree+dip+refraction
        newdegree,newminute = divmod(correctedaltitude,1)
        newdegree=int(newdegree)
        newminute=newminute*60
        correctedminute=round(newminute,1)
        while correctedminute>60.0:
            correctedminute=correctedminute-60.0
            newdegree=newdegree+1
        #print (correctedminute)
        correctedaltitude1=str(newdegree)+"d"+str(correctedminute)
        #print (correctedaltitude1)
        values['altitude']=correctedaltitude1

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
