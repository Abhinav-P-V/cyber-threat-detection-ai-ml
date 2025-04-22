def extract_features(df):
    df['is_night'] = df['login_hour'].apply(lambda x: 1 if x < 6 or x > 20 else 0)
    df['high_file_access'] = df['files_accessed'].apply(lambda x: 1 if x > 50 else 0)
    df['usb_used'] = df['device_connected']
    return df[['is_night', 'high_file_access', 'usb_used']]
