# RPCRC
A sleek and multi-use PTT and voice switch for Discord and VATSIM's Consolidated Radar Client.

<image src="img/cover_close.png" style="height: 200px;">

### Function
A PTT for CRC, a PTT for Discord, and a Toggle Deafen for Discord, as well as RX, SPKR, XC, and XCA switches for CRC's AFV Voice Switch.
### Motive
I don't want to give up my right Alt / Ctrl keys on my keyboard for VATSIM controlling, so I made this with some extra switches.
## Features
* 3 Dedicated MX Switches for PTT and Deafen Toggles
* 4 Dedicated On-Off Switches for RX, SPKR, XC, and XCA Toggles in CRC
<sup>(INOP of 4/2026 due to CRC AFV Restrictions)</sup>
* 3 Green, Blue, and Red LEDs for PTT and Deafen Visual Signaling
* Custom Board with RP2040
* Custom KMK Firmware for ARM Cortex-M0+ on CircuitPython

<sup>(yes, this is a bit exaggerated)</sup>

## CAD
RPCRC is modeled in OnShape. STEPs and GLTFs are available.

## PCB
The Gerber ZIP (`RPCRCv1Final.zip`) and a standard STEP file (`pcb.step`) including sample parts are available.

## Firmware
RPCRC runs on KMK commit `8afe569` with CircuitPython `v10.2.0-alpha.1`.
#### Code `RPCRC/firmware/src/code.py`

#### Upload Files `RPCRC/firmware/upload`

#### KMK `RPCRC/firmware/kmk`

#### CircuitPython `RPCRC/firmware/cpy`

## Images

### PCB
<image src="img/pcb_3d_side.png" style="height: 200px;">

<image src="img/pcb_final.png" style="height: 200px;">

<image src="img/pcb_editor_view.png" style="height: 200px;">

### PCB with Components
<image src="img/pcb_3d_model_side.png" style="height: 200px;">

### Case and Lid
#### Flat Case
<image src="img/cad_case.png" style="height: 200px;">

#### Angled Case (13.85°)
<image src="img/cad_angled_case.png" style="height: 200px;">

#### Lid
<image src="img/cad_lid.png" style="height: 200px;">

### Final Product
#### Standard
<image src="img/assembly_left.png" style="height: 200px;">

<image src="img/assembly_side_angle.png" style="height: 200px;">

<image src="img/assembly_top.png" style="height: 200px;">

#### Angled
<image src="img/assembly_angle_right.png" style="height: 200px;">

<image src="img/assembly_angle_side.png" style="height: 200px;">

