import pandas as pd
import urllib.parse as url

initial_date = '01.01.2019'
second_date = '01.01.2021'
final_date = '0'
final_date_forecast = 'd+7'

start_date = [initial_date, second_date]
end_date = [second_date, final_date]

def fetch_skm_data(symbol, columnNames, start_date = start_date, end_date = end_date):
    
    data = pd.DataFrame()
    
    for date, end in zip(start_date, end_date):
        request = {
            "series": ','.join(symbol),
            'interval': 'hour',
            'start': date,
            'end': end,
            'token': 'KFrEUXu9EhCdkKW',
            'emptydata': 'yes',
            'currency': 'SEK',
            'dateFormat': 'nbno',
            'numberFormat': 'nothousandsdot',
            'fileformat': 'csv',
            'headers': 'no'
        }
        dataUrl = f'https://syspower5.skm.no/api/webquery/execute?{url.urlencode(request)}'
        subset = pd.read_csv(dataUrl, sep=';', index_col=0, parse_dates=True, dayfirst=True, \
                       header=None, names = ['Date'] + columnNames)
        data = pd.concat([data, subset], ignore_index=False)
        
        data = data[~data.index.duplicated(keep='first')]
        
    print("Missing values in " + str(data.columns) + " : " + str(data.isna().sum().sum()))
    return data


# -- Nord Pool
def getSpotPrice(symbol = ['SPOTSE3']):
    return fetch_skm_data(symbol, ['spotPrice'] )

#Hourly!
def getProductionGWh(symbol = ['PROSE1', 'PROSE2', 'PROSE3', 'PROSE4', 'PROSE']):
    return fetch_skm_data(symbol, ['ProductionSE1GWh', 'ProductionSE2GWh', 'ProductionSE3GWh', 'ProductionSE4GWh', 'ProductionALLGWh'])
def getConsumptionGWh(symbol = ['CNPSE1', 'CNPSE2', 'CNPSE3', 'CNPSE4', 'CNPSE']):
    return fetch_skm_data(symbol, ['ConsumptionSE1GWh','ConsumptionSE2GWh','ConsumptionSE3GWh','ConsumptionSE4GWh', 'ConsumptionALLGWh'])

def getTransmissionCapTo(symbol = ['Transmission#Cap#DK1SE3', 'Transmission#Cap#NO1SE3', 
                                   'Transmission#Cap#SE2SE3', 'Transmission#Cap#FISE3', 
                                   'Transmission#Cap#SE4SE3', 'Transmission#Cap#SE3LSSE3']):
    
    return fetch_skm_data(symbol, ['TDK1SE3', 'TNO1SE3', 'TSE2SE3', 'TF1SE3', 'TSE4SE3', 'TLSE3SE3'] )

def getCapacityTo(symbol = ['SCAPSE2SE3', 'SCAPDK1SE3', 'SCAPFISE3', 'SCAPSE4SE3']):
    return fetch_skm_data(symbol, ['SE2SE3', 'DK1SE3', 'FISE3', 'SE4SE3'] )

def getOtherNordPoolData(symbol = ['EXHSE', 'EXHSE2_SE3', 'EXHSE4_SE3', 'REGSE3', 'TOVERSE3_SK']):
    
    return fetch_skm_data(symbol, ['ExchangeSweden(GWh)', 'ExchangeSE2>SE3(GWh)', 'ExchangeSE4>SE3(GWh)', 'ReguSE3(EUR_MWh)', 'TurnoverSE3(MWh)'])
# --

# -- Svenska Kraftnät
def getAllSE1ProductionMWh(symbol = ['PROSE1WAT', 'PROSE1WINDON_ENTSOE', 'PROSE1SOL', 'PROSE1TRM', 'PROSE1OTH']):
    return fetch_skm_data(symbol, ['waterSE1(MWh)', 'windSE1(MWh)', 'solSE1MWh', 'trmSE1MWh', 'OthSE1MWh'] )
