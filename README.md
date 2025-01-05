# Design Patterns

## Creational Patterns

#### 1. Builder
  * Seperate component for when object construction gets too complicated
  * Can create mutually cooperating sub-builders
  * Builder often have fluent interface


#### 2. Factories
  * Factory method more expressive than initializer
  * Factory can be an outside class or inner class

#### 3. Prototype
  * Creation of object from an existing object
  * Requires explicity deep copy

#### 4. Singleton
  * When you need to ensure just a single instance exists
  * Easy to make with a decorator or metaclass
  * Consider using dependency injection


## Structural Patterns

#### #### 1. Adaptor
  * Converts the interface you get to the interface you need

#### #### 2. Bridge
  * Decouple abstraction from implementation

#### #### 3. Composite
  * Allow clients to treat individual objects and compositions of objects uniformly

#### #### 4. Decorator
  * Attach additional responsibilities to the objects
  * Python has functional decorators

#### #### 5. Façade
  * Provide a single unified interface over a set of interfaces
  * Friendly and easy-to-use, but can provide access to low-level features

#### #### 6. Flyweight
  * Efficiently support very large number of similar objects

#### #### 7. Proxy
  * Provide a surrogate object that forwards call to the real object while performing additional functions
  * E.g., access control, communication, logging, etc.


## Behavioural Patterns

#### 1. Chain of Responsibility
  * Allow components to processs information/events in a chain
  * Each element in the chain referes to next element; or
  * Make a list and go through it

#### 2. Command
  * Encapsulate a request  into a seperate object
  * Good for audit, replay, undo/redo
  * Part of CQS/ CQRS

#### 3. Interpreter
  * Transform textual input into object-oriented structures
  * Used by interpreters, compilers, static analysis tools, etc.
  * <i>Compiler Theory</i> is a seperate branch of Computer Science

#### 4. Iterator
  * Provide an interface for accessing elements of an aggregate object
  * `__iter__/__next__` are stateful, but *yield* is much more convenient

#### 5. Mediator
  * Provide mediation services between two objects
  * *E.g.* message passing, chat room

#### 6. Memento
  * Yields tokens representing systems states
  * Tokens do not allow direct manipulation, but can be used in appropriate APIs

#### 7. Observer
  * Allows notifications of changes/happenings in a components

#### 8. State
  * We model systems by having one of possible states and transitions between these states
  * Such a system is called a state machine
  * Special frameworks exists to orchestrate state machines

#### 9. Strategy & Template Method
  * Both define a skeleton algorithm with details filled in by implementor
  * Strategy uses ordinary composition, template method uses inheritance

#### 10. Visitor
  * Allow non-intrusive addition of functionality to hierarchies
