
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
gfx = "RoundHex/terrain"

[grid_top]

x_top_left = 1
y_top_left = 1
dx = 62
dy = 36

tiles = { "row", "column", "tag"
  0,  0, "t.l0.grassland1"
  ;0,  1, Unused
  0,  2, "t.l0.inaccessible1"
  0,  3, "mask.tile"
  0,  4, "t.l0.forest1"
  ;0,  5, Unused
  0,  6, "t.l0.coast1"
  0,  7, "t.l0.floor1"
  0,  8, "t.l0.lake1"

  ; TODO
  0, 10, "t.dither_tile"
}

[grid_bottom]

x_top_left = 1
y_top_left = 38
dx = 31
dy = 18

tiles = { "row", "column", "tag"
  0,  0, "t.l0.plains_hex_cell_right_0_0_1"
  0,  1, "t.l0.plains_hex_cell_left_0_0_1"
  1,  0, "t.l0.plains_hex_cell_left_1_0_1"
  1,  1, "t.l0.plains_hex_cell_right_1_0_1"
  2,  0, "t.l0.plains_hex_cell_right_1_1_1"
  2,  1, "t.l0.plains_hex_cell_left_1_1_1"
  3,  0, "t.l0.plains_hex_cell_left_1_1_0"
  3,  1, "t.l0.plains_hex_cell_right_1_1_0"
  4,  0, "t.l0.plains_hex_cell_right_0_1_1"
  4,  1, "t.l0.plains_hex_cell_left_0_1_1"
  5,  0, "t.l0.plains_hex_cell_left_1_0_0"
  5,  1, "t.l0.plains_hex_cell_right_1_0_0"
  6,  0, "t.l0.plains_hex_cell_right_0_1_0"
  6,  1, "t.l0.plains_hex_cell_left_0_1_0"

  0,  2, "t.l0.desert_hex_cell_right_0_0_1"
  0,  3, "t.l0.desert_hex_cell_left_0_0_1"
  1,  2, "t.l0.desert_hex_cell_left_1_0_1"
  1,  3, "t.l0.desert_hex_cell_right_1_0_1"
  2,  2, "t.l0.desert_hex_cell_right_1_1_1"
  2,  3, "t.l0.desert_hex_cell_left_1_1_1"
  3,  2, "t.l0.desert_hex_cell_left_1_1_0"
  3,  3, "t.l0.desert_hex_cell_right_1_1_0"
  4,  2, "t.l0.desert_hex_cell_right_0_1_1"
  4,  3, "t.l0.desert_hex_cell_left_0_1_1"
  5,  2, "t.l0.desert_hex_cell_left_1_0_0"
  5,  3, "t.l0.desert_hex_cell_right_1_0_0"
  6,  2, "t.l0.desert_hex_cell_right_0_1_0"
  6,  3, "t.l0.desert_hex_cell_left_0_1_0"

  0,  4, "t.l0.swamp_hex_cell_right_0_0_1"
  0,  5, "t.l0.swamp_hex_cell_left_0_0_1"
  1,  4, "t.l0.swamp_hex_cell_left_1_0_1"
  1,  5, "t.l0.swamp_hex_cell_right_1_0_1"
  2,  4, "t.l0.swamp_hex_cell_right_1_1_1"
  2,  5, "t.l0.swamp_hex_cell_left_1_1_1"
  3,  4, "t.l0.swamp_hex_cell_left_1_1_0"
  3,  5, "t.l0.swamp_hex_cell_right_1_1_0"
  4,  4, "t.l0.swamp_hex_cell_right_0_1_1"
  4,  5, "t.l0.swamp_hex_cell_left_0_1_1"
  5,  4, "t.l0.swamp_hex_cell_left_1_0_0"
  5,  5, "t.l0.swamp_hex_cell_right_1_0_0"
  6,  4, "t.l0.swamp_hex_cell_right_0_1_0"
  6,  5, "t.l0.swamp_hex_cell_left_0_1_0"

  0,  6, "t.l0.tundra_hex_cell_right_0_0_1"
  0,  7, "t.l0.tundra_hex_cell_left_0_0_1"
  1,  6, "t.l0.tundra_hex_cell_left_1_0_1"
  1,  7, "t.l0.tundra_hex_cell_right_1_0_1"
  2,  6, "t.l0.tundra_hex_cell_right_1_1_1"
  2,  7, "t.l0.tundra_hex_cell_left_1_1_1"
  3,  6, "t.l0.tundra_hex_cell_left_1_1_0"
  3,  7, "t.l0.tundra_hex_cell_right_1_1_0"
  4,  6, "t.l0.tundra_hex_cell_right_0_1_1"
  4,  7, "t.l0.tundra_hex_cell_left_0_1_1"
  5,  6, "t.l0.tundra_hex_cell_left_1_0_0"
  5,  7, "t.l0.tundra_hex_cell_right_1_0_0"
  6,  6, "t.l0.tundra_hex_cell_right_0_1_0"
  6,  7, "t.l0.tundra_hex_cell_left_0_1_0"

  ; arctic shares the base layer with tundra
  0,  6, "t.l0.arctic_hex_cell_right_0_0_1"
  0,  7, "t.l0.arctic_hex_cell_left_0_0_1"
  1,  6, "t.l0.arctic_hex_cell_left_1_0_1"
  1,  7, "t.l0.arctic_hex_cell_right_1_0_1"
  2,  6, "t.l0.arctic_hex_cell_right_1_1_1"
  2,  7, "t.l0.arctic_hex_cell_left_1_1_1"
  3,  6, "t.l0.arctic_hex_cell_left_1_1_0"
  3,  7, "t.l0.arctic_hex_cell_right_1_1_0"
  4,  6, "t.l0.arctic_hex_cell_right_0_1_1"
  4,  7, "t.l0.arctic_hex_cell_left_0_1_1"
  5,  6, "t.l0.arctic_hex_cell_left_1_0_0"
  5,  7, "t.l0.arctic_hex_cell_right_1_0_0"
  6,  6, "t.l0.arctic_hex_cell_right_0_1_0"
  6,  7, "t.l0.arctic_hex_cell_left_0_1_0"

  0,  8, "t.l0.hills_hex_cell_right_0_0_1"
  0,  9, "t.l0.hills_hex_cell_left_0_0_1"
  1,  8, "t.l0.hills_hex_cell_left_1_0_1"
  1,  9, "t.l0.hills_hex_cell_right_1_0_1"
  2,  8, "t.l0.hills_hex_cell_right_1_1_1"
  2,  9, "t.l0.hills_hex_cell_left_1_1_1"
  3,  8, "t.l0.hills_hex_cell_left_1_1_0"
  3,  9, "t.l0.hills_hex_cell_right_1_1_0"
  4,  8, "t.l0.hills_hex_cell_right_0_1_1"
  4,  9, "t.l0.hills_hex_cell_left_0_1_1"
  5,  8, "t.l0.hills_hex_cell_left_1_0_0"
  5,  9, "t.l0.hills_hex_cell_right_1_0_0"
  6,  8, "t.l0.hills_hex_cell_right_0_1_0"
  6,  9, "t.l0.hills_hex_cell_left_0_1_0"

  0, 10, "t.l0.mountains_hex_cell_right_0_0_1"
  0, 11, "t.l0.mountains_hex_cell_left_0_0_1"
  1, 10, "t.l0.mountains_hex_cell_left_1_0_1"
  1, 11, "t.l0.mountains_hex_cell_right_1_0_1"
  2, 10, "t.l0.mountains_hex_cell_right_1_1_1"
  2, 11, "t.l0.mountains_hex_cell_left_1_1_1"
  3, 10, "t.l0.mountains_hex_cell_left_1_1_0"
  3, 11, "t.l0.mountains_hex_cell_right_1_1_0"
  4, 10, "t.l0.mountains_hex_cell_right_0_1_1"
  4, 11, "t.l0.mountains_hex_cell_left_0_1_1"
  5, 10, "t.l0.mountains_hex_cell_left_1_0_0"
  5, 11, "t.l0.mountains_hex_cell_right_1_0_0"
  6, 10, "t.l0.mountains_hex_cell_right_0_1_0"
  6, 11, "t.l0.mountains_hex_cell_left_0_1_0"

  0, 12, "t.l0.jungle_hex_cell_right_0_0_1"
  0, 13, "t.l0.jungle_hex_cell_left_0_0_1"
  1, 12, "t.l0.jungle_hex_cell_left_1_0_1"
  1, 13, "t.l0.jungle_hex_cell_right_1_0_1"
  2, 12, "t.l0.jungle_hex_cell_right_1_1_1"
  2, 13, "t.l0.jungle_hex_cell_left_1_1_1"
  3, 12, "t.l0.jungle_hex_cell_left_1_1_0"
  3, 13, "t.l0.jungle_hex_cell_right_1_1_0"
  4, 12, "t.l0.jungle_hex_cell_right_0_1_1"
  4, 13, "t.l0.jungle_hex_cell_left_0_1_1"
  5, 12, "t.l0.jungle_hex_cell_left_1_0_0"
  5, 13, "t.l0.jungle_hex_cell_right_1_0_0"
  6, 12, "t.l0.jungle_hex_cell_right_0_1_0"
  6, 13, "t.l0.jungle_hex_cell_left_0_1_0"

  0, 14, "t.l1.arctic_hex_cell_right_0_0_1"
  0, 15, "t.l1.arctic_hex_cell_left_0_0_1"
  1, 14, "t.l1.arctic_hex_cell_left_1_0_1"
  1, 15, "t.l1.arctic_hex_cell_right_1_0_1"
  2, 14, "t.l1.arctic_hex_cell_right_1_1_1"
  2, 15, "t.l1.arctic_hex_cell_left_1_1_1"
  3, 14, "t.l1.arctic_hex_cell_left_1_1_0"
  3, 15, "t.l1.arctic_hex_cell_right_1_1_0"
  4, 14, "t.l1.arctic_hex_cell_right_0_1_1"
  4, 15, "t.l1.arctic_hex_cell_left_0_1_1"
  5, 14, "t.l1.arctic_hex_cell_left_1_0_0"
  5, 15, "t.l1.arctic_hex_cell_right_1_0_0"
  6, 14, "t.l1.arctic_hex_cell_right_0_1_0"
  6, 15, "t.l1.arctic_hex_cell_left_0_1_0"

  0, 16, "t.l1.coast_hex_cell_right_0_0_1"
  0, 17, "t.l1.coast_hex_cell_left_0_0_1"
  1, 16, "t.l1.coast_hex_cell_left_1_0_1"
  1, 17, "t.l1.coast_hex_cell_right_1_0_1"
  2, 16, "t.l1.coast_hex_cell_right_1_1_1"
  2, 17, "t.l1.coast_hex_cell_left_1_1_1"
  3, 16, "t.l1.coast_hex_cell_left_1_1_0"
  3, 17, "t.l1.coast_hex_cell_right_1_1_0"
  4, 16, "t.l1.coast_hex_cell_right_0_1_1"
  4, 17, "t.l1.coast_hex_cell_left_0_1_1"
  5, 16, "t.l1.coast_hex_cell_left_1_0_0"
  5, 17, "t.l1.coast_hex_cell_right_1_0_0"
  6, 16, "t.l1.coast_hex_cell_right_0_1_0"
  6, 17, "t.l1.coast_hex_cell_left_0_1_0"

  0, 16, "t.l1.floor_hex_cell_right_0_0_1"
  0, 17, "t.l1.floor_hex_cell_left_0_0_1"
  1, 16, "t.l1.floor_hex_cell_left_1_0_1"
  1, 17, "t.l1.floor_hex_cell_right_1_0_1"
  2, 16, "t.l1.floor_hex_cell_right_1_1_1"
  2, 17, "t.l1.floor_hex_cell_left_1_1_1"
  3, 16, "t.l1.floor_hex_cell_left_1_1_0"
  3, 17, "t.l1.floor_hex_cell_right_1_1_0"
  4, 16, "t.l1.floor_hex_cell_right_0_1_1"
  4, 17, "t.l1.floor_hex_cell_left_0_1_1"
  5, 16, "t.l1.floor_hex_cell_left_1_0_0"
  5, 17, "t.l1.floor_hex_cell_right_1_0_0"
  6, 16, "t.l1.floor_hex_cell_right_0_1_0"
  6, 17, "t.l1.floor_hex_cell_left_0_1_0"

  0, 16, "t.l1.lake_hex_cell_right_0_0_1"
  0, 17, "t.l1.lake_hex_cell_left_0_0_1"
  1, 16, "t.l1.lake_hex_cell_left_1_0_1"
  1, 17, "t.l1.lake_hex_cell_right_1_0_1"
  2, 16, "t.l1.lake_hex_cell_right_1_1_1"
  2, 17, "t.l1.lake_hex_cell_left_1_1_1"
  3, 16, "t.l1.lake_hex_cell_left_1_1_0"
  3, 17, "t.l1.lake_hex_cell_right_1_1_0"
  4, 16, "t.l1.lake_hex_cell_right_0_1_1"
  4, 17, "t.l1.lake_hex_cell_left_0_1_1"
  5, 16, "t.l1.lake_hex_cell_left_1_0_0"
  5, 17, "t.l1.lake_hex_cell_right_1_0_0"
  6, 16, "t.l1.lake_hex_cell_right_0_1_0"
  6, 17, "t.l1.lake_hex_cell_left_0_1_0"

  ; Matching is inverted
  0, 18, "t.l2.coast_hex_cell_right_0_0_1"
  0, 19, "t.l2.coast_hex_cell_left_0_0_1"
  1, 18, "t.l2.coast_hex_cell_left_1_0_1"
  1, 19, "t.l2.coast_hex_cell_right_1_0_1"
  2, 18, "t.l2.coast_hex_cell_right_1_1_1"
  2, 19, "t.l2.coast_hex_cell_left_1_1_1"
  3, 18, "t.l2.coast_hex_cell_left_1_1_0"
  3, 19, "t.l2.coast_hex_cell_right_1_1_0"
  4, 18, "t.l2.coast_hex_cell_right_0_1_1"
  4, 19, "t.l2.coast_hex_cell_left_0_1_1"
  5, 18, "t.l2.coast_hex_cell_left_1_0_0"
  5, 19, "t.l2.coast_hex_cell_right_1_0_0"
  6, 18, "t.l2.coast_hex_cell_right_0_1_0"
  6, 19, "t.l2.coast_hex_cell_left_0_1_0"

  0, 18, "t.l2.floor_hex_cell_right_0_0_1"
  0, 19, "t.l2.floor_hex_cell_left_0_0_1"
  1, 18, "t.l2.floor_hex_cell_left_1_0_1"
  1, 19, "t.l2.floor_hex_cell_right_1_0_1"
  2, 18, "t.l2.floor_hex_cell_right_1_1_1"
  2, 19, "t.l2.floor_hex_cell_left_1_1_1"
  3, 18, "t.l2.floor_hex_cell_left_1_1_0"
  3, 19, "t.l2.floor_hex_cell_right_1_1_0"
  4, 18, "t.l2.floor_hex_cell_right_0_1_1"
  4, 19, "t.l2.floor_hex_cell_left_0_1_1"
  5, 18, "t.l2.floor_hex_cell_left_1_0_0"
  5, 19, "t.l2.floor_hex_cell_right_1_0_0"
  6, 18, "t.l2.floor_hex_cell_right_0_1_0"
  6, 19, "t.l2.floor_hex_cell_left_0_1_0"

  0, 18, "t.l2.lake_hex_cell_right_0_0_1"
  0, 19, "t.l2.lake_hex_cell_left_0_0_1"
  1, 18, "t.l2.lake_hex_cell_left_1_0_1"
  1, 19, "t.l2.lake_hex_cell_right_1_0_1"
  2, 18, "t.l2.lake_hex_cell_right_1_1_1"
  2, 19, "t.l2.lake_hex_cell_left_1_1_1"
  3, 18, "t.l2.lake_hex_cell_left_1_1_0"
  3, 19, "t.l2.lake_hex_cell_right_1_1_0"
  4, 18, "t.l2.lake_hex_cell_right_0_1_1"
  4, 19, "t.l2.lake_hex_cell_left_0_1_1"
  5, 18, "t.l2.lake_hex_cell_left_1_0_0"
  5, 19, "t.l2.lake_hex_cell_right_1_0_0"
  6, 18, "t.l2.lake_hex_cell_right_0_1_0"
  6, 19, "t.l2.lake_hex_cell_left_0_1_0"
}
