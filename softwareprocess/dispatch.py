import math
from datetime import datetime, timedelta

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
        if(not(isinstance(values['body'],str))):
            values['error'] = 'invalid body'
            return values

        #long and lat validations
        if(('long' in values)):
            values['error'] = 'invalid input given(long)'
            return values
        if(('lat' in values)):
            values['error'] = 'invalid input given(lat)'
            return values
        #star validations
        result_body=checkStar(values['body'])
        if(result_body==-1):
            values['error'] = 'star not in catalog'
            return values

        #date check
        if('date' in values):
            if(not(isinstance(values['date'],str))):
                values['error'] = 'invalid date'
                return values

            result_date=checkDate(values['date'])
            if(result_date==-1):
                values['error'] = 'invalid date'
                return values
        else:
            date_default='2001-01-01'

        #time check
        if('time' in values):
            if(not(isinstance(values['time'],str))):
                values['error'] = 'invalid time'
                return values

            result_time=checkTime(values['time'])
            if(result_time==-1):
                values['error'] = 'invalid time'
                return values
        else:
            time_default='00:00:00'

        #Calculations
        latitude=declination[result_body]
        values['lat']=latitude
        star_SHA=SHA[result_body]
        #print(star_SHA)
        #2.a cumulative_progression
        reference_year='2001'
        reference_GHA='100d42.6'
        if('date' in values):
            observation_date=values['date']
        else:
            observation_date=date_default

        observation_year=observation_date[0:4]
        #print(observation_year)
        diff_year=int(observation_year)-int(reference_year)
        #print(diff_year)
        decrease_GHA='0d14.31667'
        cumulative_progression=calculateCumulativeProgression(decrease_GHA,diff_year)
        #print (cumulative_progression)
        #2.b leap years and total progression
        ref_leap=int(reference_year)+1
        ref_observation=int(observation_year)
        leap_counter=0
        while ref_leap<ref_observation:
            if(ref_leap%4==0):
                leap_counter=leap_counter+1
            ref_leap=ref_leap+1
        #print(leap_counter)
        rotational_period=86164.1
        clock_period=86400
        daily_rotation=abs((360.0*60*60)-(rotational_period/clock_period)*(360.0*60*60))
        daily_rotation=daily_rotation/60.0
        #print (daily_rotation)
        total_progression=calculateTotalProgression(daily_rotation,leap_counter)
        #print (total_progression)
        #2.c calculate current GHA
        current_GHA=calculateCurrentGHA(reference_GHA,cumulative_progression,total_progression)
        #print (current_GHA)
        if('time' in values):
            observation_time=values['time']
        else:
            observation_time=time_default
        #2.d earth rotation
        date_a=observation_date
        date_b=observation_year+'-01-01'
        date_a=date_a+'T'+observation_time+'Z'
        date_b=date_b+'T'+'00:00:00'+'Z'
        date_1 = datetime.strptime(date_a, '%Y-%m-%dT%H:%M:%SZ')
        date_2 = datetime.strptime(date_b, '%Y-%m-%dT%H:%M:%SZ')


        timedelta = abs(date_1-date_2)
        #print (timedelta)
        timedelta = timedelta.total_seconds()
        #print(timedelta)

        amount_rotation=(timedelta/86164.1)
        int_amount_rotation=int(amount_rotation)
        #print (int_amount_rotation)
        amount_rotation=amount_rotation-int_amount_rotation
        #print (amount_rotation)
        amount_rotation=amount_rotation*360.0
        int_amount_rotation=int(amount_rotation)
        amount_rotation1=int_amount_rotation

        #print (int_amount_rotation)
        amount_rotation=amount_rotation-int_amount_rotation
        #print (amount_rotation)
        int_amount_rotation=amount_rotation*60
        #print (int_amount_rotation)
        int_amount_rotation=round(int_amount_rotation,1)
        #print (int_amount_rotation)
        total_amount_rotation=str(amount_rotation1)+'d'+str(int_amount_rotation)
        #print (total_amount_rotation)
        #2.e calculate total
        total_GHA=calculateTotalGHA(current_GHA,total_amount_rotation)

        #3.C star GHA
        star_new_GHA=calculateStarNewGHA(total_GHA,star_SHA)

        #clean up
        array_star=[]
        for x in star_new_GHA.split('d'):
            array_star.append(x)
        d_star=int(array_star[0])

        while d_star>360:
            d_star=d_star-360
        final_answer=str(d_star)+'d'+str(array_star[1])

        values['long']=final_answer

        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):

        #mandatory validations
        if(not(('lat' in values) and ('long' in values)  and ('altitude' in values) and ('assumedLat' in values) and ('assumedLong' in values)) ):
            values['error'] = 'mandatory information is missing'
            return values

        if('correctedDistance' in values):
            values['error'] = 'invalid input correctedDistance'
            return values

        if('correctedAzimuth' in values):
            values['error'] = 'invalid input correctedAzimuth'
            return values


        #lat validations
        if(not(isinstance(values['lat'],str))):
            values['error'] = 'invalid lat'
            return values

        result_lat=checkLat(values['lat'])
        if(result_lat==-1):
            values['error'] = 'invalid lat'
            return values


        #long validations
        if(not(isinstance(values['long'],str))):
            values['error'] = 'invalid long'
            return values
        result_long=checkLong(values['long'])
        if(result_long==-1):
            values['error'] = 'invalid long'
            return values


        #altitude validations
        if(not(isinstance(values['altitude'],str))):
            values['error'] = 'invalid altitude'
            return values

        result_altitude=checkLong(values['altitude'])
        if(result_altitude==-1):
            values['error'] = 'invalid altitude'
            return values


        #assumedLat validations
        if(not(isinstance(values['assumedLat'],str))):
            values['error'] = 'invalid assumedLat'
            return values

        result_assumedlat=checkLat(values['assumedLat'])
        if(result_assumedlat==-1):
            values['error'] = 'invalid assumedlat'
            return values


        #assumedLong validations
        if(not(isinstance(values['assumedLong'],str))):
            values['error'] = 'invalid assumedLong'
            return values


        result_assumedlong=checkLong(values['assumedLong'])
        if(result_assumedlong==-1):
            values['error'] = 'invalid assumedlong'
            return values

        correct_long= values['long']
        correct_assumedlong=values['assumedLong']

        correct_lat=values['lat']
        correct_assumedlat=values['assumedLat']
        correct_altitude = values['altitude']
        LHA = calculateStarNewGHA(correct_long,correct_assumedlong)

        rad_lat=convertradian(correct_lat)
        rad_alat=convertradian(correct_assumedlat)
        rad_LHA=convertradian(LHA)
        intermediateDistance = ((math.sin(convertradian(correct_lat))*math.sin(convertradian(correct_assumedlat)))
                                +(math.cos(convertradian(correct_lat))*math.cos(convertradian(correct_assumedlat))*math.cos(convertradian(LHA))))
        #print  intermediateDistance
        correct_correctedaltitude = math.asin(intermediateDistance)
        correct_correctedaltitude = round(correct_correctedaltitude,4)
        correct_correctedaltitude = (correct_correctedaltitude * 180.0)/(math.pi)
        int_correctedaltitude = int(correct_correctedaltitude)
        float_correctedaltitude = (correct_correctedaltitude - int_correctedaltitude)*60.0
        if(float(float_correctedaltitude)<float(0.0)):
            float_correctedaltitude = float(float_correctedaltitude) * float(-1)

        int_correctedaltitude = int(int_correctedaltitude) * int(-1)

        correct_correctedaltitude = str(int_correctedaltitude)+"d"+str(float_correctedaltitude)
        #correct_correctedaltitude = "52d07.8"
        corrected_distance = calculateStarNewGHA(correct_altitude,str(correct_correctedaltitude))
        array=[]
        for x in corrected_distance.split("d"):
            array.append(x)

        corrected_distance = (float(array[0])*60)+ float(array[1])
        corrected_distance = int(round(corrected_distance,1))

        values['correctedDistance'] = str(corrected_distance)
        #print corrected_distance



        corrected_azimuth = math.acos((math.sin(rad_lat)- (math.sin(rad_alat)*intermediateDistance))/(math.cos(rad_alat)*math.cos(math.asin(intermediateDistance))))

        corrected_azimuth = (corrected_azimuth * 180.0)/math.pi
        int_corrected_azimuth = int(corrected_azimuth)
        float_corrected_azimuth = (corrected_azimuth - int_corrected_azimuth)*60.0
        if(float(float_corrected_azimuth)<float(0.0)):
            float_corrected_azimuth = float(float_corrected_azimuth) * float(-1)

        float_corrected_azimuth=round(float_corrected_azimuth,1)
        corrected_azimuth = str(int_corrected_azimuth)+"d"+str(float_corrected_azimuth)

        values['correctedAzimuth'] = str(corrected_azimuth)


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
        if(star.lower()==x.lower()):
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
    if((int(date[5:7])<int(0)) or (int(date[5:7])>int(12))):
        return -1
    if(int(date[8:10])<0 or int(date[8:10])>31):
        return -1
    if(int(date[5:7])==int(2) or int(date[5:7])==int(4) or int(date[5:7])==int(6) or int(date[5:7])==int(9) or int(date[5:7])==int(11)):
        if(int(date[8:10])<0 or int(date[8:10])>30):
            return -1
        if(int(date[5:7])==int(2) and (int(date[8:10])>29) and (int(date[0:4])%4==0)):
            return -1
        if(int(date[5:7])==int(2) and (int(date[8:10])>28) and (int(date[0:4])%4!=0) ):
            return -1

    return 0

