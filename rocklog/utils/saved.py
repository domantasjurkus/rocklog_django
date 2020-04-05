def decorate_with_saved_all(stream):
    for stream_entry in stream:
        stream_entry.saved = True
    return stream


def decorate_with_saved_user(stream, saved_songs):
    for entry in stream:
        for saved_song in saved_songs:
            if entry.song_id == saved_song.song_id:
                entry.saved = True
    return stream