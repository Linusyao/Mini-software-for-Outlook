import os

import extract_msg

def read_email_dates(msg_file):
    # Öffnen MSG file
    with extract_msg.Message(msg_file) as msg:
        # Extrahieren des Sendedatums
        sent_date = msg.date
        
        return sent_date




def rename_msg_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".msg") and not filename.startswith("23-"):
            full_path = os.path.join(directory, filename)

            # Bekommen den Sendedatum
            most_recent = read_email_dates(full_path)

            # Addieren Sendedatum zu den Anfang der Dateinames
            # Formatieren die Zeit für Filename
            formatted_date = most_recent.strftime("%y%m%d")
            # Erstelle den neuen Dateinamen
            new_filename = formatted_date + "-" + filename
            # Benenne die Datei um
            os.rename(full_path, os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")
            
# Ändere den Pfad zum Verzeichnis, in dem sich deine MSG-Dateien befinden
#directory_path 
directory_path = r"C:directory_path"
rename_msg_files(directory_path)
