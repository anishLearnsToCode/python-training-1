def seconds_to_minutes(seconds: int) -> tuple:
    return seconds // 60, seconds % 60


def print_metadata(video):
    print(video.length)
    print(video.rating)
    minutes, seconds = seconds_to_minutes(video.length)
    print(f'Duration: {minutes}m{seconds}s')


def download_video(video):
    video.download('')
