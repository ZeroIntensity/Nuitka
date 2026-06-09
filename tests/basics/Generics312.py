#     Copyright 2026, Kay Hayen, mailto:kay.hayen@gmail.com find license text at end of file


"""Generic tests, cover most important forms of them."""

# Tests are dirty on purpose.
#
# pylint: disable=redefined-outer-name,used-before-assignment


def someGenericFunction[T]():
    print("hello", T)


someGenericFunction()

# Verify the name didn't leak.
try:
    print(T)
except NameError:
    print("not found")

T = 1


def someGenericFunctionShadowingGlobal[T]():
    print(T)


someGenericFunctionShadowingGlobal()
print(T)


print("Function in a class with private name")


class someClassWithPrivateArgumentNames:
    def f(self, *, __kw: 1):
        pass


print(someClassWithPrivateArgumentNames.f.__annotations__)


def simpleExample[T](test: T) -> T:
    print(test)
    return test


simpleExample(42)

try:
    print(T)
except NameError:
    print("good")

try:

    def weirdExample[T](a: T = T):
        print(a)

except NameError as err:
    print(err)

try:

    def weirdExample[*Ts](a: Ts = Ts):
        print(a)

except NameError as err:
    print(err)

try:

    def weirdExample[**P](a: P = P):
        print(a)

except NameError as err:
    print(err)


try:

    async def asyncExample[T, *Ts, **P](a: T, b: Ts, c: P) -> T | Ts | P:
        print(a, b, c)
        print(T, Ts, P)

    # This is a little cheat to await it without using asyncio
    try:
        asyncExample(1, 2, 3).send(None)
    except StopIteration:
        print("Awaited function")
except NameError as err:
    print(err)


class TypeParams[T, *Ts, **P]:
    saved = (T, Ts, P)


print(TypeParams.__type_params__)
print(tuple(a is b for a, b in zip(TypeParams.__type_params__, TypeParams.saved)))
print(TypeParams.__bases__)
print(TypeParams.__orig_bases__)


def functionTypeParams[T, *Ts, **P]():
    pass


async def asyncFunctionTypeParams[T, *Ts, **P]():
    pass


async def asyncGenTypeParams[T, *Ts, **P]():
    pass


print(functionTypeParams, functionTypeParams.__type_params__)
print(asyncFunctionTypeParams, asyncFunctionTypeParams.__type_params__)
print(asyncGenTypeParams, asyncGenTypeParams.__type_params__)


def sideEffect():
    print("Side effect")
    return int


class CustomBound:
    pass


def BoundUsingFunction[
    BoundT: str,
    DeferredT: sideEffect(),
    ConstrainedT: (str, bytes),
    CustomT: CustomBound,
    GenericAliasT: list[int],
    UnboundT,
]():
    print("Function TypeVar bound", BoundT.__bound__ is str)
    print("Function TypeVar deferred bound", DeferredT.__bound__ is int)
    print("Function TypeVar deferred cached", DeferredT.__bound__ is int)
    print("Function TypeVar constrained bound", ConstrainedT.__bound__ is None)
    print(
        "Function TypeVar constraints",
        ConstrainedT.__constraints__ == (str, bytes),
    )
    print("Function TypeVar custom bound", CustomT.__bound__ is CustomBound)
    print("Function TypeVar generic alias bound", GenericAliasT.__bound__ == list[int])
    print("Function TypeVar unbound", UnboundT.__bound__ is None)


print("Function with bound")
BoundUsingFunction()

print("Class with bound")


class BoundUsingClass[
    BoundT: str,
    DeferredT: sideEffect(),
    ConstrainedT: (str, bytes),
    CustomT: CustomBound,
    GenericAliasT: list[int],
    UnboundT,
]:
    print("Class TypeVar bound", BoundT.__bound__ is str)
    print("Class TypeVar deferred bound", DeferredT.__bound__ is int)
    print("Class TypeVar deferred cached", DeferredT.__bound__ is int)
    print("Class TypeVar constrained bound", ConstrainedT.__bound__ is None)
    print(
        "Class TypeVar constraints",
        ConstrainedT.__constraints__ == (str, bytes),
    )
    print("Class TypeVar custom bound", CustomT.__bound__ is CustomBound)
    print("Class TypeVar generic alias bound", GenericAliasT.__bound__ == list[int])
    print("Class TypeVar unbound", UnboundT.__bound__ is None)


type AliasBound[AliasT: str] = list[AliasT]
type AliasDeferred[AliasT: sideEffect()] = AliasT
type AliasConstrained[AliasT: (str, bytes)] = AliasT
type AliasCustom[AliasT: CustomBound] = AliasT
type AliasGeneric[AliasT: list[int]] = AliasT
type AliasUnbound[AliasT] = AliasT

print("After type alias bound definitions")
print("Type alias TypeVar bound", AliasBound.__type_params__[0].__bound__ is str)
print(
    "Type alias TypeVar deferred bound",
    AliasDeferred.__type_params__[0].__bound__ is int,
)
print(
    "Type alias TypeVar deferred cached",
    AliasDeferred.__type_params__[0].__bound__ is int,
)
print(
    "Type alias TypeVar constrained bound",
    AliasConstrained.__type_params__[0].__bound__ is None,
)
print(
    "Type alias TypeVar constraints",
    AliasConstrained.__type_params__[0].__constraints__ == (str, bytes),
)
print(
    "Type alias TypeVar custom bound",
    AliasCustom.__type_params__[0].__bound__ is CustomBound,
)
print(
    "Type alias TypeVar generic alias bound",
    AliasGeneric.__type_params__[0].__bound__ == list[int],
)
print("Type alias TypeVar unbound", AliasUnbound.__type_params__[0].__bound__ is None)


#     Python tests originally created or extracted from other peoples work. The
#     parts were too small to be protected.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
