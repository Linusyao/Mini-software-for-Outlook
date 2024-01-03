import os

def rename_msg_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".msg") and filename.startswith("2023-"):
            # Zerlege den Dateinamen 
            parts = filename.split("-")
            # Ändere das Datumsteil des Dateinamens
            new_date = parts[0][2:] + parts[1] + parts[2]
            # Erstelle den neuen Dateinamen
            new_filename = new_date + "-" + "-".join(parts[3:])
            # Benenne die Datei um
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

# Ändere den Pfad zum Verzeichnis, in dem sich deine MSG-Dateien befinden
#directory_path 
directory_path = r"C:\directory_path"
rename_msg_files(directory_path)