def getAllSE2ProductionMWh(symbol = ['PROSE2WAT', 'PROSE2WINDON_ENTSOE', 'PROSE2SOL', 'PROSE2TRM', 'PROSE2OTH']):
    return fetch_skm_data(symbol, ['waterSE2(MWh)', 'windSE2(MWh)', 'solSE2MWh', 'trmSE2MWh', 'OthSE2MWh'] )

def getAllSE3ProductionMWh(symbol = ['PROSE3WAT', 'PROSE3WINDON_ENTSOE', 'PROSE3NUC', 'PROSE3SOL', 'PROSE3TRM', 'PROSE3OTH']):
    return fetch_skm_data(symbol, ['waterSE3(MWh)', 'windSE3(MWh)', 'nucSE3(MWh)', 'solSE3MWh', 'trmSE3MWh', 'OthSE3MWh'] )
def getAllSE4ProductionMWh(symbol = ['PROSE4WAT', 'PROSE4WINDON_ENTSOE', 'PROSE4SOL', 'PROSE4TRM', 'PROSE4OTH']):
    return fetch_skm_data(symbol, ['waterSE4(MWh)', 'windSE4(MWh)', 'solSE4MWh', 'trmSE4MWh', 'OthSE4MWh'] )
# --

# -- SMHI  
# (FROM STOCKHOLM)
def getDailyWeather_sthlm(symbol = ['TEMPSTO;DAY', 'PRECSTO;DAY']):
    return fetch_skm_data(symbol, ['Temperature(day)', 'Precipitation(day)'])

def getDailyWeather(symbol = ['TEMPSE;DAY', 'PENSE;DAY', 'PENNO;DAY', 'PENFI;DAY']):
    return fetch_skm_data(symbol, ['Temperature(day)', 'PrecipitationEnergySE(day)', 'PrecipitationEnergyNO(day)', 'PrecipitationEnergyFI(day)'])

def getDailyWeather_all(symbol = ['TEMPSUND;DAY', 'TEMPFALU;DAY', 'TEMPKARLK;DAY', 'TEMPRONNE;DAY', 'TEMPOSL;DAY', 'TEMPBER;DAY', 'TEMPTRH;DAY', 'TEMPTRM;DAY',
                                  'TEMPKRS;DAY', 'TEMPSTO;DAY', 'TEMPSIRD;DAY', 'TEMPMOS;DAY', 'TEMPFAG;DAY', 'TEMPALTA;DAY', 'TEMPBOD;DAY', 'TEMPKONG;DAY',
                                  'TEMPSELB;DAY', 'TEMPTAFJ;DAY', 'TEMPEIDF;DAY', 'TEMPGOTB;DAY', 'TEMPKATT;DAY', 'TEMPMLMS;DAY', 'TEMPVAX;DAY', 'TEMPRITS;DAY', 
                                  'TEMPGUNN;DAY', 'TEMPOSTE;DAY', 'TEMPLUND;DAY', 'TEMPSTAV;DAY', 'TEMPVENA;DAY', 'TEMPSAUD;DAY', 'TEMPMALU;DAY', 'TEMPFORD;DAY', 
                                  'TEMPARH;DAY', 'TEMPHEL;DAY', 'TEMPCOP;DAY', 'TEMPBARDU;DAY', 'TEMPVISBY;DAY', 'TEMPSARN;DAY', 'TEMPHAPA;DAY', 'TEMPKARE;DAY', 
                                  'TEMPFRAN;DAY', 'TEMPBERL;DAY', 'TEMPPUD;DAY', 'TEMPSODA;DAY']):
    
    return fetch_skm_data(symbol, ['TEMPSUND;DAY', 'TEMPFALU;DAY', 'TEMPKARLK;DAY', 'TEMPRONNE;DAY', 'TEMPOSL;DAY', 'TEMPBER;DAY', 'TEMPTRH;DAY', 'TEMPTRM;DAY', 
                                   'TEMPKRS;DAY', 'TEMPSTO;DAY', 'TEMPSIRD;DAY', 'TEMPMOS;DAY', 'TEMPFAG;DAY', 'TEMPALTA;DAY', 'TEMPBOD;DAY', 'TEMPKONG;DAY', 
                                   'TEMPSELB;DAY', 'TEMPTAFJ;DAY', 'TEMPEIDF;DAY', 'TEMPGOTB;DAY', 'TEMPKATT;DAY', 'TEMPMLMS;DAY', 'TEMPVAX;DAY', 'TEMPRITS;DAY', 
                                   'TEMPGUNN;DAY', 'TEMPOSTE;DAY', 'TEMPLUND;DAY', 'TEMPSTAV;DAY', 'TEMPVENA;DAY', 'TEMPSAUD;DAY', 'TEMPMALU;DAY', 'TEMPFORD;DAY', 
                                   'TEMPARH;DAY', 'TEMPHEL;DAY', 'TEMPCOP;DAY', 'TEMPBARDU;DAY', 'TEMPVISBY;DAY', 'TEMPSARN;DAY', 'TEMPHAPA;DAY', 'TEMPKARE;DAY',
                                   'TEMPFRAN;DAY', 'TEMPBERL;DAY', 'TEMPPUD;DAY', 'TEMPSODA;DAY'] )
