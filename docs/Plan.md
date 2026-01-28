# Plan

So there will be a primitive EIA scraper with the API and the ability to call constant.




class BaseScraper(ABC):

    def __init__(
        max_retries :  int = 3
        waiting : int = 30
    ) 

        self.max_retries : int =4
        self.waiting : int

    def retry_wrapper(func : func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            retry = 0
            while retry < max_retries
                try:
                    data = 
                except 




class EIAScraper()

    base_url : str = XXX


    def get(
        start : str
        end : str,
        duoarea : Iterable[str],
        process : Iterable [str],
        product : [str],
        Series : [str],
        sort : Sequence[ Sequence[str..]],

    )
    