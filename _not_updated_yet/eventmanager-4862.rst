
The Event Manager is responsible for all aspects of MPF's event-driven
control system. It lives in the *mpf/system/events.py* module. The
event manager handles registering and removing event handlers,
receiving commands to post events, the processing and calling of
handlers for events that have been posted, and for calling callbacks
once events have been completed. The event manager maintains a queue
of events that are in-progress. The event manager is also responsible
for setting up and maintaining event monitors which are ways that
other processes can be notified of all events that are posted. (The
BCP interface uses this, as well as tools that plug in to show the
state of the event system.)



