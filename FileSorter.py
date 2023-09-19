import os
import shutil


# Dictionary extensions
extensions_categories = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico", ".psd", ".ai", ".eps"],
    "videos": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".m4v", ".mpeg", ".mpg", ".3gp", ".m2ts", ".mts", ".ogg", ".vob", ".rm", ".rmvb"],
    "documents": [
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx",
    ".odt", ".ods", ".odp", ".rtf", ".txt", ".csv", ".xml", ".html",
    ".htm", ".md", ".tex", ".epub", ".mobi", ".djvu", ".pages",
    ".numbers", ".keynote", ".pps", ".ppsx", ".wpd", ".azw", ".azw3"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".java", ".js", ".html", ".css", ".xml", ".rb", ".swift", ".kt", ".pl", ".lua", ".sh", ".bat", ".ps1", ".m", ".vb", ".asm", ".r", ".scala", ".h", ".m", ".pas", ".json", ".yml", ".sql", ".jsp", ".asp", ".dart", ".go", ".rust", ".ts", ".vb", ".vbs"],
    "compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz",".rpm"]
}

# Target folder
target_directory = r"C:\your\target\folder"

# Iterate files in target directory
for file in os.listdir(target_directory):
    if file == "FileSorter.py":
        continue
        
    file_path = os.path.join(target_directory, file)
    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()
        
        # Iterate extension categories
        for categorie, extensions in extensions_categories.items():
            if extension in extensions:
                category_folder = os.path.join(target_directory, categorie)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                destination = os.path.join(category_folder, file)
                shutil.move(file_path, destination)
                break
