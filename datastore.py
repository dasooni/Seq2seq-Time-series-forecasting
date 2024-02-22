import pandas as pd
import urllib.parse as url


start_data = '01.01.2021'

def fetch_skm_data(symbol, columnNames, start_date = start_data):
    
    request = {
      "series": ','.join(symbol),
      'interval': 'hour',
      'start': start_date,
      'end': '0',
      'token': 'KFrEUXu9EhCdkKW',
      'emptydata': 'yes',
      'currency': 'SEK',
      'dateFormat': 'nbno',
      'numberFormat': 'nothousandsdot',
      'fileformat': 'csv',
      'headers': 'no'
    }

    dataUrl = f'https://syspower5.skm.no/api/webquery/execute?{url.urlencode(request)}'
    data = pd.read_csv(dataUrl, sep=';', index_col=0, parse_dates=True, dayfirst=True, \
                       header=None, names = ['Date'] + columnNames)
    print("Missing values in " + str(data.columns) + " : " + str(data.isna().sum().sum()))
    # print(data.isna().sum())
    return data


# -- Nord Pool
def getProductionGWh(symbol = ['PROSE3'], start_date = start_data):
    return fetch_skm_data(symbol, ['ProductionGWh'], start_date )
def getConsumptionGWh(symbol = ['CNPSE3'], start_date = start_data):
    return fetch_skm_data(symbol, ['ConsumptionGWh'], start_date )
def getSpotPrice(symbol = ['SPOTSE3'], start_date = start_data):
    return fetch_skm_data(symbol, ['spotPrice'], start_date )

def getTransmissionCapTo(symbol = ['Transmission#Cap#DK1SE3', 'Transmission#Cap#NO1SE3', 
                                   'Transmission#Cap#SE2SE3', 'Transmission#Cap#FISE3', 
                                   'Transmission#Cap#SE4SE3', 'Transmission#Cap#SE3LSSE3'], start_date = start_data):
    
    return fetch_skm_data(symbol, ['TDK1SE3', 'TNO1SE3', 'TSE2SE3', 'TF1SE3', 'TSE4SE3', 'TLSE3SE3'], start_date )

def getCapacityTo(symbol = ['SCAPSE2SE3', 'SCAPDK1SE3', 'SCAPFISE3', 'SCAPSE4SE3'], start_date = start_data):
    return fetch_skm_data(symbol, ['SE2SE3', 'DK1SE3', 'FISE3', 'SE4SE3'], start_date )

def getOtherNordPoolData(symbol = ['EXHSE', 'PROSE', 'CNPSE', 'EXHSE2_SE3', 
                                   'EXHSE4_SE3', 'REGSE3', 'TOVERSE3_SK'] , start_date = start_data):
    
    return fetch_skm_data(symbol, ['ExchangeSweden(GWh)', 'ProductionSweden(GWh)', 'ConsumptionSweden(GWh)', 'ExchangeSE2>SE3(GWh)', 'ExchangeSE4>SE3(GWh)', 
                                   'ReguSE3(EUR_MWh)', 'TurnoverSE3(MWh)'], start_date)
# --

# -- Svenska Kraftnät
def getHydroProductionMWh(symbol = ['PROSE3WAT'], start_date = start_data):
    return fetch_skm_data(symbol, ['waterMWh'], start_date )

def getWindProductionMWh(symbol = ['PROSE3WINDON_ENTSOE'], start_date = start_data):
    return fetch_skm_data(symbol, ['windMWh'], start_date )

def getNuclearProductionMWh(symbol = ['PROSE3NUC'], start_date = start_data):
    return fetch_skm_data(symbol, ['nucMWh'], start_date )

def getSolarProductionMWh(symbol = ['PROSE3SOL'], start_date = start_data):
    return fetch_skm_data(symbol, ['solMWh'], start_date )

def getThermalProductionMWh(symbol = ['PROSE3TRM'], start_date = start_data):
    return fetch_skm_data(symbol, ['trmMWh'], start_date )

