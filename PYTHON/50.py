import os
import shutil

def backup_files(source_folder, backup_folder):
    copied_files = set()

    try:
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        log_file = open("backup.log", "a")

        for file_name in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file_name)
            dest_path = os.path.join(backup_folder, file_name)

            try:
                if file_name in copied_files:
                    log_file.write(f"Skipped duplicate: {file_name}\n")
                    continue

                if os.path.isfile(source_path):
                    shutil.copy2(source_path, dest_path)
                    copied_files.add(file_name)
                    log_file.write(f"Copied: {file_name}\n")

            except PermissionError:
                log_file.write(f"Permission denied: {file_name}\n")

        log_file.write("Backup completed successfully.\n")
        log_file.close()

        return "Backup process finished!"

    except FileNotFoundError:
        return "Error: Source folder not found!"
    except Exception as e:
        return f"Unexpected error: {e}"


# Example usage
source = "source_files"
backup = "backup_files"

print(backup_files(source, backup))