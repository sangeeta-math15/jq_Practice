import jq
import json
from urllib.request import urlopen


class JqDemo:
    """
    create Jq_Demo class
    """
    @staticmethod
    def filter_data():
        """
        this function return filtered data using jq commands
        """
        with open('filename.json', 'r') as f:
            input_data = json.load(f)
            print(jq.compile('{(.user): .titles}').input(input_data).all())

    @staticmethod
    def filter_data1():
        """
        this function return filtered data using jq commands
        """
        url = "https://api.icndb.com/jokes/random"
        response = urlopen(url)
        data_json = json.loads(response.read())
        print(data_json)
        print(jq.compile('.[]|tostring').input(data_json).all())


if __name__ == '__main__':
    j_q = JqDemo()
    j_q.filter_data()
    j_q.filter_data1()
