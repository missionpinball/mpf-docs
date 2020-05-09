
Each of the SW-16 boards requires a unique binary address which is set by the board's dipswitches 1 through 6. 
Although the P3-ROC has two serial switch connectors (J11 and J14) there is only one serial switch bus. Meaning, 
if one SW-16 board connects to the P3-ROC through J11 and another through J14 the SW-16 boards will still 
require seperate addresses to be properly registered.  

Similarly, the PD-16 and PD-LED driver boards also each require an unique address on the driver bus accessed through
J12 and J15 on the P3-ROC. If for instance a PD-16 and a PD-LED share on the same address, commands through the 
driver serial bus meant to drive LEDs can acutate coils even if the boards are interfacing through different
plugs.  

On the SW-16, PD-16 and PD-LED boards themselves dipswitch addressing is somewhat counterintuitive. 
Switch one is the lowest address bit and switch 6 is the highest.  Reading the switch block from left (starting 
at switch 1) to right, binary address zero would be 000000, address one through four would be 100000, 010000, 110000
and 001000, respectively.
