

INPUT_FILE_PATH = "sampleinput.txt"


class Cache:
    def __init__(self, cache_id, size):
        self.id = cache_id
        self.max_size = size
        self.videos = []
        self.load = 0
        self.dataCenters = []

    def add_video(self, video):
        if video.size + self.load > self.max_size:
            print "Could not load video: %s to cache: %s" % (video.id, self.id)
        else:
            self.videos.append(video)
            self.load += video.size


class Video:

    def __init__(self, video_id, size):
        self.id = video_id
        self.size = size


class Connection:
    def __init__(self, destination, latency):
        self.dest = destination
        self.lag = latency


class Endpoint:
    def __init__(self, endpoint_id, latency):
        self.id = endpoint_id
        self.lag = latency
        self.caches = []


def print_endpoint_info(endpoints):
    for e in endpoints:
        print "Endpoint: ", e.id
        print "\tLatency: ", e.lag
        print "\tCache count: ", len(e.caches)
        for c in e.caches:
            print "\t\tCache: ", c.dest.id
            print "\t\tLatency: ", c.lag

def load_endpoint_data():
    lines = open(INPUT_FILE_PATH).read().split('\n')

    video_count, endpoint_count, req_descriptions, total_cache_count, cache_size = lines[0].split(
        ' ')  # videos, endpoints, req descriptions, caches, size of cache

    videos = lines[1].split(' ')
    print videos
    lines = lines[2:]
    caches = []  # TODO:
    for c in range(0, int(total_cache_count)):
        caches.append(Cache(c, cache_size))

    endpoints = []

    for i in range(0, int(endpoint_count)):
        lag, cache_count = lines[0].split()

        e = Endpoint(i, lag)
        endpoints.append(e)
        for j in range(0, int(cache_count)):
            e_id, e_lag = lines[i + j + 1].split(' ')
            e.caches.append(Connection(caches[int(e_id)], int(e_lag)))

        lines = lines[i + int(cache_count) + 1:]
    return endpoints

if __name__ == "__main__":

    es = load_endpoint_data()
    print_endpoint_info(es)