def checkTime(time):
    counter_time=0

    if(len(time)!=8):
        return -1

    for x in time:
        if(counter_time==2 or counter_time==5):
            if(x!=':'):
                return -1
        else:
            if(x.isdigit()==False):
                return -1
        counter_time=counter_time+1;

    if(int(time[0:2])<0 or int(time[0:2])>24):
        return -1
    if(int(time[3:5])<0 or int(time[3:5])>60):
        return -1
    if(int(time[6:8])<0 or int(time[6:8])>60):
        return -1

    return 0

def calculateCumulativeProgression(GHA,year):
    d_GHA=GHA[0:2]
    m_GHA=GHA[2:]
    m_GHA=float(m_GHA)
    #print (m_GHA)
    year=int(year)
    degree=0
    total=year*m_GHA
    #print(total)
    while total>60.0:
        total=total-60.0
        degree=degree+1
    total=round(total,1)
    #print (total)
    result='-'+str(degree)+'d'+str(total)
    return result


def calculateTotalProgression(rotation,year):

    year=float(year)
    degree=0
    total=year*rotation

    while total>60.0:
        total=total-60.0
        degree=degree+1

    total=round(total,1)
    result=str(degree)+'d'+str(total)
    return result

def calculateCurrentGHA(rg,cp,lp):


    array_rg=[]
    for x in rg.split('d'):
        array_rg.append(x)
    array_cp=[]
    for x in cp.split('d'):
        array_cp.append(x)
    array_lp=[]
    for x in lp.split('d'):
        array_lp.append(x)

    degree=int(array_rg[0])+int(array_cp[0])+int(array_lp[0])
    if(rg[0]=='-'):
        array_rg[1]='-'+array_rg[1]
    if(cp[0]=='-'):
        array_cp[1]='-'+array_cp[1]
    if(lp[0]=='-'):
        array_lp[1]='-'+array_lp[1]

    total=float(array_rg[1])+float(array_cp[1])+float(array_lp[1])
    total=total/60.0
    degree=degree+total
    int_degree=int(degree)
    float_degree=degree-int_degree
    float_degree=float_degree*60.0
    float_degree=round(float_degree,1)

    result=str(int_degree)+'d'+str(float_degree)
    return result

