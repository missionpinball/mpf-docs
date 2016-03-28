
The "Blink" decorator is used to cause a display element to blink. You
can specify the on time and off time (in seconds), as well as how many
times you want the element to blink. Here's a demo of it in action.
Notice that the decorator continues to function even as the slide is
transitioning out. https://www.youtube.com/watch?v=tFNq-wJNGEs



Settings
~~~~~~~~


+ Decorator name as it's entered into YAML files: `blink`
+ on_secs: The number of seconds the element is on. Decimals are ok.
+ off_secs: The number of seconds the element is off. Decimals are ok.
+ repeats: The number of times the blinking will repeat. Enter `-1`
  for forever.




Example Usage
~~~~~~~~~~~~~

Here's an example of how to apply this decorator to text which is in a
show file. Notice that the decorator only applies to the "PRESS START"
text, and not the "FREE PLAY" text.


::

    
    - tocks: 3
      display:
        - type: Text
          text: "(PRESS START)"
          decorators:
            type: blink
            repeats: -1
            on_secs: .4
            off_secs: .4
        - type: Text
          text: "(FREE PLAY)"
          color: 00ff00
          v_pos: bottom
          font: small
          transition:
            type: move_in
            duration: 1s
            direction: right




