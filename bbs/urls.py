import random
from scrapy.http import Request
from scrapy.utils.url import canonicalize_url


class RandomUserAgent(object):

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class RandomProxy(object):

    def __init__(self, iplist):
        self.iplist = iplist

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.setting.getlist('IPLIST'))

    def process_request(self, request, spider):
        proxy = random.choice(self.iplist)
        request.meta['proxy'] = proxy


class UrlCanonicalizerMiddleware(object):
    '''实现Request中URL的规范化'''

    def process_spider_output(self, response, result, spider):
        for r in result:
            if isinstance(r, Request):
                curl = canonicalize_url(r.url)
                if curl != r.url:
                    r = r.replace(url=curl)
            yield r
