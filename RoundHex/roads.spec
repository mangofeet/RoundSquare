
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
gfx = "RoundHex/roads"

[grid_top]

x_top_left = 1
y_top_left = 1
dx = 62
dy = 36
pixel_border = 1

tiles = { "row", "column", "tag"
  4, 0, "road.road_isolated"
  0, 0, "road.road_c_n0se0w1"
  0, 1, "road.road_c_n0se1w0"
  0, 2, "road.road_c_n0se1w1"
  0, 3, "road.road_c_n1se0w0"
  0, 4, "road.road_c_n1se0w1"
  0, 5, "road.road_c_n1se1w0"
  0, 6, "road.road_c_n1se1w1"

  1, 0, "road.road_d_e0s0nw1"
  1, 1, "road.road_d_e0s1nw0"
  1, 2, "road.road_d_e0s1nw1"
  1, 3, "road.road_d_e1s0nw0"
  1, 4, "road.road_d_e1s0nw1"
  1, 5, "road.road_d_e1s1nw0"
  1, 6, "road.road_d_e1s1nw1"

  0, 0, "road.rail_isolated"
  0, 0, "road.rail_c_n0se0w1"
  0, 0, "road.rail_c_n0se1w0"
  0, 0, "road.rail_c_n0se1w1"
  0, 0, "road.rail_c_n1se0w0"
  0, 0, "road.rail_c_n1se0w1"
  0, 0, "road.rail_c_n1se1w0"
  0, 0, "road.rail_c_n1se1w1"

  0, 0, "road.rail_d_e0s0nw1"
  0, 0, "road.rail_d_e0s1nw0"
  0, 0, "road.rail_d_e0s1nw1"
  0, 0, "road.rail_d_e1s0nw0"
  0, 0, "road.rail_d_e1s0nw1"
  0, 0, "road.rail_d_e1s1nw0"
  0, 0, "road.rail_d_e1s1nw1"

  0, 0, "road.maglev_isolated"
  0, 0, "road.maglev_c_n0se0w1"
  0, 0, "road.maglev_c_n0se1w0"
  0, 0, "road.maglev_c_n0se1w1"
  0, 0, "road.maglev_c_n1se0w0"
  0, 0, "road.maglev_c_n1se0w1"
  0, 0, "road.maglev_c_n1se1w0"
  0, 0, "road.maglev_c_n1se1w1"

  0, 0, "road.maglev_d_e0s0nw1"
  0, 0, "road.maglev_d_e0s1nw0"
  0, 0, "road.maglev_d_e0s1nw1"
  0, 0, "road.maglev_d_e1s0nw0"
  0, 0, "road.maglev_d_e1s0nw1"
  0, 0, "road.maglev_d_e1s1nw0"
  0, 0, "road.maglev_d_e1s1nw1"
}
