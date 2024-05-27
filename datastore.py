import pandas as pd
import urllib.parse as url

#Due to SKM limiting data requests to 5 years at a time, we need to split the requests.
initial_date = '01.01.2018'
second_date = '01.01.2021'
final_date = '31.12.2023'

final_date_forecast = 'd+7' # unused

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
def getTotalConsumptionProduction(symbol = ['CNPSE3', 'PROSE3']): # GWh
    return fetch_skm_data(symbol, ['ConsumptionGWh', 'ProductionGWh'] )
# TRANSMISSION UMM
def getTransmissionCapTo(symbol = ['Transmission#Cap#DK1SE3', 'Transmission#Cap#NO1SE3', 
                                   'Transmission#Cap#SE2SE3', 'Transmission#Cap#FISE3', 
                                   'Transmission#Cap#SE4SE3']):
    return fetch_skm_data(symbol, ['TDK1SE3', 'TNO1SE3', 'TSE2SE3', 'TF1SE3', 'TSE4SE3'])    

def getTransmissionCapFrom(symbol = ['Transmission#Cap#SE3DK1', 'Transmission#Cap#SE3NO1', 
                                   'Transmission#Cap#SE3SE2', 'Transmission#Cap#SE3FI', 
                                   'Transmission#Cap#SE3SE4']):
    return fetch_skm_data(symbol, ['TSE3DK1', 'TSE3NO1', 'TSE3SE2', 'TSE3F1', 'TSE3SE4'])    

#NET Exchange flow SE3 (MWh) (import - export)
def getNetFlow(symbol = ['SFLOWSE3']):
    return fetch_skm_data(symbol, ['NetFlowSE3'] )

def getFlow(symbol = ['SFLOWSE2SE3', 'SFLOWSE3FI', 'SFLOWSE3SE4']):
    return fetch_skm_data(symbol, ['F_LOWSE2SE3', 'F_LOWSE3FI', 'F_LOWSE3SE4'] )

# Capacity data in MWH
def getFlowCapacityTo(symbol = ['SCAPSE4SE3', 'SCAPDK1SE3', 'SCAPFISE3', 'SCAPNO1SE3', 'SCAPSE2SE3']):
    return fetch_skm_data(symbol,  ['C_SE4SE3', 'C_DK1SE3', 'C_FISE3', 'C_NO1SE3', 'C_SE2SE3'] )

def getFlowCapacityFrom(symbol = ['SCAPSE3DK1', 'SCAPSE3FI', 'SCAPSE3NO1', 'SCAPSE3SE2', 'SCAPSE3SE4']):
    return fetch_skm_data(symbol,  ['C_SE3DK1', 'C_SE3FI', 'C_SE3NO1', 'C_SE3SE2', 'C_SE3SE4'] )

# Power exchange in GWh
def getNetExchange(symbol = ['EXHSE']):
    return fetch_skm_data(symbol,  ['ESE'] )

def getExchangeFrom(symbol = ['EXHSE3_FI', 'EXHSE3_NO1', 'EXHSE3_DK1', 'EXHSE3_SE4', 'EXHSE3_SE2']):
    return fetch_skm_data(symbol,  ['ESE3_FI', 'ESE3_NO1', 'ESE3_DK1', 'ESE3_SE4', 'ESE3_SE2'] )

def getExchangeTo(symbol =  ['EXHFI_SE3', 'EXHDK1_SE3', 'EXHSE2_SE3', 'EXHSE4_SE3', 'EXHNO1_SE3']):
    return fetch_skm_data(symbol,  ['EFI_SE3', 'EDK1_SE3', 'ESE2_SE3', 'ESE4_SE3', 'ENO1_SE3'] )


def getTurnover(symbol =  ['TOVERSE3_SK', 'TOVERSE3_SS']):
    return fetch_skm_data(symbol,  ['TurnoverB', 'TurnoverS'] )
# --

# -- Svenska Kraftnät

def getAllSE1ProductionMWh(symbol = ['PROSE1WAT', 'PROSE1WINDON_ENTSOE', 'PROSE1TRM']):
    return fetch_skm_data(symbol, ['waterSE1(MWh)', 'windSE1(MWh)', 'trmSE1MWh'] )

def getAllSE2ProductionMWh(symbol = ['PROSE2WAT', 'PROSE2WINDON_ENTSOE', 'PROSE2SOL', 'PROSE2TRM', 'PROSE2OTH']):
    return fetch_skm_data(symbol, ['waterSE2(MWh)', 'windSE2(MWh)', 'solSE2MWh', 'trmSE2MWh', 'OthSE2MWh'] )

