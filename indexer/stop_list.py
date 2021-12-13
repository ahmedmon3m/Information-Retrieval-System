from abc import ABC, abstractmethod
import nltk
from nltk.corpus import stopwords
class StopList(ABC):
    @abstractmethod
    def __contains__(self, word: str) -> bool:
        raise NotImplementedError

class ReutersRCV1StopList(StopList):
    def __contains__(self, word):
        for word in str:
            if word in stopwords:
               return True
            else:
                return False
        raise NotImplementedError
