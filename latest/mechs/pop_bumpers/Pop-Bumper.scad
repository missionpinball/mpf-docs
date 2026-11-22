base_thickness = 4;

module cubes() { //little cubes for the switch to be mounted
    cube([70, 10, base_thickness]);
    translate(v = [0, 10, 0]) cube([25, 15, base_thickness]);
}

module bar() { //make holes into the cube structure to mount the switch
    translate(v = [-62, -5, 0])
    difference() {
        cubes();
        translate(v = [5.5, 19, -base_thickness / 2]) cylinder(h = 2 * base_thickness, r1 = 1, r2 = 4);
        translate(v = [15, 19, -base_thickness / 2]) cylinder(h = 2 * base_thickness, r1 = 1, r2 = 4);
        translate(v = [62, 19, -base_thickness / 2]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    }
}

module body_holes() //for pop bumper body holes wires and screws, needs to be rotated later
{
    translate(v = [-10.5, 0, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    translate(v = [10.5, 0, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);

    translate(v = [0, -10.5, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    translate(v = [0, 10.5, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
}

module print_body() {   //solid body, the disc itself plus the 3 bars
    cylinder(h = 5, r = 37.5);
    rotate([0, 0, -90]) bar();
    rotate([0, 0, -45]) bar();
    rotate([0, 0, -135]) bar();
}

difference() {  //now poking all the holes into the solid body

    print_body();

    //large circle for pop bumber base diameter around 17mm
    cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    translate(v = [4, -2, 1]) linear_extrude(height = 5) text("17", size = 4);

    //two circles for pop bumber rods diameter around 8mm so they can move freely
    translate(v = [-17.5, 0, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    translate(v = [17.5, 0, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    translate(v = [-19.5, 5, 1]) linear_extrude(height = 5) text("8", size = 4);
    translate(v = [15.5, 5, 1]) linear_extrude(height = 5) text("8", size = 4);

    //three circles for the coil bracket, diameter around 5mm
    translate(v = [-25, -14, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    translate(v = [25, -14, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    translate(v = [0, -30, -base_thickness / 100]) cylinder(h = 2 * base_thickness, r1 = 2, r2 = 4);
    translate(v = [-26.5, -10, 1]) linear_extrude(height = 5) text("5", size = 4);
    translate(v = [23.5, -10, 1]) linear_extrude(height = 5) text("5", size = 4);
    translate(v = [-1.5, -25, 1]) linear_extrude(height = 5) text("5", size = 4);

    //four holes for the pop bumper body (2 for screws 2 for wires)
    rotate([0, 0, 45]) body_holes();
    translate(v = [6, -16, 1]) linear_extrude(height = 5) text("2", size = 4);
    translate(v = [6, 12, 1]) linear_extrude(height = 5) text("2", size = 4);
    translate(v = [-9, -16, 1]) linear_extrude(height = 5) text("2", size = 4);
    translate(v = [-9, 12, 1]) linear_extrude(height = 5) text("2", size = 4);

}

translate(v = [-15, 25, 1]) linear_extrude(height = 5) text("Pop Bumper", size = 4);
