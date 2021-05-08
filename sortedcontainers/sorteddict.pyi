from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Hashable,
    Iterator,
    Iterable,
    ItemsView,
    KeysView,
    List,
    Mapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Tuple,
    Union,
    ValuesView,
    overload,
)

_T = TypeVar("_T")
_S = TypeVar("_S")
_T_h = TypeVar("_T_h", bound=Hashable)
_KT = TypeVar("_KT", bound=Hashable)  # Key type.
_VT = TypeVar("_VT")  # Value type.
_KT_co = TypeVar("_KT_co", covariant=True, bound=Hashable)
_VT_co = TypeVar("_VT_co", covariant=True)
_SD = TypeVar("_SD", bound=SortedDict)
_Key = Callable[[_T], Any]

class SortedDict(Dict[_KT, _VT]):
    @overload
    def __init__(self, **kwargs: _VT) -> None: ...
    @overload
    def __init__(self, __map: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def __init__(
        self, __iterable: Iterable[Tuple[_KT, _VT]], **kwargs: _VT
    ) -> None: ...
    @overload
    def __init__(self, __key: _Key[_KT], **kwargs: _VT) -> None: ...
    @overload
    def __init__(
        self, __key: _Key[_KT], __map: Mapping[_KT, _VT], **kwargs: _VT
    ) -> None: ...
    @overload
    def __init__(
        self,
        __key: _Key[_KT],
        __iterable: Iterable[Tuple[_KT, _VT]],
        **kwargs: _VT
    ) -> None: ...
    @property
    def key(self) -> Optional[_Key[_KT]]: ...
    @property
    def iloc(self) -> SortedKeysView[_KT]: ...
    def clear(self) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __reversed__(self) -> Iterator[_KT]: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def _setitem(self, key: _KT, value: _VT) -> None: ...
    def copy(self: _SD) -> _SD: ...
    def __copy__(self: _SD) -> _SD: ...
    @classmethod
    @overload
    def fromkeys(cls, seq: Iterable[_T_h]) -> SortedDict[_T_h, None]: ...
    @classmethod
    @overload
    def fromkeys(cls, seq: Iterable[_T_h], value: _S) -> SortedDict[_T_h, _S]: ...
    def keys(self) -> SortedKeysView[_KT]: ...
    def items(self) -> SortedItemsView[_KT, _VT]: ...
    def values(self) -> SortedValuesView[_VT]: ...
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _T = ...) -> Union[_VT, _T]: ...
    def popitem(self, index: int = ...) -> Tuple[_KT, _VT]: ...
    def peekitem(self, index: int = ...) -> Tuple[_KT, _VT]: ...
    def setdefault(self, key: _KT, default: _VT = ...) -> _VT: ...
    @overload
    def update(self, __map: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def update(
        self, __iterable: Iterable[Tuple[_KT, _VT]], **kwargs: _VT
    ) -> None: ...
    @overload
    def update(self, **kwargs: _VT) -> None: ...
    def __reduce__(
        self
    ) -> Tuple[
        Type[SortedDict[_KT, _VT]],
        Tuple[Callable[[_KT], Any], List[Tuple[_KT, _VT]]],
    ]: ...
    def __repr__(self) -> str: ...
    def _check(self) -> None: ...

class SortedKeysView(KeysView[_KT_co], Sequence[_KT_co]):
    @overload
    def __getitem__(self, index: int) -> _KT_co: ...
    @overload
    def __getitem__(self, index: slice) -> List[_KT_co]: ...
    def __delitem__(self, index: Union[int, slice]) -> None: ...

class SortedItemsView(
    ItemsView[_KT_co, _VT_co], Sequence[Tuple[_KT_co, _VT_co]]
):
    def __iter__(self) -> Iterator[Tuple[_KT_co, _VT_co]]: ...
    @overload
    def __getitem__(self, index: int) -> Tuple[_KT_co, _VT_co]: ...
    @overload
    def __getitem__(self, index: slice) -> List[Tuple[_KT_co, _VT_co]]: ...
    def __delitem__(self, index: Union[int, slice]) -> None: ...

class SortedValuesView(ValuesView[_VT_co], Sequence[_VT_co]):
    @overload
    def __getitem__(self, index: int) -> _VT_co: ...
    @overload
    def __getitem__(self, index: slice) -> List[_VT_co]: ...
    def __delitem__(self, index: Union[int, slice]) -> None: ...