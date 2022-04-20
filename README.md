# Pathifier

Playing with representing marks as SVG path templates.

I have found the
[Mozilla docs](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d) to
be very helpful when working on this project.

## Path commands

Path commands are instructions that define a path to be drawn. Each command is
composed of a command letter and numbers that represent the command parameters.

SVG defines 6 types of path commands, for a total of 20 commands:

- MoveTo: M, m
- LineTo: L, l, H, h, V, v
- Cubic Bézier Curve: C, c, S, s
- Quadratic Bézier Curve: Q, q, T, t
- Elliptical Arc Curve: A, a
- ClosePath: Z, z
