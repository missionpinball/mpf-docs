In MPF :doc:`lights </config/lights>` abstract a light source which emits
arbitrary colors.
However, this is not true for all real lights.
Some support only white (GIs), others only a single-color (i.e. red inserts)
and others support full RGB.
For that reason MPF knows :doc:`light numbers and channel numbers </config/lights>`.
Internally, a light consists of one or multiple channels.
For instance, a single-color GI will contain a single white channel.
While a RGB light will control a red, green and a blue channel.
A white light behind a red insert should be a single red channel (because it
cannot emit other colors through the red insert).
You can configure those channels using the ``channels`` setting or use
``start_channel`` and ``type`` to define the channels.
See :doc:`/mechs/lights/index` for details.

However, in most cases a platform supports one type of lights (per ``subtype``)
this would be overly verbose and we added the ``number`` setting for
configuring lights in the common platform way.
For instance a platform for GIs will configure single channel white lights or
a serial LED controller will configure RGB lights with three channels.
