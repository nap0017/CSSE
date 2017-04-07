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
        SHA=['357d41.7','353d14.1','349d38.4','348d54.1','335d25.5','327d58.7','316d41.3','315d16.8','314d13.0','308d37.4','290d47.1','281d10.1','280d31.4','278d29.8','278d10.1','275d44.3','270d59.1','263d54.8','258d31.7','255d10.8','244d57.5','243d25.2','234d16.6','222d50.7','221d38.4','217d54.1','207d41.4','193d49.4','182d31.8','175d50.4','173d07.2','171d58.8','166d19.4','158d29.5','152d57.8','148d45.5','148d05.6','145d54.2','139d49.6','137d03.7','137d21.0','126d09.9','112d24.4','107d25.2','102d10.9','96d20.0','96d05.2','90d45.9','83d41.9','80d38.2','75d56.6','62d06.9','53d17.2','49d30.7','33d45.7','27d42.0','15d22.4','13d51.8','13d36.7']
        declination=['29d10.9','-42d13.4','56d37.7','-17d54.1','-57d09.7','23d32.3','89d20.1','-40d14.8','4d09.0','49d55.1','16d32.3','-8d11.3','46d00.7','6d21.6','28d37.1','-1d11.8','7d24.3','-52d42.5','-16d44.3','-28d59.9','5d10.9','27d59.0','-59d33.7','-43d29.8','-69d46.9','-8d43.8','11d53.2','61d39.5','14d28.9','-17d37.7','-63d10.9','-57d11.9','55d52.1','-11d14.5','49d13.8','-60d26.6','-36d26.6','19d06.2','-60d53.6','-16d06.3','74d05.2','26d39.7','-26d27.8','-69d03.0','-15d44.4','-37d06.6','12d33.1','51d29.3','-34d22.4','38d48.1','-26d16.4','8d54.8','-56d41.0','45d20.5','9d57.0','-46d53.1','-29d32.3','28d10.3','15d17.6']

        #body validations
        if(not('body' in values)):
            values['error'] = 'mandatory information is missing'
            return values
        #star validations
        result_body=checkStar(values['body'])
        if(result_body==-1):
            values['error'] = 'star not in catalog'
            return values

        #date check
        if('date' in values):
            result_date=checkDate(values['date'])
            if(result_date==-1):
                values['error'] = 'invalid date'
                return values
        else:
            date_default='2001-01-01'

        #time check
        if('time' in values):
            result_time=checkTime(values['time'])
            if(result_time==-1):
                values['error'] = 'invalid time'
                return values
        else:
            time_default='00:00:00'



        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values

def checkStar(star):
    name=['Alpheratz','Ankaa','Schedar','Diphda','Achernar','Hamal','Polaris','Akamar','Menkar','Mirfak','Aldebaran','Rigel','Capella','Bellatrix','Elnath','Alnilam','Betelgeuse','Canopus','Sirius','Adara','Procyon','Pollux','Avior','Suhail','Miaplacidus','Alphard','Regulus','Dubhe','Denebola','Gienah','Acrux','Gacrux','Alioth','Spica','Alcaid','Hadar','Menkent','Arcturus','Rigil Kent.','Zubenelg.','Kochab','Alphecca','Antares','Atria','Sabik','Shaula','Rasalhague','Etamin','Kaus Aust.','Vega','Nunki','Altair','Peacock','Deneb','Enif','Alnair','Fomalhaut','Scheat','Markab']
    #SHA=['357d41.7','353d14.1','349d38.4','348d54.1','335d25.5','327d58.7','316d41.3','315d16.8','314d13.0','308d37.4','290d47.1','281d10.1','280d31.4','278d29.8','278d10.1','275d44.3','270d59.1','263d54.8','258d31.7','255d10.8','244d57.5','243d25.2','234d16.6','222d50.7','221d38.4','217d54.1','207d41.4','193d49.4','182d31.8','175d50.4','173d07.2','171d58.8','166d19.4','158d29.5','152d57.8','148d45.5','148d05.6','145d54.2','139d49.6','137d03.7','137d21.0','126d09.9','112d24.4','107d25.2','102d10.9','96d20.0','96d05.2','90d45.9','83d41.9','80d38.2','75d56.6','62d06.9','53d17.2','49d30.7','33d45.7','27d42.0','15d22.4','13d51.8','13d36.7']
    #declination=['29d10.9','-42d13.4','56d37.7','-17d54.1','-57d09.7','23d32.3','89d20.1','-40d14.8','4d09.0','49d55.1','16d32.3','-8d11.3','46d00.7','6d21.6','28d37.1','-1d11.8','7d24.3','-52d42.5','-16d44.3','-28d59.9','5d10.9','27d59.0','-59d33.7','-43d29.8','-69d46.9','-8d43.8','11d53.2','61d39.5','14d28.9','-17d37.7','-63d10.9','-57d11.9','55d52.1','-11d14.5','49d13.8','-60d26.6','-36d26.6','19d06.2','-60d53.6','-16d06.3','74d05.2','26d39.7','-26d27.8','-69d03.0','-15d44.4','-37d06.6','12d33.1','51d29.3','-34d22.4','38d48.1','-26d16.4','8d54.8','-56d41.0','45d20.5','9d57.0','-46d53.1','-29d32.3','28d10.3','15d17.6']
    counter=0
    for x in name:
        if(star==x):
            return counter
        counter=counter+1
    return -1

def checkDate(date):
    counter_date=0

    if(len(date)!=10):
        return -1

    for x in date:
        if(counter_date==4 or counter_date==7):
            if(x!='-'):
                return -1
        else:
            if(x.isdigit()==False):
                return -1
        counter_date=counter_date+1;

    if(int(date[0:4])<2001):
        return -1
    if(int(date[5:2])<0 or int(date[5:2])>12):
        return -1
    if(int(date[8:2])<0 or int(date[8:2])>31):
        return -1

    return 0

def checkTime(time):
    counter_time=0

    if(len(time)!=8):
        return -1

    for x in time:
        if(counter_date==2 or counter_date==5):
            if(x!=':'):
                return -1
        else:
            if(x.isdigit()==False):
                return -1
        counter_date=counter_date+1;

    if(int(time[0:2])<0 or int(time[0:2])>24):
        return -1
    if(int(time[3:2])<0 or int(time[3:2])>60):
        return -1
    if(int(time[6:2])<0 or int(time[6:2])>60):
        return -1

    return 0
