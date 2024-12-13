from abc import ABC, abstractmethod
from services.dto import FinancialDTO


# Interface for a Chain of Responsability design pattern
class Handler(ABC):
    @abstractmethod
    def execute(self, dto: FinancialDTO) -> FinancialDTO:
        raise NotImplementedError
    
    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def execute(self, dto: FinancialDTO) -> FinancialDTO:
        if self._next_handler:
            return self._next_handler.execute(dto)

        return dto