def getOtherProductionMWh(symbol = ['PROSE3OTH'], start_date = start_data):
    return fetch_skm_data(symbol, ['OthMWh'], start_date )

def getAllProductionMWh(symbol = ['PROSE3WAT', 'PROSE3WINDON_ENTSOE', 'PROSE3NUC', 'PROSE3SOL', 'PROSE3TRM', 'PROSE3OTH'], start_date = start_data):
    return fetch_skm_data(symbol, ['water(MWh)', 'wind(MWh)', 'nuc(MWh)', 'solMWh', 'trmMWh', 'OthMWh'], start_date )
# --

# -- SMHI  
# (FROM STOCKHOLM)
def getDailyWeather(symbol = ['TEMPSTO;DAY', 'PRECSTO;DAY'], start_date = start_data):
    return fetch_skm_data(symbol, ['Temperature(day)', 'Precipitation(day)'], start_date)
#--

# -- Svensk Energi
def getWeeklyHydroReservs(symbol = ['WATSE;WEEK', 'WATSE3;WEEK'], start_date = start_data):
    return fetch_skm_data(symbol, ['HydroRes(GWh_week)', 'HydroResSE3(GWh_week)'], start_date )
#--

# -- EEX, ENTSOE
def getHourlyProduction_Germany(symbol = ['PRODEWINDON_ENTSOE', 'PRODESOL', 'PRODEGEOTHM_ENTSOE', 'PRODEBIO_ENTSOE', 'PRODEHCL_ENTSOE', 
                                          'PRODEGAS_ENTSOE', 'PRODEOIL_ENTSOE', 'PRODELIG_ENTSOE', 'PRODENUC_ENTSOE', 'CNPDEPUMP_ENTSOE'
                                          , 'PRODERNO_ENTSOE', 'PRODEWASTE_ENTSOE', 'PRODESOL_ENTSOE'], start_date = start_data):
    return fetch_skm_data(symbol, ['wind(Mwh)', 'solar(Mwh)', 'trm(Mwh)', 'biomass(Mwh)', 'coal(MWh)', 
                                   'gas(MWh)', 'oil(MWh)', 'lignite(MWh)', 'nuc(MWh)', 'pump(MWh)',
                                   'other(MWh)', 'waste(MWh)', 'sol(MWh)'], start_date )
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
                               'TEMPSLT', 'TEMPFORDE', 'TEMPRENA'], start_date = start_data):
    return fetch_skm_data(symbol, ['TEMPVALDRES', 'TEMPVIKSND', 'TEMPTYNSET', 'TEMPUVDAL', 'TEMPSTANGE', 
                               'TEMPSTEINKJR', 'TEMPHONFSS', 'TEMPMOSJ', 'TEMPSVOLVR', 'TEMPHAMRFST', 
                               'TEMPHARSTD', 'TEMPARNDL', 'TEMPBO', 'TEMPFLORO', 'TEMPSANDFJ', 
                               'TEMPALESND', 'TEMPDRAMN', 'TEMPHAMAR', 'TEMPNOTODN', 'TEMPLHMR', 'TEMPFAG', 
                               'TEMPOSL', 'TEMPKONG', 'TEMPMELS', 'TEMPSARP', 'TEMPFJER', 'TEMPBUHLM', 
                               'TEMPGEILO', 'TEMPMOL', 'TEMPVIGR', 'TEMPTAFJ', 'TEMPVENA', 'TEMPSGNDL', 
                               'TEMPSAUD', 'TEMPKRS', 'TEMPSTAV', 'TEMPBER', 'TEMPKRSU', 'TEMPSUNN', 
                               'TEMPRORO', 'TEMPTRH', 'TEMPNMS', 'TEMPMAJA', 'TEMPBOD', 'TEMPTRM', 'TEMPALTA', 
                               'TEMPSLT', 'TEMPFORDE', 'TEMPRENA'], start_date)
# --

# Example usage
# test = data_extractor(['PROSE3'], ['ProductionGWh'], '01.01.2021')
# print(test.describe())
