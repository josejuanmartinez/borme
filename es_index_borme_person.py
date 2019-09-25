from elasticsearch import Elasticsearch

class ElasticSearchUtils:
    """Custom class for managing Elastic Searcher queries"""

    def __init__(self):
        pass

    @staticmethod
    def create_index():
        ElasticSearchUtils.remove_index()
        es = Elasticsearch()
        request_body = {
            "settings": {
                "number_of_shards": 5,
                "number_of_replicas": 1
            },

        }
        res = es.indices.create(index='borme-person', body=request_body)

    @staticmethod
    def remove_index():
        es = Elasticsearch()
        res = es.indices.delete(index='borme-person', ignore=[400, 404])

if __name__ == "__main__":
    ElasticSearchUtils.create_index()
