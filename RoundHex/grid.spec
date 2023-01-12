
[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]

artists = "
    Jason Dorje Short <jdorje@freeciv.org>
    Hans Lemurson
    Louis Moureaux <louis94>
"

[file]
gfx = "RoundHex/grid"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 62
dy = 36
pixel_border = 1

tiles = { "row", "column", "tag"
  0,  0, "grid.coastline.ud"
  0,  1, "grid.coastline.ns"
  0,  2, "grid.coastline.we"

  1,  0, "grid.selected.ud"
  1,  1, "grid.selected.ns"
  1,  2, "grid.selected.we"

  2,  0, "grid.worked.ud"
  2,  1, "grid.worked.ns"
  2,  2, "grid.worked.we"

  3,  0, "grid.city.ud"
  3,  1, "grid.city.ns"
  3,  2, "grid.city.we"

  4,  0, "grid.main.ud"
  4,  1, "grid.main.ns"
  4,  2, "grid.main.we"

  0,  3, "grid.unavailable"
  0,  4, "grid.nonnative"

  1,  3, "grid.borders.d"
  1,  4, "grid.borders.u"

  2,  3, "grid.borders.s"
  2,  4, "grid.borders.n"

  3,  3, "grid.borders.w"
  3,  4, "grid.borders.e"
}
