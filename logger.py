
class FolderLogger:
    def __init__(self):
        self.file_types = {
            "Images" : ["jpg", "jpeg", "png", "gif", "bmp"],
            "Document" : ["pdf", "docx", "doc", "txt", "xlsx"],
            "Audio" : ["mp3", "wav", "aac"],
            "Video" : ["mp4", "mov", "avi", "mkv"],
            "code" : ["py", "js", "html", "css", "java", "cpp"],
            "Archive" : ["zip", "rar", "tar", "gz"]
        }
        self.counts = {
            "Images": 0,
            "Document": 0,
            "Audio": 0,
            "Video": 0,
            "code": 0,
            "Archive": 0,
            "No Extension": 0,
            "Others": 0
        }
    
    #Update count and log moved file
    def log_file_move(self, file, category):
        self.counts[category] += 1
        print(f"Moved: {file} to {category} folder")

    #Summary of moved files log
    def summaryLog(self):
        print("\nSummary of files moved:")
        for category, count in self.counts.items():
            print(f"{category}: {count} files")
