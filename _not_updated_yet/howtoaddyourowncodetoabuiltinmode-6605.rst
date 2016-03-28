
You can add your own attract mode folder and add your own attract.py
code, and then just have that code subclass the built-in Attract Mode
instead of just plain “Mode”, and it should be nice and clean and not
break anything. Here’s a skeleton structure. (I should make this a How
To guide.)


::

    
    import mpf.modes.attract.code.attract
    
    class Attract(mpf.modes.attract.code.attract.Attract):
    
        def mode_init(self):
            pass
    
        def mode_start(self, **kwargs):
            super(Attract, self).mode_start(**kwargs)
    
            pass
    
        def mode_stop(self, **kwargs):
            pass


Right now I do a lot in the mode_start() for the built-in attract mode
which is why you need to call super(). I should probably change that
so you can use mode_start() like any mode. But if you use this and put
your code in the “pass” sections then you should be good. So use this
code as the template for your
your_machine/modes/attract/code/attract.py module, and remember to add
the blank __init__.py files to the whole structure (one each in your
your modes, attract, and code folders) and you should be good to go.



