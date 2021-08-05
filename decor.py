import builtins
import logging
import re
from json.decoder import JSONDecodeError
import jsonschema
import typing

log = logging.getLogger(__name__)

SIMPLE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "examples": [
            {
                "key":0
            }
    ],
    "required": ["key"],
    "additionalProperties": False,
    "properties": {
        "key":{
            "type": "integer",
            "exclusiveMaximum": 100
        }
    }
}


def input_validation1(x: str) -> bool:
    """Валидация входящего значения."""
    regex = re.compile("^[0-9]+$")
    return bool(regex.match(x))


def result_validation1(result: dict) -> bool:
    """Валидация результата."""
    try:
        return not bool(jsonschema.validate(result, SIMPLE_SCHEMA))
    except jsonschema.ValidationError:
        return False


def default_behavior1() -> None:
    """Функция выполнится при выходе из цикла в декоратере."""
    print("Функция выполняется при истечении дозволенного количества повторений")


class InputParameterVerificationError(Exception):
    """Обработка исключения ввода."""

    def __init__(self, message: str):
        """Инициализация обработки исключения ввода."""
        self.message = message
        super().__init__(message) #??? из примера Алекса

    def __str__(self) -> str:
        return f"Error: {self.message}"


class ResultVerificationError(Exception):
    """Обработка исключения результата."""

    def __init__(self, message: str):
        """Инициализация обработки исключения результата."""
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"Error : {self.message}"


class MyCustomError(Exception):
    """Своё исключение."""
     def __init__(self, *args):
        if args:
            self.message = message
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return f"ошибка : {self.message}"
        else:
            return 'MyCustomError has been raised'
  

def fun_exc(exc: typing.Any) -> None:
    """Обработка всех исключений декоратора."""
    try:
        if exc == "Input":
            raise InputParameterVerificationError("Ошибка сработала:InpParVerifError")
        if exc == "Valid":
            raise ResultVerificationError("Ошибка сработала:ResVerifError")
        if exc == 0:
            raise OnFailRepeatTimesError("Ошибка сработала:OnFailRepTimeError")
        
    except JSONDecodeError:
        print("Ошибка импорта")
        
    except InputParameterVerificationError as err:
        print(f"Ошибка ввода {err}")
        
    except ResultVerificationError as err:
        print(f"Ошибка значения {err}")
        
    except OnFailRepeatTimesError as err:
        print(f"Ошибка значения {err}")


def my_param(
    input_valid,
    result_valid,
    on_fail_repeat_times = 1,
    default_behavior  = None,
    ) -> typing.Any:
    
    """Декоратор для  исключений."""
    def dec_func(func: typing.Any) -> typing.Any:
        def cyclefunc(*arg: str, **kwargs: str) -> typing.Any:
            input = input_valid(*arg, **kwargs)
            if input == None:
                fun_exc("Input")
                exit(1)
            result = result_valid(func(*arg, **kwargs))
            if result == None:
                if on_fail_repeat_times == 0:
                    fun_exc(0)
                    exit(1)
                if on_fail_repeat_times < 0:
                    while on_fail_repeat_times != 0:
                        fun_exc("Valid")
                        func(*arg, **kwargs)
                if on_fail_repeat_times > 0:
                    for i in range(on_fail_repeat_times):
                        fun_exc("Valid")
                        func(*arg, **kwargs)
                    default_behavior()
            else:
                res = func(*arg, **kwargs)
                return res
        return cyclefunc

    return dec_func

    def default(x) -> dict:

    return {"key" : int(x)}


@my_param(input_valid, result_valid,
                 on_fail_repeat_times=3, default_behavior=default_behavior1)


  

