__author__ = 'xt'

conf = {
    'douban': {
        'name': 'douban',
        'allow_domains': ['douban.com'],
        'start_urls': ['http://www.douban.com/'],
        'article': '//div[@class="notes"]//li//a',
        'create_time': {
            'xpath': "//div[@id='content']//div/span[@class='pl']/text()",
            'index': 0,
        },
        'author': {
            'xpath': '//div/a[@class="note-author"]/text()',
            'index': 0,
        },
        'title': {
            'xpath': '//div[contains(@class, "note-header")]/h1/text()',
            'index': 0,
        },
        'content': {
            'xpath': "//div[@id='link-report']",
        },
    },
    'guoke': {
        'name': 'guoke',
        'allow_domains': ['guokr.com'],
        'start_urls': ['http://www.guokr.com/'],
        'article': '//div[@class="focus-explain"]//a',
        'create_time': {
            'xpath': '//div[@class="content-th-info"]/span/text()',
            'index': 0,
        },
        'author': {
            'xpath': '//div[@class="content-th-info"]/a/text()',
            'index': 0,
        },
        'title': {
            'xpath': '//h1[@id="articleTitle"]/text()',
            'index': 0,
        },
        'content': {
            'xpath': '//div[@class="document"]/div',
            'index': 0,
        },
    },
    'tengxun': {
        'name': 'tengxun',
        'allow_domains': ['news.qq.com'],
        'start_urls': ['http://news.qq.com/'],
        'article': '//div[@class="Q-tpList"]//a',
        'create_time': {
            'xpath': '//span[@class="article-time"]/text()',
            'index': 0,
        },
        'author': {
            'xpath': '//span[@bosszone="jgname"]/a/text()',
            'index': 0,
        },
        'title': {
            'xpath': '//div[@class="hd"]/h1/text()',
            'index': 0,
        },
        'content': {
            'xpath': '//div[@accesskey="3"]',
            'index': 0,
        },
    },
    'sina': {
        'name': 'sina',
        'allow_domains': ['news.sina.com.cn'],
        'start_urls': ['http://news.sina.com.cn/'],
        'article': '//div[@class="blk_04"]//a',
        'create_time': {
            'xpath': '(//span[@class="time-source"] | //span[@id="pub_date"])/text()',
            'index': 0,
        },
        'author': {
            'xpath': '(//span[@data-sudaclick="media_name"] | //span[@id="media_name"])/a/text()',
            'index': 0,
        },
        'title': {
            'xpath': '//h1[@id="artibodyTitle"]/text()',
            'index': 0,
        },
        'content': {
            'xpath': '//div[@id="artibody"]//p',
            'join': 1,
        },
    },
    '36kr': {
        'name': '36kr',
        'allow_domains': ['36kr.com'],
        'start_urls': ['http://36kr.com/'],
        'article': '//div[@class="head-images J_headImages"]//a |'
                   ' //div[@class="article-list"]//article//a[@target="_blank"]',
        'create_time': {
            'xpath': '//time[@class="timeago"]/attribute::title',
            'index': 0,
        },
        'author': {
            'xpath': '//span[@class="name"]/text()',
            'index': 0,
        },
        'title': {
            'xpath': '//h1[@class="single-post__title"]/text()',
            'index': 0,
        },
        'content': {
            'xpath': '//section[@class="article"]',
            'index': 0,
        },
    },

}
