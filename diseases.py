from disease_class import Disease

dislib=[]
def createlib():
    """
    Creates a list of diseases.
    returns: list of Disease objects
    """
    flu=Disease('Influenza',['fever','runny nose','sore throat','muscle ache','joint pain','headache','cough','drowsiness'],Disease.VIR,['air','touch'],40)
    dislib.append(flu)
    alz=Disease('Alzheimer\'s Disease',['amnesia','mental decline','depression','hallucinations','delusions','mood swings'],Disease.MENT,[''],50)
    dislib.append(alz)
    cpx=Disease('Chikenpox',['fever', 'drowsiness', 'loss of appetite','headache','spots','itchiness','blister','rash'], Disease.VIR,['touch','air','saliva',],3.5)
    dislib.append(cpx)
    cvd=Disease('Coronavirus Disease 2019',['fever', 'cough', 'shortness of breath', 'drowsiness', 'muscle aches', 'headache','lost of taste', 'lost of smell', 'sore throat', 'runny nose', 'nausea', 'diarrhea','chest pain'],Disease.VIR,['air','touch'],70)
    dislib.append(cvd)
    srp=Disease('Strep Throat',['sore throat','swollen tonsils','swollen lymph nodes','fever','chills'],Disease.BACT,['air','saliva'],30)
    dislib.append(srp)
    slm=Disease('Salmonella',['diarrhea', 'vomiting', 'muscle cramps'],Disease.BACT,['animal'],13.5)
    dislib.append(slm)
    mal=Disease('Malaria',['fever','chills','shivers','headache','diarrhea','nausea','muscle aches'],Disease.PAR,['insect','blood'],0.02)
    dislib.append(mal)
    dng=Disease('Dengue Fever',['nausea', 'vomiting', 'rash', 'muscle aches', 'bone pain', 'joint pain'],Disease.VIR,['animal'],0.012)
    dislib.append(dng)
    lcn=Disease('Lung Cancer',['chest pain','cough','coughing blood','shortness of breath','swollen lymph nodes', 'weakness', 'fatigue','loss of appetite','weight loss'],Disease.CAN, [],2.2)
    dislib.append(lcn)
    atf=Disease('Athlete\'s Foot',['rash','itchiness','blisters','stinging'],Disease.FUNG,['touch'],30)
    dislib.append(atf)
    tbc=Disease('Tuberculosis',['chest pain','chills','weight loss','fatigue','shortness of breath', 'swollen lymph nodes','loss of appetite'],Disease.BACT,['air'],.1)
    dislib.append(tbc)
    pnk=Disease('Pink Eye',['irratated eyes','dry eyes','eye discharge','itchiness','puffy eyes','congestion'],Disease.BACT,['touch'],60)
    dislib.append(pnk)
    return dislib

