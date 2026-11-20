from typing import Any, cast
from collections.abc import Sequence, Set, Mapping
from enum import Enum

class DiagnosticsHelper:

    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    @staticmethod
    def format_value(value: Any) -> str:

        if isinstance(value, Enum):
            return f"{value.__class__.__name__}.{value.name}"

        if isinstance(value, (str, bytes)):
            return str(value)

        if isinstance(value, Sequence):
            seq: Sequence[Any] = cast(Sequence[Any], value)

            if isinstance(value, list):
                open_bracket, close_bracket = "[", "]"
            elif isinstance(value, tuple):
                open_bracket, close_bracket = "(", ")"
            else:
                open_bracket, close_bracket = "[", "]"

            parts: list[str] = [DiagnosticsHelper.format_value(elem) for elem in seq]
            inner: str = ", ".join(parts)
            return f"{open_bracket}{inner}{close_bracket}"

        if isinstance(value, Set):
            s: Set[Any] = cast(Set[Any], value)
            parts: list[str] = [DiagnosticsHelper.format_value(elem) for elem in s]
            inner: str = ", ".join(parts)
            return "{" + inner + "}"

        if isinstance(value, Mapping):
            m: Mapping[Any, Any] = cast(Mapping[Any, Any], value)
            parts: list[str] = [f"{DiagnosticsHelper.format_value(k)}: {DiagnosticsHelper.format_value(v)}" for k, v in m.items()]
            inner: str = ", ".join(parts)
            return "{" + inner + "}"

        return str(value)

    @staticmethod
    def object_as_string(obj: Any) -> str:
        cls_name: str = obj.__class__.__name__

        attributes: dict[str, Any] | None
        try:
            attributes = vars(obj) # type: ignore
        except TypeError:
            attributes = None

        if attributes is not None:
            items: list[tuple[str, Any]] = list(sorted(attributes.items(), key = lambda kv: kv[0])) # type: ignore
        else:
            def _should_include(name: str) -> bool:
                if name.startswith("_"):
                    return False
                try:
                    attr = getattr(obj, name)
                except Exception:
                    return False
                return not callable(attr)

            names: list[str] = sorted(n for n in dir(obj) if _should_include(n))
            items = [(n, getattr(obj, n)) for n in names]

        props: list[str] = [f"{key}={DiagnosticsHelper.format_value(value)}" for key, value in items]
        return f"{cls_name}({', '.join(props)})"
    
    @staticmethod
    def console(string: str) -> None:

        print(string)

    @staticmethod
    def console_green(string: str) -> None:

        print (f"{DiagnosticsHelper.GREEN}{string}{DiagnosticsHelper.RESET}")

    @staticmethod
    def console_error(string: str) -> None:

        print (f"{DiagnosticsHelper.RED}{string}{DiagnosticsHelper.RESET}")

    @staticmethod
    def console_object(object: Any) -> None:

        DiagnosticsHelper.console(DiagnosticsHelper.object_as_string(object))