
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]

artists = "
    Tatu Rissanen <tatu.rissanen@hut.fi>
    Jeff Mallatt <jjm@codewell.com> (miscellaneous)
    Eleazar (buoy)
    Vincent Croisier <vincent.croisier@advalvas.be> (ruins)
    Michael Johnson <justaguest> (nuke explosion)
    The Square Cow (inaccessible terrain)
    GriffonSpade
    Hans Lemurson (remade most terrain)
    Louis Moureaux <louis94>
"

[file]
gfx = "RoundHex/rivers"

[grid_top]

x_top_left = 1
y_top_left = 1
dx = 62
dy = 36
pixel_border = 1

tiles = { "row", "column", "tag"
  11, 1, "road.river_s_n0e0se0s0w0nw0"
  0,  5, "road.river_s_n0e0se0s0w0nw1"
  5,  5, "road.river_s_n0e0se0s0w1nw0"
  0,  4, "road.river_s_n0e0se0s0w1nw1"
  4,  5, "road.river_s_n0e0se0s1w0nw0"
  0,  3, "road.river_s_n0e0se0s1w0nw1"
  4,  4, "road.river_s_n0e0se0s1w1nw0"
  8,  2, "road.river_s_n0e0se0s1w1nw1"

  3,  5, "road.river_s_n0e0se1s0w0nw0"
  0,  2, "road.river_s_n0e0se1s0w0nw1"
  3,  4, "road.river_s_n0e0se1s0w1nw0"
  9,  4, "road.river_s_n0e0se1s0w1nw1"
  3,  3, "road.river_s_n0e0se1s1w0nw0"
  9,  3, "road.river_s_n0e0se1s1w0nw1"
  8,  3, "road.river_s_n0e0se1s1w1nw0"
  2,  1, "road.river_s_n0e0se1s1w1nw1"

  2,  5, "road.river_s_n0e1se0s0w0nw0"
  0,  1, "road.river_s_n0e1se0s0w0nw1"
  2,  4, "road.river_s_n0e1se0s0w1nw0"
  9,  2, "road.river_s_n0e1se0s0w1nw1"
  2,  3, "road.river_s_n0e1se0s1w0nw0"
  9,  1, "road.river_s_n0e1se0s1w0nw1"
  7,  3, "road.river_s_n0e1se0s1w1nw0"
  3,  1, "road.river_s_n0e1se0s1w1nw1"

  2,  2, "road.river_s_n0e1se1s0w0nw0"
  8,  1, "road.river_s_n0e1se1s0w0nw1"
  10, 4, "road.river_s_n0e1se1s0w1nw0"
  4,  1, "road.river_s_n0e1se1s0w1nw1"
  10, 3, "road.river_s_n0e1se1s1w0nw0"
  5,  1, "road.river_s_n0e1se1s1w0nw1"
  1,  0, "road.river_s_n0e1se1s1w1nw0"
  7,  0, "road.river_s_n0e1se1s1w1nw1"

  1,  5, "road.river_s_n1e0se0s0w0nw0"
  1,  1, "road.river_s_n1e0se0s0w0nw1"
  1,  4, "road.river_s_n1e0se0s0w1nw0"
  6,  4, "road.river_s_n1e0se0s0w1nw1"
  1,  3, "road.river_s_n1e0se0s1w0nw0"
  6,  3, "road.river_s_n1e0se0s1w0nw1"
  7,  4, "road.river_s_n1e0se0s1w1nw0"
  3,  2, "road.river_s_n1e0se0s1w1nw1"

  1,  2, "road.river_s_n1e0se1s0w0nw0"
  6,  2, "road.river_s_n1e0se1s0w0nw1"
  10, 2, "road.river_s_n1e0se1s0w1nw0"
  4,  2, "road.river_s_n1e0se1s0w1nw1"
  10, 1, "road.river_s_n1e0se1s1w0nw0"
  5,  2, "road.river_s_n1e0se1s1w0nw1"
  2,  0, "road.river_s_n1e0se1s1w1nw0"
  8,  0, "road.river_s_n1e0se1s1w1nw1"

  0,  0, "road.river_s_n1e1se0s0w0nw0"
  6,  1, "road.river_s_n1e1se0s0w0nw1"
  8,  4, "road.river_s_n1e1se0s0w1nw0"
  4,  3, "road.river_s_n1e1se0s0w1nw1"
  7,  2, "road.river_s_n1e1se0s1w0nw0"
  5,  3, "road.river_s_n1e1se0s1w0nw1"
  3,  0, "road.river_s_n1e1se0s1w1nw0"
  9,  0, "road.river_s_n1e1se0s1w1nw1"

  7,  1, "road.river_s_n1e1se1s0w0nw0"
  5,  4, "road.river_s_n1e1se1s0w0nw1"
  4,  0, "road.river_s_n1e1se1s0w1nw0"
  10, 0, "road.river_s_n1e1se1s0w1nw1"
  5,  0, "road.river_s_n1e1se1s1w0nw0"
  11, 0, "road.river_s_n1e1se1s1w0nw1"
  6,  0, "road.river_s_n1e1se1s1w1nw0"
  11, 2, "road.river_s_n1e1se1s1w1nw1"

  6,  5, "road.river_outlet_nw"
  7,  5, "road.river_outlet_w"
  7,  5, "road.river_outlet_sw" ; Unused but required
  8,  5, "road.river_outlet_s"
  9,  5, "road.river_outlet_se"
  10, 5, "road.river_outlet_e"
  10, 5, "road.river_outlet_ne" ; Unused but required
  11, 5, "road.river_outlet_n"
}