## BoM
**Subtotal $32.19**
| Name | Purpose | Quantity | Total Cost (USD) | Link | Distributor |
| :--- | :--- | :---: | :---: | :--- | :--- |
| SMD Stencil | Single Side | 1 | 3.05 | [Link](https://jlcpcb.com) | JLCPCB |
| PCB | FR4 Blue Min 5 | 5 | 4.00 | [Link](https://jlcpcb.com) | JLCPCB |
| 10 R0603 | C109318 Min 100 | 100 | 0.40 | [Link](https://www.lcsc.com/product-detail/C109318.html?s_z=n_10ohm%25200603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVVZVQVJbVzsOAxUeFF5JWBYZEEoKFBINSQcJGk4%3D) | LCSC |
| 100 R0603 | C105588 Min 100 | 100 | 0.14 | [Link](https://www.lcsc.com/product-detail/C105588.html?s_z=n_100%2520ohm%2520r0603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlNUTlhXUDsOAxUeFF5JWBYZEEoKFBINSQcJGk4dAgUUFAk%3D) | LCSC |
| Green L0603 | C965804 Min 100 | 100 | 0.51 | [Link](https://www.lcsc.com/product-detail/C965804.html?spm=wm.fly.bg.3.xh___wm.ppx.1.5.a&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlFWRldYUDsOAxUeFF5JWBYZEEoKFBINSQcJGk4%3D) | LCSC |
| Blue L0603 | C965807 Min 100 | 100 | 0.42 | [Link](https://www.lcsc.com/product-detail/C965807.html?spm=wm.fly.bg.2.xh___wm.ppx.1.5.a&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlFWRldYUDsOAxUeFF5JWBYZEEoKFBINSQcJGk4%3D) | LCSC |
| Red L0603 | C965799 Min 100 | 100 | 0.38 | [Link](https://www.lcsc.com/product-detail/C965799.html?s_z=n_red%2520led&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlFWRldYUDsOAxUeFF5JWBYZEEoKFBINSQcJGk4%3D) | LCSC |
| 27 R0603 | C2907021 Min 100 | 100 | 0.10 | [Link](https://www.lcsc.com/product-detail/C2907021.html?s_z=n_27%2520ohm%25200603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlBXQFRZXzsOAxUeFF5JWBYZEEoKFBINSQcJGk4dAgUUFAk%3D) | LCSC |
| 1K R0603 | C22548 Min 100 | 100 | 0.15 | [Link](https://www.lcsc.com/product-detail/C22548.html?s_z=n_1K%2520R0603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVldTQVNaVzsOAxUeFF5JWBYZEEoKFBINSQcJGk4dAgUUFAk%3D) | LCSC |
| 15pF C0603 | C1644 Min 100 | 100 | 0.54 | [Link](https://www.lcsc.com/product-detail/C1644.html?s_z=n_15pF%2520C0603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVldXRlBWUzsOAxUeFF5JWBYZEEoKFBINSQcJGk4eFQsCAgIaSgADAwAHC0slTllcVVRIHxUDCw%3D%3D) | LCSC |
| 10K R0603 | C98220 Min 100 | 100 | 0.15 | [Link](https://www.lcsc.com/product-detail/C98220.html?s_z=n_10K%2520R0603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlZQRFhfVjsOAxUeFF5JWBYZEEoKFBINSQcJGk4dAgUUFAk%3D) | LCSC |
| 5.1K R0603 | C2907044 Min 100 | 100 | 0.12 | [Link](https://www.lcsc.com/product-detail/C2907044.html?s_z=n_5.1K%2520R0603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlZXT1ZbXjsOAxUeFF5JWBYZEEoKFBINSQcJGk4dAgUUFAk%3D) | LCSC |
| 10uF C0603 | C19702 Min 50 | 50 | 0.40 | [Link](https://www.lcsc.com/product-detail/C19702.html?s_z=n_10uF%2520C0603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlVQQ1ZaVzsOAxUeFF5JWBYZEEoKFBINSQcJGk4dAgUUFAk%3D) | LCSC |
| 0.1uF C0603 | C1591 Min 100 | 100 | 0.28 | [Link](https://www.lcsc.com/product-detail/C1591.html?s_z=n_0.1uF%2520C0603&spm=wm.ssy.bg.1.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlVWQ1RfVTsOAxUeFF5JWBYZEEoKFBINSQcJGk4eFQsCAgIaSgADAwAHC0slRlRWU11IHxUDCw%3D%3D) | LCSC |
| 1uF C0603 | C15849 Min 50 | 50 | 0.39 | [Link](https://www.lcsc.com/product-detail/C15849.html?s_z=n_1uF%25200603&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbVlRTTlBWVjsOAxUeFF5JWBYZEEoKFBINSQcJGk4%3D) | LCSC |
| Pushbutton | C49234152 Min 20 | 20 | 0.64 | [Link](https://www.lcsc.com/product-detail/C49234152.html?s_z=n_C49234152) | LCSC |
| On-Off Switch | C1788492 | 10 | 5.16 | [Link](https://www.lcsc.com/product-detail/C1788492.html) | LCSC |
| RP2040 | C2040 | 5 | 4.74 | [Link](https://www.lcsc.com/product-detail/C2040.html?s_z=n_RP2040&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbV1xfQVlXVjsOAxUeFF5JWBYZEEoKFBINSQcJGk4eFQsCAgIaSgADAwAHC0slTlZbVVVIHxUDCw%3D%3D) | LCSC |
| 16MB Flash | C97521 | 4 | 7.83 | [Link](https://www.lcsc.com/product-detail/C97521.html?s_z=n_W25Q128JVSIQ&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbV1xVRFBXUzsOAxUeFF5JWBYZEEoKFBINSQcJGk4eFQsCAgIaSgADAwAHC0slQlBfVlxIHxUDCw%3D%3D) | LCSC |
| 3.3V LDO | C51118 Min 5 | 5 | 0.73 | [Link](https://www.lcsc.com/product-detail/C51118.html?s_z=n_AP2112K-3.3TRG1&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbV1NUTlJYVDsOAxUeFF5JWBYZEEoKFBINSQcJGk4eFQsCAgIaSgADAwAHC0slRVZYUlVeQU8GEwkK) | LCSC |
| USB-C 16pin | C2765186 Min 20 | 20 | 1.33 | [Link](https://www.lcsc.com/product-detail/C2765186.html?s_z=n_TYPE-C%252016PIN%25202MD%28073%29&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbV1JeQlldUzsOAxUeFF5JWBYZEEoKFBINSQcJGk4eFQsCAgIaSgADAwAHC0slTlFeVUoOAwwC) | LCSC |
| 12MHz Crystal | C9002 Min 10 | 10 | 0.73 | [Link](https://www.lcsc.com/product-detail/C9002.html?s_z=n_12mhz&spm=wm.ssy.bg.0.xh&lcsc_vid=QgIPUwJUQQdcBgFSRgdeV1RWQ1NfAgADFQUNUAdRQgcxVlNRQVBbV1FfT1RfUTsOAxUeFF5JWBYZEEoKFBINSQcJGk4%3D) | LCSC |

_Excludes applicable tax, shipping, and tools._

## Copyright
**Copyright 2026 Jeongwoo "Ryan" Kim KO6LVM. All rights reserved.**