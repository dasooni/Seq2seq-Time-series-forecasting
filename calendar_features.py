# Will use these after all the other features are extracted
# Calendar information is known as ordinal categorical variables
# Ordinal meaning that the order of the categories is important
# For example, Monday is before Tuesday, and Monday is after Sunday. 
# Same applies to the other features, day of week etc. 

def calendar_transformer(df):
    '''Extracts calendar features from datetime index'''
    from feature_engine.datetime import DatetimeFeatures
    
    transformer = DatetimeFeatures(
        variables   =  "index",
        features_to_extract = ['year', 'month', 'day_of_week', 'weekend', 'hour'] 
    )
    return transformer.fit_transform(df)

def daylight_extractor(df):
    ''' Extracts daylight features from datetime index'''
    from astral.sun import sun
    from astral import LocationInfo
    
    location = LocationInfo("Stockholm", "Sweden", "Europe/Stockholm")
    sunrise_hour = [sun(location.observer, date=date)['sunrise'].hour for date in df.index]
    sunset_hour = [sun(location.observer, date=date)['sunset'].hour for date in df.index]
    
    sun_light_features = pd.DataFrame({'sunrise_hour': sunrise_hour, 'sunset_hour': sunset_hour}, index=df.index)
    sun_light_features['daylight_hours'] = sun_light_features['sunset_hour'] - sun_light_features['sunrise_hour']
    
    return sun_light_features

def get_holidays(df):
    ''' Extracts holidays from datetime index'''
    import holidays
    
    holidays_dict = holidays.Sweden()
    holidays_list = [date in holidays_dict for date in df.index]
    return pd.DataFrame({'holidays': holidays_list}, index=df.index)