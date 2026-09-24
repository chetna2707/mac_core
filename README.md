# 8-Bit MAC Core — RTL-to-GDSII Physical Design Flow (SkyWater 130nm)

This repository contains the complete open-source ASIC physical design implementation for an 8-bit × 8-bit pipelined Multiply-Accumulate (MAC) core (`mac_core`) with a 16-bit multiplier output and 20-bit accumulator, targeted for the **SkyWater 130nm HD PDK (`sky130_fd_sc_hd`)**.

The backend flow executes Verilog RTL logic synthesis using Yosys, performs floorplanning, placement, clock tree synthesis (CTS), and multi-layer detailed routing in OpenROAD, performs Static Timing Analysis (STA), and exports the final GDSII layout using KLayout's Python API.

---


## Technical Specifications & Physical Metrics

| Parameter | Value |
| --- | --- |
| Design Top Module | mac_core (8×8 Pipelined MAC) |
| Technology Node | SkyWater 130nm (sky130A) |
| Standard Cell Library | sky130_fd_sc_hd (High Density) |
| Total Placed Components | 960 cells (413 active logic + 547 filler cells) |
| Sequential Flip-Flops | 36 DFFs (sky130_fd_sc_hd__dfrtp_1) |
| I/O Pin Count | 39 pins |
| Routing Nets / Terminals | 432 nets / 5,279 terminals |
| Die Dimensions | 100 um x 100 um |
| Total Die Footprint Area | 10,000 um^2 (0.01 mm^2) |
| Standard Cell Logic Area | 3,535 um^2 |
| Core Cell Utilization | 56% |
| Max Operating Frequency (f_max) | 175.1 MHz (5.71 ns Critical Path) |
| Setup Worst Slack (WNS Max) | +14.29 ns |
| Hold Worst Slack (WNS Min) | +0.42 ns |
| Total Power Consumption | 0.368 mW (368 uW) |
| Routing Metal Layers Used | met1 through met5 |
| DRC / LVS Status | PASSED (0 Violations) |
| Final Output File | mac_core.gds (4.4 MB) |

---

## ASIC Execution Flow

1. Verilog RTL (mac_core.v) -> Yosys Logic Synthesis (sky130_fd_sc_hd)
2. Logic Synthesis -> Gate-Level Netlist (mac_core.v)
3. Gate-Level Netlist -> OpenROAD Physical Design (Floorplanning, Placement, CTS, TritonRoute)
4. OpenROAD PnR -> Routed DEF (mac_core_routed.def) + STA Analysis
5. Routed DEF -> KLayout Stream-Out (def2gds API) -> Tapeout GDSII (mac_core.gds)

---

## Standard Cell Logic Breakdown

- Sequential Logic: 36 D-Flip-Flops (sky130_fd_sc_hd__dfrtp_1)
- Combinational Gates: 377 cells (70 NAND2, 59 XNOR2, 52 NOR2, 37 Majority Gates, 26 AOI21, 24 XOR2, etc.)
- Clock / Isolation Buffers: 14 cells (7 clkinv_1, 7 level iso-buffers)
- Filler Cells: 547 cells (fill_8: 172, fill_1: 142, fill_2: 129, fill_4: 104)

---

## Power Breakdown

- Internal Power: 0.248 mW (67.2%)
- Switching Power: 0.121 mW (32.8%)
- Leakage Power: 1.43 nW (0.0%)
- Total Power: 0.368 mW

---

## Repository Structure

- mac_core.v : Verilog RTL Top Module
- mac_core_routed.def : Routed DEF file with power grid and cell placements
- run_sta.tcl : OpenROAD Static Timing Analysis script
- run_lvs_area.tcl : LVS and design area reporting script
- def2gds.py : KLayout Python API script for GDSII stream-out
- mac_core.gds : Final 4.4 MB GDSII Tapeout Layout File
- README.md : Project Documentation

---

## How to Reproduce Flow & Stream-Out

### 1. Run Static Timing Analysis & Power Reporting
openroad -exit run_sta.tcl

### 2. Stream Out Routed DEF to GDSII
klayout -b -r def2gds.py