#--a

# -- Svensk Energi
def getWeeklyHydroReservs(symbol = ['WATSE;WEEK', 'WATSE3;WEEK']):
    return fetch_skm_data(symbol, ['HydroRes(GWh_week)', 'HydroResSE3(GWh_week)'] )
#--

# -- EEX, ENTSOE
def getHourlyProduction_Germany_all(symbol = ['PRODEWINDON_ENTSOE', 'PRODESOL', 'PRODEGEOTHM_ENTSOE', 'PRODEBIO_ENTSOE', 'PRODEHCL_ENTSOE', 
                                          'PRODEGAS_ENTSOE', 'PRODEOIL_ENTSOE', 'PRODELIG_ENTSOE', 'PRODENUC_ENTSOE', 'CNPDEPUMP_ENTSOE'
                                          , 'PRODERNO_ENTSOE', 'PRODEWASTE_ENTSOE', 'PRODESOL_ENTSOE']):
    return fetch_skm_data(symbol, ['wind(Mwh)', 'solar(Mwh)', 'trm(Mwh)', 'biomass(Mwh)', 'coal(MWh)', 
                                   'gas(MWh)', 'oil(MWh)', 'lignite(MWh)', 'nuc(MWh)', 'pump(MWh)',
                                   'other(MWh)', 'waste(MWh)', 'sol(MWh)'] )
    
def getHourlyProduction_nuclear_EU(symbol = ['PROFINUC_ENTSOE', 'PRODENUC_ENTSOE']):
    return fetch_skm_data(symbol, ['nucFI(MWh)', 'nucDE(MWh)'] )
# --

