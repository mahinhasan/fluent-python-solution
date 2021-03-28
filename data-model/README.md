# doctest — Test interactive Python examples¶



category method names
string/bytes representation __repr__, __str__, __format__, __bytes__
conversion to number __abs__, __bool__, __complex__, __int__, __float__, __hash__, __in
dex__
emulating collections __len__, __getitem__, __setitem__, __delitem__, __contains__
iteration __iter__, __reversed__, __next__
emulating callables __call__
context management __enter__, __exit__
instance creation and destruction __new__, __init__, __del__
attribute management __getattr__, __getattribute__, __setattr__, __delattr__, __dir__
attribute descriptors __get__, __set__, __delete__
class services __prepare__, __instancecheck__, __subclasscheck__
Table 1-2. Special method names for operators.
category method names and related operators
unary numeric operators __neg__ -, __pos__ +, __abs__ abs()
rich compartison operators __lt__ >, __le__ <=, __eq__ ==, __ne__ !=, __gt__ >, __ge__ >=
arithmetic operators __add__+,__sub__-,__mul__*,__truediv__/,__floordiv__//,__mod__
%, __divmod__ divmod() , __pow__ ** or pow(), __round__ round()
reversed arithmetic operators __radd__, __rsub__, __rmul__, __rtruediv__, __rfloordiv__,
__rmod__, __rdivmod__, __rpow__
augmented assignment
arithmetic operators
__iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__, __im
od__, __ipow__
bitwise operators __invert__ ~, __lshift__ <<, __rshift__ >>, __and__ &, __or__ |,
__xor__ ^
reversed bitwise operators __rlshift__, __rrshift__, __rand__, __rxor__, __ror__
augmented assignment bitwise
operators
__ilshift__, __irshift__, __iand__, __ixor__, __ior__