# About the Electronic

A small bit of electronic hacking is required for now. You need to power the XL-320 motors with 7.5V and the MX-28 with 12V.

The cables between motors have two purposes:

* Distribute alimentation to each motor
* Convey messages to each motor (ordering them to move or asking them for sensors' values)

Thus the alimentation should be added between the USB2AX (that deals with communication aspects) and the motors.
To this end simply create the following card that can power both type of motors.

![elec1](img/electronic/elec1.jpg)

## Bill of Materials

| Part Name      | Quantity |   Note   |
| --------------:|:--------:|:--------:|
| base           |    1     |          |
| U_horn_to_horn |    1     |          |
| U_side_to_horn |    1     |          |
| shift_one_side |    6     |          |
| pen_holder     |    1     | Optional |