def getAllSE3ProductionMWh(symbol = ['PROSE3WAT', 'PROSE3WINDON_ENTSOE', 'PROSE3NUC', 'PROSE3SOL', 'PROSE3TRM', 'PROSE3OTH']):
    return fetch_skm_data(symbol, ['waterSE3(MWh)', 'windSE3(MWh)', 'nucSE3(MWh)', 'solSE3MWh', 'trmSE3MWh', 'OthSE3MWh'] )

def getAllSE4ProductionMWh(symbol = ['PROSE4WAT', 'PROSE4WINDON_ENTSOE', 'PROSE4SOL', 'PROSE4TRM', 'PROSE4OTH']):
    return fetch_skm_data(symbol, ['waterSE4(MWh)', 'windSE4(MWh)', 'solSE4MWh', 'trmSE4MWh', 'OthSE4MWh'] )
# --

# -- SMHI  
def getDailyPerc(symbol = ['PENSE;DAY' ]): # Precipitation Energy in GWh!
    return fetch_skm_data(symbol, ['PrecipitationEnergySE(day)'])
def getDailyPerEnergy_Norway_Finland(symbol = [ 'PENNO;DAY', 'PENFI;DAY']):
    return fetch_skm_data(symbol, ['PrecipitationEnergyNO(day)', 'PrecipitationEnergyFI(day)'])
def getHourlyWindVelocity(symbol = ['WINDPITE']): # Wind velocity in m/s
    return fetch_skm_data(symbol, ['Wind(Pite)'])
# --    

# -- Svensk Energi
def getWeeklyHydro(symbol = ['WATSE;WEEK', 'HBALSE;WEEK']):
    return fetch_skm_data(symbol, ['HydroRes(GWh_week)', 'HydroBalance(GWh_week)'] )
#--

# -- EEX, ENTSOE
def getHourlyProduction_Germany_all(symbol = ['PRODEWINDON_ENTSOE', 'PRODESOL', 'PRODEGEOTHM_ENTSOE', 'PRODEBIO_ENTSOE', 'PRODEHCL_ENTSOE', 
                                          'PRODEGAS_ENTSOE', 'PRODEOIL_ENTSOE', 'PRODELIG_ENTSOE', 'PRODENUC_ENTSOE', 'CNPDEPUMP_ENTSOE'
                                          , 'PRODERNO_ENTSOE', 'PRODEWASTE_ENTSOE']):
    return fetch_skm_data(symbol, ['wind(Mwh)', 'solar(Mwh)', 'trm(Mwh)', 'biomass(Mwh)', 'coal(MWh)', 
                                   'gas(MWh)', 'oil(MWh)', 'lignite(MWh)', 'nuc(MWh)', 'pump(MWh)',
                                   'other(MWh)', 'waste(MWh)'] )
    
def getHourlyProduction_nuclear_EU(symbol = ['PROFINUC_ENTSOE', 'PRODENUC_ENTSOE']):
    return fetch_skm_data(symbol, ['nucFI(MWh)', 'nucDE(MWh)'] )
# --

# -- PAST + WEEK AHEAD PLANNED DATA UMM

#There is no SE1 -> SE3 and SE3 -> SE1
def getTransmissionCapTo_forecast(symbol = ['Transmission#Cap#DK1SE3', 'Transmission#Cap#NO1SE3', 
                                   'Transmission#Cap#SE2SE3', 'Transmission#Cap#FISE3', 
                                   'Transmission#Cap#SE4SE3']):
    return fetch_skm_data(symbol, ['TDK1SE3', 'TNO1SE3', 'TSE2SE3', 'TF1SE3', 'TSE4SE3'] , start_date=start_date, end_date=[second_date, final_date_forecast])    

def getTransmissionCapFrom_forecast(symbol = ['Transmission#Cap#SE3DK1', 'Transmission#Cap#SE3NO1', 
                                   'Transmission#Cap#SE3SE2', 'Transmission#Cap#SE3FI', 
                                   'Transmission#Cap#SE3SE4']):
    return fetch_skm_data(symbol, ['TSE3DK1', 'TSE3NO1', 'TSE3SE2', 'TSE3F1', 'TSE3SE4'] , start_date=start_date, end_date=[second_date, final_date_forecast])

def getTotalConsumptionProduction_future(symbol = ['CNPSE3', 'PROSENP_F']): # GWh
    return fetch_skm_data(symbol, ['ConsumptionGWh', 'ProductionGWh'] )
# Example usage
# test = data_extractor(['PROSE3'], ['ProductionGWh'], '01.01.2021')
# print(test.describe())
