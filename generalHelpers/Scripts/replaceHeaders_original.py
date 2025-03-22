import os

def replaceHeadersFromCSVbyDirectory(source_dir):

    """
    Receives the directory that contains the csv's and for each header it will replace the underscore (_) with a point (.).

    Args:
        source_dir = directory that keeps the csv files.
    """
    try:
        for domain_folder in os.listdir(source_dir):
            domain_path = os.path.join(source_dir, domain_folder)

            csv_folder = os.path.join(domain_path, "CSVs") 

            for file_name in os.listdir(csv_folder):
                if file_name.endswith(".csv"):
                    file_path = os.path.join(csv_folder, file_name)

                with open(file_path, "r", encoding="utf-8") as file:
                        lines = file.readlines() 
                        
                        if not lines:
                            continue
                        
                        headers = lines[0].strip().split(",") 
                        headers = [header.replace("_", ".") for header in headers]
                        lines[0] = ",".join(headers) + "\n"

                        with open(file_path, "w", encoding="utf-8") as file:
                            file.writelines(lines)

    except Exception as e:
        print(e)

            


if __name__ == "__main__":
    source_directory = "ITC_Files"

    replaceHeadersFromCSVbyDirectory(source_directory)