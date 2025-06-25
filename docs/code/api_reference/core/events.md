
# self.machine.events

``` python
class mpf.core.events.EventManager(machine: MachineController)
```

Bases: `mpf.core.mpf_controller.MpfController`

Handles all the events and manages the handlers in MPF.

## Accessing the events in code

There is only one instance of the events in MPF, and it’s accessible via self.machine.events.

## Methods & Attributes

The events has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_async_handler(event: str, handler: Any, priority: int = 1, blocking_facility: Any = None, **kwargs) → mpf.core.events.EventHandlerKey`

Register a coroutine as event handler.

`add_handler(event: str, handler: Any, priority: int = 1, blocking_facility: Any = None, **kwargs) → mpf.core.events.EventHandlerKey`

Register an event handler to respond to an event.

Parameters:

* **event** – String name of the event you’re adding a handler for. Since events are text strings, they don’t have to be pre-defined.
* **handler** – The callable method that will be called when the event is fired. Since it’s possible for events to have kwargs attached to them, the handler method must include **kwargs in its signature.
* **priority** – An arbitrary integer value that defines what order the handlers will be called in. The default is 1, so if you have a handler that you want to be called first, add it here with a priority of 2. (Or 3 or 10 or 100000.) The numbers don’t matter. They’re called from highest to lowest. (i.e. priority 100 is called before priority 1.)
* **blocking_facility** – Facility which can block this event.
* ****kwargs** – Any any additional keyword/argument pairs entered here will be attached to the handler and called whenever that handler is called. Note these are in addition to kwargs that could be passed as part of the event post. If there’s a conflict, the event-level ones will win.

Returns EventHandlerKey to the handler which you can use to later remove the handler via remove_handler_by_key. For example: `my_handler = self.machine.events.add_handler('ev', self.test))` Then later to remove all the handlers that a module added, you could: for handler in handler_list: `events.remove_handler(my_handler)`

`does_event_exist(event_name: str) → bool`

Check to see if any handlers are registered for the event name that is passed.

Parameters:

* **event_name** – The string name of the event you want to check.

Returns True or False.

`get_event_and_condition_from_string`

Parse an event string to divide the event name from a possible placeholder / conditional in braces.

Parameters:

* **event_string** – String to parse
Returns 2-item tuple- First item is the event name. Second item is the condition (A BoolTemplate instance) if it exists, or None if it doesn’t.

`post(event: str, callback=None, **kwargs) → None`

Post an event which causes all the registered handlers to be called. Events are processed serially (e.g. one at a time), so if the event core is in the process of handling another event, this event is added to a queue and processed after the current event is done. You can control the order the handlers will be called by optionally specifying a priority when the handlers were registered. (Higher priority values will be processed first.)

Parameters:

* **event** – A string name of the event you’re posting. Note that you can post whatever event you want. You don’t have to set up anything ahead of time, and if no handlers are registered for the event you post, so be it.
* **callback** – An optional method which will be called when the final handler is done processing this event. Default is None.
* **`**kwargs`** – One or more options keyword/value pairs that will be passed to each handler. (The event manager will enforce that handlers have `**kwargs` in their signatures when they’re registered to prevent run-time crashes from unexpected kwargs that were included in post() calls.

`post_async(event: str, **kwargs) → _asyncio.Future`

Post event and wait until all handlers are done.

`post_boolean(event: str, callback=None, **kwargs) → None`

Post an boolean event which causes all the registered handlers to be called one-by-one. Boolean events differ from regular events in that if any handler returns False, the remaining handlers will not be called. Events are processed serially (e.g. one at a time), so if the event core is in the process of handling another event, this event is added to a queue and processed after the current event is done. You can control the order the handlers will be called by optionally specifying a priority when the handlers were registered. (Higher priority values will be processed first.)

Parameters:

* **event** – A string name of the event you’re posting. Note that you can post whatever event you want. You don’t have to set up anything ahead of time, and if no handlers are registered for the event you post, so be it.
* **callback** – An optional method which will be called when the final handler is done processing this event. Default is None. If any handler returns False and cancels this boolean event, the callback will still be called, but a new kwarg ev_result=False will be passed to it.
* ****kwargs** – One or more options keyword/value pairs that will be passed to each handler.

`post_queue(event, callback, **kwargs)`

Post a queue event which causes all the registered handlers to be called. Queue events differ from standard events in that individual handlers are given the option to register a “wait”, and the callback will not be called until any handler(s) that registered a wait will have to release that wait. Once all the handlers release their waits, the callback is called. Events are processed serially (e.g. one at a time), so if the event core is in the process of handling another event, this event is added to a queue and processed after the current event is done. You can control the order the handlers will be called by optionally specifying a priority when the handlers were registered. (Higher numeric values will be processed first.)

Parameters:

* **event** - A string name of the event you’re posting. Note that you can post whatever event you want. You don’t have to set up anything ahead of time, and if no handlers are registered for the event you post, so be it.
* **callback** - The method which will be called when the final handler is done processing this event and any handlers that registered waits have cleared their waits.
* **`**kwargs`** - One or more options keyword/value pairs that will be passed to each handler. (Just make sure your handlers are expecting them. You can add `**kwargs` to your handler methods if certain ones don’t need them.)

Post the queue event called `pizza_time`, and then call `self.pizza_done` when done: `self.machine.events.post_queue('pizza_time', self.pizza_done)`

`post_queue_async(event: str, **kwargs) → _asyncio.Future`

Post queue event, wait until all handlers are done and locks are released.

`post_relay(event: str, callback=None, **kwargs) → None`

Post a relay event which causes all the registered handlers to be called. A dictionary can be passed from handler-to-handler and modified as needed.

Parameters:

* **event** – A string name of the event you’re posting. Note that you can post whatever event you want. You don’t have to set up anything ahead of time, and if no handlers are registered for the event you post, so be it.
* **callback** – The method which will be called when the final handler is done processing this event. Default is None.
* **`**kwargs`** – One or more options keyword/value pairs that will be passed to each handler. (Just make sure your handlers are expecting them. You can add `**kwargs` to your handler methods if certain ones don’t need them.)

Events are processed serially (e.g. one at a time), so if the event core is in the process of handling another event, this event is added to a queue and processed after the current event is done. You can control the order the handlers will be called by optionally specifying a priority when the handlers were registered. (Higher priority values will be processed first.) Relay events differ from standard events in that the resulting kwargs from one handler are passed to the next handler. (In other words, standard events mean that all the handlers get the same initial kwargs, whereas relay events “relay” the resulting kwargs from one handler to the next.)

`post_relay_async(event: str, **kwargs) → _asyncio.Future`

Post relay event, wait until all handlers are done and return result.

`process_event_queue() → None`

Check if there are any other events that need to be processed, and then process them.

`remove_all_handlers_for_event(event: str) → None`

Remove all handlers for event. Use carefully. This is currently used to remove handlers for all init events which only occur once.

`remove_handler(method: Any) → None`

Remove an event handler from all events a method is registered to handle.

Parameters:

* **method** – The method whose handlers you want to remove.

`remove_handler_by_event(event: str, handler: Any) → None`

Remove the handler you pass from the event you pass.

Parameters:

* **event** – The name of the event you want to remove the handler from.
* **handler** – The handler method you want to remove.

Note that keyword arguments for the handler are not taken into consideration. In other words, this method only removes the registered handler / event combination, regardless of whether the keyword arguments match or not.

`remove_handler_by_key(key: mpf.core.events.EventHandlerKey) → None`

Remove a registered event handler by key.

Parameters:

* **key** – The key of the handler you want to remove

`remove_handlers_by_keys(key_list: List[mpf.core.events.EventHandlerKey]) → None`

Remove multiple event handlers based on a passed list of keys.

Parameters:

* **key_list** – A list of keys of the handlers you want to remove

`replace_handler(event: str, handler: Any, priority: int = 1, **kwargs) → mpf.core.events.EventHandlerKey`

Check to see if a handler (optionally with kwargs) is registered for an event and replaces it if so.

Parameters:

* **event** – The event you want to check to see if this handler is registered for.
* **handler** – The method of the handler you want to check.
* **priority** – Optional priority of the new handler that will be registered.
* ****kwargs** – The kwargs you want to check and the kwargs that will be registered with the new handler.

If you don’t pass kwargs, this method will just look for the handler and event combination. If you do pass kwargs, it will make sure they match before replacing the existing entry. If this method doesn’t find a match, it will still add the new handler.

`wait_for_any_event(event_names: List[str]) → _asyncio.Future`

Wait for any event from event_names.

`wait_for_event(event_name: str) → _asyncio.Future`

Wait for event.