# -- Metno
def getHourlyTempAll(symbol = ['TEMPVALDRES', 'TEMPVIKSND', 'TEMPTYNSET', 'TEMPUVDAL', 'TEMPSTANGE', 
                               'TEMPSTEINKJR', 'TEMPHONFSS', 'TEMPMOSJ', 'TEMPSVOLVR', 'TEMPHAMRFST', 
                               'TEMPHARSTD', 'TEMPARNDL', 'TEMPBO', 'TEMPFLORO', 'TEMPSANDFJ', 
                               'TEMPALESND', 'TEMPDRAMN', 'TEMPHAMAR', 'TEMPNOTODN', 'TEMPLHMR', 'TEMPFAG', 
                               'TEMPOSL', 'TEMPKONG', 'TEMPMELS', 'TEMPSARP', 'TEMPFJER', 'TEMPBUHLM', 
                               'TEMPGEILO', 'TEMPMOL', 'TEMPVIGR', 'TEMPTAFJ', 'TEMPVENA', 'TEMPSGNDL', 
                               'TEMPSAUD', 'TEMPKRS', 'TEMPSTAV', 'TEMPBER', 'TEMPKRSU', 'TEMPSUNN', 
                               'TEMPRORO', 'TEMPTRH', 'TEMPNMS', 'TEMPMAJA', 'TEMPBOD', 'TEMPTRM', 'TEMPALTA', 
                               'TEMPSLT', 'TEMPFORDE', 'TEMPRENA']):
    return fetch_skm_data(symbol, ['TEMPVALDRES', 'TEMPVIKSND', 'TEMPTYNSET', 'TEMPUVDAL', 'TEMPSTANGE', 
                               'TEMPSTEINKJR', 'TEMPHONFSS', 'TEMPMOSJ', 'TEMPSVOLVR', 'TEMPHAMRFST', 
                               'TEMPHARSTD', 'TEMPARNDL', 'TEMPBO', 'TEMPFLORO', 'TEMPSANDFJ', 
                               'TEMPALESND', 'TEMPDRAMN', 'TEMPHAMAR', 'TEMPNOTODN', 'TEMPLHMR', 'TEMPFAG', 
                               'TEMPOSL', 'TEMPKONG', 'TEMPMELS', 'TEMPSARP', 'TEMPFJER', 'TEMPBUHLM', 
                               'TEMPGEILO', 'TEMPMOL', 'TEMPVIGR', 'TEMPTAFJ', 'TEMPVENA', 'TEMPSGNDL', 
                               'TEMPSAUD', 'TEMPKRS', 'TEMPSTAV', 'TEMPBER', 'TEMPKRSU', 'TEMPSUNN', 
                               'TEMPRORO', 'TEMPTRH', 'TEMPNMS', 'TEMPMAJA', 'TEMPBOD', 'TEMPTRM', 'TEMPALTA', 
                               'TEMPSLT', 'TEMPFORDE', 'TEMPRENA'])
# --


# -- PAST + FORECASTING DATA UMM

def getStationCapForecast(symbol = ['Station#Cap#9297', 'Station#Cap#9309', 'Station#Cap#8007', 'Station#Cap#9280', 'Station#Cap#9282', 'Station#Cap#9421', 
                                    'Station#Cap#9343', 'Station#Cap#2983', 'Station#Cap#12422', 'Station#Cap#10222', 'Station#Cap#9377', 'Station#Cap#12831', 
                                    'Station#Cap#12833', 'Station#Cap#8016', 'Station#Cap#9284', 'Station#Cap#9286', 'Station#Cap#8011', 'Station#Cap#9288', 
                                    'Station#Cap#9290', 'Station#Cap#9292', 'Station#Cap#9401', 'Station#Cap#9415', 'Station#Cap#12717', 
                                    'Station#Cap#3472', 'Station#Cap#3475', 'Station#Cap#9426', 'Station#Cap#3594', 
                                    'Station#Cap#9434']):
    return fetch_skm_data(symbol, ['sCapAros', 'sCapBravallaverket', 'sCapForsmarkB1', 'sCapForsmarkB2', 'sCapForsmarkB3', 'sCapFyrisKraftvarmeverk', 
                                   'sCapHändeloverket', 'sCapHoljes', 'sCapJadraasHallasen', 'sCapKarskarG4', 'sCapMarviken', 'sCapMalarberget', 
                                   'sCapNysater', 'sCapOskarshamn1', 'sCapOskarshamn2', 'sCapOskarshamn3', 'sCapRinghalsB1', 'sCapRinghalsB2', 
                                   'sCapRinghalsB3', 'sCapRinghalsB4',  'sCapRyaKVV', 'sCapStenungsund', 'sCapSvartnas', 
                                   'sCapTrollhattan', 'sCapTrangslet', 'sCapVartan', 'sCapAlvkarleby', 
                                   'sCapAbyverket'], start_date=start_date, end_date=[second_date, final_date_forecast])

    

# Example usage
# test = data_extractor(['PROSE3'], ['ProductionGWh'], '01.01.2021')
# print(test.describe())
