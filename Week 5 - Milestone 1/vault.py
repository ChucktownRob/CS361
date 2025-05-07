from storage import read_videos, write_video
from zeromq_stub import ZmqInt


class VideoVault:
    def __init__(self):
        self.filename = "video_vault.csv"
        self.zmq_stub = ZmqInt()  # Provisioned

    def add_video(self, title, format_, year):
        check = self.search(title)
        if len(check) != 0:
            return 0
        else:
            record = {"Title": title, "Format": format_, "Year": year}
            write_video(self.filename, record)
            return 1

    def search(self, query):
        videos = read_videos(self.filename)
        query = query.lower()
        results = [v for v in videos if query in v["Title"].lower() or query in v["Format"].lower() or query in v["Year"]]
        return results

    def list_all(self):
        return read_videos(self.filename)
