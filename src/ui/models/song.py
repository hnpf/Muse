import gi
from gi.repository import GObject

gi.require_version("Gtk", "4.0")


class SongItem(GObject.Object):
    __gtype_name__ = "SongItem"

    @GObject.Property(type=str)
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @GObject.Property(type=str)
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        self._artist = value

    @GObject.Property(type=str)
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @GObject.Property(type=str)
    def thumbnail_url(self):
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, value):
        self._thumbnail_url = value

    @GObject.Property(type=str)
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        self._video_id = value

    @GObject.Property(type=str)
    def like_status(self):
        return self._like_status

    @like_status.setter
    def like_status(self, value):
        self._like_status = value

    @GObject.Property(type=bool, default=False)
    def is_playing(self):
        return self._is_playing

    @is_playing.setter
    def is_playing(self, value):
        self._is_playing = value

    @GObject.Property(type=str)
    def album(self):
        return self._album

    @album.setter
    def album(self, value):
        self._album = value

    def __init__(self, track_data, index):
        super().__init__()
        self.track_data = track_data
        self.index = index

        self._title = track_data.get("title", "Unknown")
        artist_list = track_data.get("artists", [])
        if isinstance(artist_list, list):
            self._artist = ", ".join([a.get("name", "") for a in artist_list])
        else:
            self._artist = track_data.get("artist", "Unknown")

        # Album
        album_data = track_data.get("album")
        if isinstance(album_data, dict):
             self._album = album_data.get("name", "")
        else:
             self._album = str(album_data or "")

        # Duration
        dur_sec = track_data.get("duration_seconds")
        if dur_sec:
            m = dur_sec // 60
            s = dur_sec % 60
            self._duration = f"{m}:{s:02d}"
        else:
            self._duration = track_data.get("duration", "")

        # Thumbnail
        thumbnails = track_data.get("thumbnails", [])
        if thumbnails:
            self._thumbnail_url = thumbnails[-1]["url"]
        else:
            self._thumbnail_url = track_data.get("thumb")

        self._video_id = track_data.get("videoId")
        self._like_status = track_data.get("likeStatus", "INDIFFERENT")
        self._is_playing = False