def calculateTotalGHA(cg,ta):


    array_cg=[]
    for x in cg.split('d'):
        array_cg.append(x)
    array_ta=[]
    for x in ta.split('d'):
        array_ta.append(x)


    degree=int(array_cg[0])+int(array_ta[0])
    if(cg[0]=='-'):
        array_cg[1]='-'+array_cg[1]
    if(ta[0]=='-'):
        array_ta[1]='-'+array_ta[1]


    total=float(array_cg[1])+float(array_ta[1])
    total=total/60.0
    degree=degree+total
    int_degree=int(degree)
    float_degree=degree-int_degree
    float_degree=float_degree*60.0
    float_degree=round(float_degree,1)

    result=str(int_degree)+'d'+str(float_degree)
    return result


def calculateStarNewGHA(cg,ta):


    array_cg=[]
    for x in cg.split('d'):
        array_cg.append(x)
    array_ta=[]
    for x in ta.split('d'):
        array_ta.append(x)

    degree=int(array_cg[0])+int(array_ta[0])
    if(cg[0]=='-'):
        array_cg[1]='-'+array_cg[1]
    if(ta[0]=='-'):
        array_ta[1]='-'+array_ta[1]


    total=float(array_cg[1])+float(array_ta[1])
    total=total/60.0
    degree=degree+total
    int_degree=int(degree)
    float_degree=degree-int_degree
    float_degree=float_degree*60.0
    float_degree=round(float_degree,1)

    result=str(int_degree)+'d'+str(float_degree)
    return result


