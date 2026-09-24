import pya
import os

layout = pya.Layout()
options = pya.LoadLayoutOptions()

# Explicitly register both LEFs into the LEF/DEF importer options
options.lefdef_config.lef_files = [
    "lef/sky130_fd_sc_hd.tech.lef",
    "lef/sky130_fd_sc_hd.lef"
]

cell_gds = "/home/chetna/.ciel/ciel/sky130/versions/8afc8346a57fe1ab7934ba5a6056ea8b43078e71/sky130A/libs.ref/sky130_fd_sc_hd/gds/sky130_fd_sc_hd.gds"

if os.path.exists(cell_gds):
    print("1. Reading Standard Cell Library GDS...")
    layout.read(cell_gds, options)

print("2. Reading Routed DEF with configured LEF files...")
layout.read("mac_core_routed.def", options)

print("3. Writing Tapeout GDSII...")
layout.write("mac_core.gds")
print("SUCCESS: mac_core.gds generated successfully!")
