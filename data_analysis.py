import pandas as pd 
import datetime as dt

data_path = r'C:\Users\HP\Documents\Uni\Master\PM\Project_data\incidentProcess_custom_wo_bom_filtered.csv'

def load_data():
    df = pd.read_csv(data_path, sep=';')
    df = df.sort_values(by=['Incident ID'])
    return df

def incident_sorted_list(df,incident):
    df = df[df['Incident ID'] == incident]
    df['ActivityTimeStamp'] = pd.to_datetime(df['ActivityTimeStamp'])
    df['ActivityTimeStamp'] = df['ActivityTimeStamp'].apply(lambda x: dt.datetime.strftime(x, '%Y-%d-%m %H:%M:%S'))
    df = df.sort_values(by=['ActivityTimeStamp'], ascending=True)
    print(df)
    return df

def check_ping_pong(df, i):
    try:
        activityA = df['Activity'].iloc[i]
        activityB = df['Activity'].iloc[i+1]
        if activityA == activityB:
            if df['Assignment Group'].iloc[i] != df['Assignment Group'].iloc[i+1]:
                #hier dus eigenlijk een lijst met tuple (teamA en TeamB plus timestamps en misschien ook de activiteit in kwestie) returnen en na alle incidenten opslaan
                print(df['Assignment Group'].iloc[i]) 
                print(df['Assignment Group'].iloc[i+1])
        check_ping_pong(df, i+1)
    except IndexError:
        print('Endddd')


def main():
    dataset = load_data()
    incident_list = pd.unique(dataset['Incident ID'])
    incident_sorted_list(dataset, incident_list[0])
    test = incident_sorted_list(dataset, incident_list[100])
    check_ping_pong(test, 0)
    
if __name__ == '__main__':
    main()