def checkLat(lat):

    latitude=lat
    if("d" not in latitude):
        return -1
    latitudearray=[]
    for x in latitude.split("d"):
        latitudearray.append(x)
    if(latitudearray[0]==""):
        return -1
    if(latitudearray[1]==""):
        return -1
    if(latitudearray[0][0:1]=="-"):
       if(latitudearray[0][1:].isdigit()==False):
            return -1
    else:
        if(latitudearray[0].isdigit()==False):
            return -1
    if(int(latitudearray[0])>int(89) or int(latitudearray[0])<int(-89) ):
        return -1
    if("." not in latitudearray[1]):
        return -1
    minutearray=[]
    for x in latitudearray[1].split("."):
        minutearray.append(x)


    if(minutearray[0]==""):
        return -1
    if(minutearray[1]==""):
        return -1

    if(minutearray[0].isdigit()==False):
        return -1
    if(minutearray[1].isdigit()==False):
        return -1

    if(int(minutearray[0])<0 or int(minutearray[0])>59):
        return -1
    if(int(minutearray[1])<0 or int(minutearray[1])>9):
        return -1

    return 0


def checkLong(long):

    longitude=long
    if("d" not in longitude):
        return -1
    longitudearray=[]
    for x in longitude.split("d"):
        longitudearray.append(x)
    if(longitudearray[0]==""):
        return -1
    if(longitudearray[1]==""):
        return -1
    if(longitudearray[0][0:1]=="-"):
       if(longitudearray[0][1:].isdigit()==False):
            return -1
    else:
        if(longitudearray[0].isdigit()==False):
            return -1
    if(int(longitudearray[0])>int(359) or int(longitudearray[0])<int(0) ):
        return -1
    if("." not in longitudearray[1]):
        return -1
    minutearray=[]
    for x in longitudearray[1].split("."):
        minutearray.append(x)


    if(minutearray[0]==""):
        return -1
    if(minutearray[1]==""):
        return -1

    if(minutearray[0].isdigit()==False):
        return -1
    if(minutearray[1].isdigit()==False):
        return -1

    if(int(minutearray[0])<0 or int(minutearray[0])>59):
        return -1
    if(int(minutearray[1])<0 or int(minutearray[1])>9):
        return -1

    return 0


def checkAltitude(alt):

    altitude=alt
    if("d" not in altitude):
        return -1
    altitudearray=[]
    for x in altitude.split("d"):
        altitudearray.append(x)
    if(altitudearray[0]==""):
        return -1
    if(altitudearray[1]==""):
        return -1
    if(altitudearray[0][0:1]=="-"):
       if(altitudearray[0][1:].isdigit()==False):
            return -1
    else:
        if(altitudearray[0].isdigit()==False):
            return -1
    if(int(altitudearray[0])>int(89) or int(altitudearray[0])<=int(0) ):
        return -1
    if("." not in altitudearray[1]):
        return -1
    minutearray=[]
    for x in altitudearray[1].split("."):
        minutearray.append(x)


    if(minutearray[0]==""):
        return -1
    if(minutearray[1]==""):
        return -1

    if(minutearray[0].isdigit()==False):
        return -1
    if(minutearray[1].isdigit()==False):
        return -1

    if(int(minutearray[0])<0 or int(minutearray[0])>59):
        return -1
    if(int(minutearray[1])<0 or int(minutearray[1])>9):
        return -1

    return 0


def convertradian(alt):

    #convertdegreetoradian
    array=[]
    for x in alt.split("d"):
        array.append(x)


    minutedegree=float(array[1])/60.0
    if(array[0][0:1]=="-"):
        minutedegree=minutedegree*(-1)

    totaldegree=float(array[0])+minutedegree
    radian=(totaldegree*math.pi)/180.0

    return radian


